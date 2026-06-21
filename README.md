# Nova Blogger Pro

A clean, professional Blogger theme rebuilt from scratch as a single XML template. It is designed to be uploaded directly in **Blogger → Theme → Restore / Upload**.

## What is included

- `theme.xml` — the main Blogger template file.
- `.github/workflows/build-blogger-template.yml` — manual workflow that validates the XML and exports a ready-to-upload artifact.

## Features

- Mobile-first responsive layout.
- Sticky glass header with Blogger PageList menu support.
- Blogger Blog widget support for posts, pages, labels, archive, comments and search pages.
- Sidebar sections for HTML, Popular Posts, Labels and Blog Archive widgets.
- Footer widget zones for About, links and profile widgets.
- Homepage hero, search box, reading progress bar, dark mode toggle and back-to-top button.
- Clean SEO basics through Blogger head content, canonical URL, title and description tags.
- Print-friendly article styling and polished typography.

## Upload to Blogger

1. Open Blogger.
2. Go to **Theme**.
3. Click the arrow/dropdown next to **Customize**.
4. Choose **Restore** or **Upload**.
5. Upload `theme.xml` or the workflow artifact XML from `dist/`.

## Manual GitHub Action build

Open **Actions → Build Blogger Template → Run workflow**.

Inputs:

- `output_name`: output XML name, default `nova-blogger-pro`.
- `minify`: removes extra blank lines while keeping Blogger XML safe.

The workflow checks that the template contains Blogger XML namespaces, a skin block, layout sections and a Blog widget. Then it uploads a Blogger-ready XML artifact.

## Customization

Use Blogger Layout to add or reorder widgets in these sections:

- Header menu
- Hero ad / feature slot
- Main posts
- Sidebar
- Footer columns

For deeper styling, edit the CSS inside the `<b:skin><![CDATA[ ... ]]></b:skin>` block in `theme.xml`.
