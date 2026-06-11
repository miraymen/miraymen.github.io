# miraymen.github.io

Source for my personal academic homepage, built with Jekyll and served by GitHub Pages: [miraymen.github.io](https://miraymen.github.io)

Feel free to borrow the code.

## Structure

All content you would edit regularly lives in `index.md` and `_content/` (`_config.yml` points Jekyll's `includes_dir` and `data_dir` there):

```
.
├── _config.yml               # identity, links, avatar/favicon, analytics
├── index.md                  # news, services, teaching, talks (must stay at the root)
├── _content/
│   ├── intro.html            # bio, rendered next to the photo in the header
│   ├── publications.yml      # one entry per paper (title, authors, links, bibtex, teaser)
│   └── publications.md       # template that renders the publication list
├── _layouts/
│   └── homepage.html         # the single page layout (head, header, theme toggle, footer)
├── _sass/
│   ├── main.scss             # site styles, light + dark mode
│   └── publications.scss     # publication list styles
└── assets/
    ├── css/style.scss        # imports _sass/* → served as the site's single stylesheet
    ├── files/                # CV
    └── img/                  # photo, favicon, paper teasers (H.264 MP4 / images, 1.9:1)
```

## Where is what — how to edit what

| To change…                                   | Edit…                                      |
| -------------------------------------------- | ------------------------------------------ |
| Bio (the text next to the photo)             | `_content/intro.html`                      |
| Publications (add / edit / reorder papers)   | `_content/publications.yml`                |
| News, Services, Teaching, Talks              | `index.md`                                 |
| Name, email, social links, CV path, GA4 id   | `_config.yml`                              |
| Profile photo, favicon, paper teasers        | `assets/img/`                              |
| CV file                                      | `assets/files/mir_resume.pdf`              |
| Colors, fonts, spacing                       | `_sass/main.scss`, `_sass/publications.scss` |
| Page skeleton (header, footer, meta tags)    | `_layouts/homepage.html`                   |
| How each publication entry is rendered       | `_content/publications.md`                 |

### Adding a paper

Append an entry to `_content/publications.yml` — nothing else to touch:

```yaml
- title: Name of the Paper
  authors: <strong>Aymen Mir</strong>, <a href="https://example.com">Coauthor Name</a>
  conference: IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2027
  pdf: https://arxiv.org/abs/XXXX.XXXXX     # PDF button
  page: https://example.com/project          # Project Page button; the title links here (falls back to pdf)
  code: https://github.com/user/repo         # Code button (optional)
  image: ./assets/img/teaser.mp4             # teaser; .mp4 autoplays muted, .jpg/.png also fine
  notes: Best Paper Finalist                 # optional gold award badge
  bibtex: |
    @inproceedings{key,
      title = {...},
      author = {...},
    }
```

Leave `conference:` empty for unpublished work. Teasers display in a 1.9:1 box (270 px wide on desktop), so source images/videos near that ratio look best; videos should be H.264 MP4 without audio.

### Styling gotcha: dark mode

The site has a three-state theme (system / forced light / forced dark via the toggle). Every dark-mode color rule must exist in **two** forms, or the toggle and the system preference fall out of sync:

```css
@media (prefers-color-scheme: dark) { html:not([data-theme="light"]) SELECTOR { ... } }
html[data-theme="dark"] SELECTOR { ... }
```

### Deploying

Push to `main` — GitHub Pages builds in about a minute. Pages and CSS are CDN-cached for ~10 minutes, so hard-refresh (or use a private window) when checking a change. The served commit is embedded in `<meta name="build-revision">`.

## Features

- Light/dark mode: follows the system by default, with a manual toggle (top right) persisted in `localStorage`
- Inline BibTeX with copy button, click-to-copy email, autoplaying MP4 teasers
- No JS frameworks, one stylesheet, no build tooling beyond Jekyll

## Local preview

Requires a recent Ruby (3.x).

```bash
bundle install
bundle exec jekyll serve
```

Then open http://localhost:4000.
