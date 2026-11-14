# Converses de casa — publishing guide

This section uses the site's existing Jekyll `_posts/` collection. No additional plugins are required.

## Write and publish

1. Create a Markdown file named `_posts/YYYY-MM-DD-short-slug.md` (see template below). Keep unpublished family conversations **outside this public repository**, including its branches and commit history.
2. Set `categories: [converses-de-casa]`, `lang: ca`, and a stable `translation_key`.
3. Open a pull request and merge when ready. The Catalan post will appear at `/converses-de-casa/`.
4. To add translations, make separate posts with `lang: es` or `lang: en`, the **same** `translation_key`, and a distinct localized `permalink`. They appear in the corresponding language index and cross-link automatically.
5. Copy the **body below the YAML front matter** into Substack. Rich-text pasting from the rendered page may preserve formatting better than raw Markdown. Upload images separately if needed.

## Example (fictional text only — do not publish verbatim)

```markdown
---
layout: conversa
title: "Una pregunta"
date: 2026-11-14
categories: [converses-de-casa]
tags: [preguntes]
lang: ca
translation_key: una-pregunta-2026-11-14
permalink: /converses-de-casa/una-pregunta/
excerpt: "Una conversa breu."
author_profile: true
comments: false
share: false
related: false
---

**Infant:** Una pregunta...

**Jo:** Què et sembla?
```

For the Spanish translation, use `lang: es` and `permalink: /es/converses-de-casa/una-pregunta/`. For English, use `lang: en` and `permalink: /en/converses-de-casa/a-question/`.

The indexes filter by the `converses-de-casa` category and language; older posts elsewhere on the site are unaffected.

**Privacy:** Don't publish real names, identifying details, photographs, or private stories without careful consideration. Deleting a post from the published site does not erase its history from a public Git repository.
