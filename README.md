# Issa Bakari Portfolio

Responsive multilingual portfolio: [live website](https://isbakari447.github.io/portfolio/).

The French, English and Swedish pages and downloadable CVs present the same background:

- IT-Högskolan: Full stack webbutveckling med inriktning JavaScript, August 2026 - June 2028 (ongoing).
- Jensen Komvux: IT training, October 2025 - July 2026 (completed).
- ICA Nära Enebytorg: January 2020 - present, part-time alongside studies.
- Upplands-Bro, Stockholm region, Sweden; 070-736 45 55; bakarii447@gmail.com.
- EnterpriseERP JavaScript platform under development, distinct from the earlier C# project.

## Local preview

```sh
python -m http.server 8080
```

Open http://localhost:8080. No build step is required.

## Files and maintenance

- `index.html`: page structure and content. Keep default HTML and all translations aligned.
- `style.css`: page styles.
- `script.js`: FR / EN / SV translations and language switching.
- `screenshots/`: project screenshots linked from the projects section.
- `diplomes/`: supporting diplomas and certificates.
- `profile-photo.png`: the supplied portrait, used unchanged.
- `issa-bakari-cv-{fr,en,sv}.pdf`: one-page CVs with the same teal sidebar design and portrait.
- `cv-issa-bakari.pdf`: compatibility alias for the French CV.
- `generate-cv-pdfs.py`: reproducible PDF generator; requires `reportlab`, `pypdf` and `pypdfium2`. On Windows it uses the installed Arial fonts.

After changing facts, update all language dictionaries in `script.js` and the generator, regenerate the PDFs and review the rendered PNGs in `tmp/pdfs/` before publishing. The main CV buttons follow the selected language. Local storage is optional.

GitHub Pages deploys from `main` at the repository root. Original design retained; profile information aligned with the updated CV in October 2026.
