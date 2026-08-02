# krz.sh

Source for [krz.sh](https://krz.sh) — the krazy warez website. Built with
[Zola](https://www.getzola.org/).

## Develop

```sh
zola serve
```

Then open http://127.0.0.1:1111.

## Build

```sh
zola build
```

Output is written to `public/`.

## Structure

- `config.toml` — site configuration
- `content/` — pages (home, `services/`, `apps/`, `about/`)
- `templates/` — Tera templates
- `sass/main.scss` — styles (compiled to `main.css`)
- `static/` — assets, `favicon.svg`, and `CNAME`

## Deploy

Pushing to `main` builds and publishes to GitHub Pages via
`.github/workflows/deploy.yml`. The custom domain is set in `static/CNAME`.
