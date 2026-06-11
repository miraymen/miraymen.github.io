# miraymen.github.io

Source for my personal academic homepage, built with Jekyll and served by GitHub Pages: [miraymen.github.io](https://miraymen.github.io)

Feel free to borrow the code.

## Structure

All content you would edit lives in `_content/` (`_config.yml` points Jekyll's `includes_dir` and `data_dir` there, and force-includes the homepage via `include:` + a `permalink: /`):

```
.
├── _config.yml               # identity, links, avatar/favicon, analytics
├── _content/
│   ├── index.md              # news, services, teaching, talks
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

Adding a paper = adding one entry to `_content/publications.yml`; nothing else to touch.

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
