# FVM GmbH – Website

Öffentliche Marketing-Website für [FVM GmbH](https://fvm-versicherung.de) (Versicherungsmakler, Rockenhausen).

## Struktur

- `index.html` – Single-Page-Website (statisch)

## Cloudflare Pages

1. **Workers & Pages** → **Create** → **Pages** → **Connect to Git**
2. Repository `fvm-website` auswählen
3. Build-Einstellungen:
   - **Framework preset:** None
   - **Build command:** *(leer)*
   - **Build output directory:** `/`
4. **Save and Deploy**
5. Unter **Custom domains** → `fvm-versicherung.de` hinzufügen
6. Erst nach Test: Nameserver bei Strato auf Cloudflare umstellen

## Lokal testen

Die Datei `index.html` im Browser öffnen oder:

```bash
npx --yes serve .
```
