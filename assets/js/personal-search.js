(function () {
  const input = document.getElementById('personal-search-input');
  const resultsContainer = document.getElementById('personal-search-results');
  const defaultList = document.getElementById('personal-search-list');

  if (!input || !resultsContainer || !defaultList) {
    return;
  }

  let index = null;
  let indexPromise = null;
  let lastQuery = '';
  const searchSrc = input.getAttribute('data-search-src') || '/search-personal.json';
  const tagsLabel = input.getAttribute('data-tags-label') || 'Tags:';

  const escapeHtml = (value) => {
    return String(value).replace(/[&<>"']/g, (char) => {
      switch (char) {
        case '&':
          return '&amp;';
        case '<':
          return '&lt;';
        case '>':
          return '&gt;';
        case '"':
          return '&quot;';
        case "'":
          return '&#39;';
        default:
          return char;
      }
    });
  };

  const normalise = (value) => String(value).toLowerCase();

  const firstWords = (text, wordLimit) => {
    const trimmed = text.trim();
    if (!trimmed) {
      return '';
    }
    const words = trimmed.split(/\s+/);
    if (words.length <= wordLimit) {
      return trimmed;
    }
    return words.slice(0, wordLimit).join(' ') + '...';
  };

  const formatDate = (value) => {
    const parsed = new Date(value);
    if (Number.isNaN(parsed.getTime())) {
      return value;
    }
    try {
      return parsed.toLocaleDateString(document.documentElement.lang || 'en', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
      });
    } catch (error) {
      return value;
    }
  };

  const buildResultNode = (post) => {
    const wrapper = document.createElement('div');
    wrapper.className = 'list__item';

    const article = document.createElement('article');
    article.className = 'archive__item';
    article.setAttribute('itemscope', '');
    article.setAttribute('itemtype', 'http://schema.org/CreativeWork');

    const heading = document.createElement('h2');
    heading.className = 'archive__item-title';
    heading.setAttribute('itemprop', 'headline');

    const link = document.createElement('a');
    link.href = post.url;
    link.setAttribute('rel', 'permalink');
    link.textContent = post.title;
    heading.appendChild(link);
    article.appendChild(heading);

    if (post.date) {
      const date = document.createElement('p');
      date.className = 'page__date';
      date.innerHTML = '<strong><i class="fa fa-fw fa-calendar" aria-hidden="true"></i> Published:</strong> ' +
        '<time datetime="' + escapeHtml(post.date) + '">' + escapeHtml(formatDate(post.date)) + '</time>';
      article.appendChild(date);
    }

    if (post.content) {
      const excerpt = document.createElement('p');
      excerpt.className = 'archive__item-excerpt';
      excerpt.setAttribute('itemprop', 'description');
      excerpt.textContent = firstWords(post.content, 30);
      article.appendChild(excerpt);
    }

    if (Array.isArray(post.tags) && post.tags.length) {
      const tagsPara = document.createElement('p');
      tagsPara.className = 'archive__item-tags';

      const label = document.createElement('strong');
      label.innerHTML = '<i class="fa fa-fw fa-tags" aria-hidden="true"></i> ' + escapeHtml(tagsLabel);
      tagsPara.appendChild(label);

      tagsPara.appendChild(document.createTextNode(' '));

      post.tags.forEach((tag, index) => {
        const tagSpan = document.createElement('span');
        tagSpan.className = 'archive__item-tag';
        tagSpan.textContent = tag;
        tagsPara.appendChild(tagSpan);

        if (index < post.tags.length - 1) {
          const separator = document.createElement('span');
          separator.className = 'sep';
          separator.textContent = ', ';
          tagsPara.appendChild(separator);
        }
      });

      article.appendChild(tagsPara);
    }

    wrapper.appendChild(article);
    return wrapper;
  };

  const setResults = (query, posts, errorMessage) => {
    if (!query) {
      resultsContainer.innerHTML = '';
      resultsContainer.hidden = true;
      defaultList.hidden = false;
      return;
    }

    defaultList.hidden = true;
    resultsContainer.hidden = false;

    if (errorMessage) {
      resultsContainer.innerHTML = '<p class="archive__search-error">' + escapeHtml(errorMessage) + '</p>';
      return;
    }

    if (!posts.length) {
      resultsContainer.innerHTML = '<p class="archive__search-empty">No posts found for "' + escapeHtml(query) + '".</p>';
      return;
    }

    const fragment = document.createDocumentFragment();
    posts.forEach((post) => {
      fragment.appendChild(buildResultNode(post));
    });

    resultsContainer.innerHTML = '';
    resultsContainer.appendChild(fragment);
  };

  const loadIndex = () => {
    if (index) {
      return Promise.resolve(index);
    }
    if (!indexPromise) {
      indexPromise = fetch(searchSrc, {
        headers: {
          Accept: 'application/json'
        }
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error('Failed to load search index');
          }
          return response.json();
        })
        .then((data) => {
          if (!Array.isArray(data)) {
            throw new Error('Search index is not an array');
          }
          index = data.map((item) => {
            const content = (item.content || '').toString();
            const categories = Array.isArray(item.categories) ? item.categories : [];
            const tags = Array.isArray(item.tags) ? item.tags : [];
            const title = item.title || '';
            const searchText = normalise([title, content, categories.join(' '), tags.join(' ')].join(' '));

            return {
              title,
              url: item.url || '#',
              date: item.date || '',
              content,
              categories,
              tags,
              searchText
            };
          });
          return index;
        })
        .catch((error) => {
          console.error(error);
          indexPromise = null;
          throw error;
        });
    }
    return indexPromise;
  };

  const handleInput = (event) => {
    const query = event.target.value.trim();
    lastQuery = query;

    if (!query) {
      setResults('', []);
      return;
    }

    const currentQuery = query;
    loadIndex()
      .then((posts) => {
        const terms = query.split(/\s+/).map(normalise).filter(Boolean);
        if (!terms.length) {
          setResults('', []);
          return;
        }
        const matches = posts.filter((post) => terms.every((term) => post.searchText.includes(term)));
        if (currentQuery !== lastQuery) {
          return;
        }
        setResults(currentQuery, matches);
      })
      .catch(() => {
        if (currentQuery !== lastQuery) {
          return;
        }
        setResults(currentQuery, [], 'Unable to load search data right now.');
      });
  };

  input.addEventListener('input', handleInput);
  input.addEventListener('search', handleInput);
})();
