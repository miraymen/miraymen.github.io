# miraymen.github.io

Source for my personal academic homepage, built with Jekyll and served by GitHub Pages: [miraymen.github.io](https://miraymen.github.io)

## Structure

```
.
├── _config.yml          # site configuration (name, links, avatar, analytics)
├── index.md             # homepage content (bio, news, talks)
├── _data/
│   └── publications.yml # publication entries rendered on the homepage
├── _includes/           # publications, services, and teaching sections
├── _layouts/
│   └── homepage.html    # the page template
├── _sass/               # styles (light + dark mode)
└── assets/              # images, videos, CSS, BibTeX files, CV
```

## Local preview

```bash
bundle install
bundle exec jekyll serve
```

Then open http://localhost:4000.
