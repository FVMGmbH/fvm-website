# FVM GmbH – Website

Öffentliche Marketing-Website für [FVM GmbH](https://fvm-versicherung.de) (Versicherungsmakler, Rockenhausen).

## Struktur

- `index.html` – Single-Page-Website (statisch)
- `assets/ordner-service.mp4` – Ordner-Service Promo (40s, 16:9, Untertitel + Off-Stimme)
- `scripts/build-ordner-video.py` – Video aus Story-Stills neu rendern
- `scripts/add-ordner-voiceover.py` – Deutsche Off-Stimme (edge-tts) aufs Video legen

```bash
python scripts/build-ordner-video.py
python scripts/add-ordner-voiceover.py
```

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
