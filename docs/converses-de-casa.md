# Converses de casa — Substack-first publishing

**Substack is the source of truth.** Publish the original story at https://gboschbo.substack.com/ and let a GitHub Action propose corresponding changes to this Jekyll website.

## Automatic review workflow

1. Publish a public article on Substack.
2. The workflow `.github/workflows/sync-substack.yml` checks `https://gboschbo.substack.com/feed` each day (06:17 UTC), or on demand via **Actions → Propose Substack conversation sync → Run workflow**.
3. `scripts/sync_substack.py` reads the public RSS items and produces Markdown in `_posts/YYYY-MM-DD-substack-<slug>.md`.
4. `peter-evans/create-pull-request` opens **or updates** a single PR from `automation/substack-converses-sync` to `master`. If nothing changed, no new PR is created.
5. Review the Markdown, language, sensitive details, images, and formatting. **Only you decide whether to merge.** The automation never merges its own PR and never writes imported posts directly to `master`.

### Initial setup

- Merge the section/setup PR first; GitHub only schedules workflows from the repository default branch (`master` in this repository).
- In **Repository Settings → Actions → General → Workflow permissions**, allow GitHub Actions to create pull requests (if your organization/repository has that setting disabled). The workflow requires `contents: write` and `pull-requests: write` for its automatically generated branch and PR.
- If the feed is temporarily empty or unreachable, the importer fails without proposing removal of content.
- **Tests:** `python -m unittest discover -s tests -p 'test_sync_substack.py' -v` (requires the dependencies installed by the workflow).

### What gets imported

- Every public article currently listed in the RSS feed, including new or edited articles while they remain in the feed. RSS typically includes only recent items; this is **not** a comprehensive archival backup of older posts.
- Category `converses-de-casa` and tag `substack`, using the existing Jekyll post layout.
- Catalan (`lang: ca`) by default, or Spanish/English if an explicit Substack tag says so. Check this manually; automatic language detection isn't attempted.
- Source URL stored as `substack_url`; this is used to update the same post instead of duplicating it. Imported files are identifiable by `-substack-` in their filename.
- Remote image URLs are retained, **not downloaded locally**. The conversion is best-effort; embedded elements, custom styling, and newsletters with rich layouts may need manual adjustments.

**Important:** Don't hand-edit an automatically imported `-substack-` Markdown file and expect the changes to persist after the next sync: the next RSS import will replace its generated contents. Edit the source on Substack or adjust it within the proposed PR before merging. Translation links can be connected using a shared `translation_key` when needed.

### Visibility / privacy

The GitHub repository and its PR branches are public, so proposed imports are publicly visible in the PR **before** you merge, even though they are not on the published website. Publish only content on Substack that you are comfortable making public.

## Manual posts and translations

The existing Jekyll `_posts/` system still supports manual Markdown posts. To add an original post directly, name it `_posts/YYYY-MM-DD-short-slug.md` and use:

```yaml
---
layout: conversa
title: "Una pregunta"
date: 2026-11-14
categories: [converses-de-casa]
tags: [preguntes]
lang: ca
translation_key: una-pregunta-2026-11-14
permalink: /converses-de-casa/una-pregunta/
author_profile: true
comments: false
share: false
related: false
---
```

For Spanish or English translations use `lang: es` or `lang: en`, share the `translation_key`, and use language-prefixed permalinks such as `/es/converses-de-casa/una-pregunta/` and `/en/converses-de-casa/a-question/`.

The section lists only `converses-de-casa` posts in the chosen language. Existing professional site content is unaffected.
