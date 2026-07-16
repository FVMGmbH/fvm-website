#!/usr/bin/env python3
"""Generate legal subpages for FVM website."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def shell(title: str, description: str, body: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="de" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} – FVM GmbH</title>
<meta name="description" content="{description}">
<link rel="icon" type="image/png" href="assets/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/legal.css">
</head>
<body>
<div class="page-bg"></div>
<div class="page-grid"></div>
<header id="hdr">
  <div class="container nav">
    <a href="index.html" class="logo"><img src="assets/fvm-logo.png" alt="FVM GmbH" width="324" height="48"></a>
    <div class="nav-actions">
      <a href="index.html" class="back-home">← Zur Startseite</a>
      <button class="theme-toggle" onclick="toggleTheme()" aria-label="Farbmodus wechseln">
        <svg class="moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>
        <svg class="sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>
      </button>
    </div>
  </div>
</header>
<main class="legal-main">
  <div class="container">
    <article class="legal-card">
{body}
    </article>
  </div>
</main>
<footer>
  <div class="container">
    <div class="foot-grid">
      <div>
        <a href="index.html" class="logo"><img src="assets/fvm-logo.png" alt="FVM GmbH" width="297" height="44"></a>
        <p>Ihr unabhängiger Versicherungsmakler in Rockenhausen.</p>
      </div>
      <nav class="legal-links" aria-label="Rechtliches">
        <a href="impressum.html">Impressum</a>
        <a href="erstinformation.html">Erstinformation</a>
        <a href="datenschutz.html">Datenschutz</a>
        <a href="eu-transparenzverordnung.html">EU-Transparenzverordnung</a>
      </nav>
    </div>
    <div class="foot-bottom">
      <span>© 2026 FVM GmbH</span>
      <span><a href="impressum.html">Impressum</a> · <a href="datenschutz.html">Datenschutz</a></span>
    </div>
  </div>
</footer>
<script src="assets/site.js"></script>
</body>
</html>
"""


CONTACT_BLOCK = """
<div class="contact-block">
<p><strong>FVM GmbH</strong></p>
<p>E-Mail: <a href="mailto:kunden@fvm-makler.de">kunden@fvm-makler.de</a></p>
<p>Adresse: Am Pfingstborn 21, 67806 Rockenhausen</p>
<p>Öffnungszeiten: Montag–Freitag 09:00–13:00 Uhr</p>
<p>Kundenservice: <a href="tel:063617744">06361 7744</a></p>
</div>
"""

IMPRESSUM = f"""
<h1>Impressum</h1>
<h2>Kontaktdaten</h2>
{CONTACT_BLOCK}
<h2>Tätigkeitsart und erteilte Erlaubnis</h2>
<p>Eingetragen im Vermittlerregister bei der Industrie- und Handelskammer Pfalz Versicherungsmakler mit Erlaubnis nach § 34d Abs. 1 GewO.</p>
<p>Registernummer D-EX3H-G2EX9-70</p>
<p>Aufsichtsbehörde und zuständige Behörde für die Erlaubnis:<br>
Industrie- und Handelskammer für die Pfalz, Rheinallee 18–20, 67061 Ludwigshafen<br>
Telefon 0621/5904-0 · <a href="https://www.ihk.de/pfalz" target="_blank" rel="noopener">www.ihk.de/pfalz</a></p>
<h2>Gemeinsame Registerstelle</h2>
<p>Deutscher Industrie- und Handelskammertag (DIHK)<br>
Breite Straße 29, 10178 Berlin<br>
Telefon: 0180 600 58 50 (Festnetzpreis 0,20 €/Anruf; Mobilfunkpreise maximal 0,60 €/Anruf)<br>
<a href="https://www.vermittlerregister.info" target="_blank" rel="noopener">www.vermittlerregister.info</a></p>
<h2>Berufsrechtliche Regelungen</h2>
<p>Wir unterliegen folgenden berufsrechtlichen Regelungen:</p>
<ul><li>Versicherungsmakler mit Erlaubnis nach § 34d Abs. 1 GewO</li></ul>
<p>Die berufsrechtlichen Regelungen können Sie im Internet unter <a href="https://www.gesetze-im-internet.de" target="_blank" rel="noopener">www.gesetze-im-internet.de</a> einsehen und abrufen.</p>
<h2>Beratung und Vergütung</h2>
<p>Wir bieten im Zuge der Vermittlung eine Beratung gemäß den gesetzlichen Vorgaben an und erhalten für die erfolgreiche Vermittlung eines Versicherungsvertrages eine Provision vom Produktanbieter. Diese Provision ist vom Kunden nicht separat an uns zu bezahlen, sondern bereits in der Versicherungsprämie enthalten. Sofern eine abweichende Regelung gewünscht wird oder von der Sache her geboten ist, wird unsere Dienstleistung durch Zahlung eines Honorars bzw. einer Aufwandsentschädigung abgegolten – gänzlich oder in Kombination mit der zuvor genannten Provision. Die Höhe des Honorars wird im Vorfeld zwischen Kunde und Berater schriftlich vereinbart. Weitere Vergütungen erhalten wir im Zusammenhang mit der Beratung und Vermittlung nicht.</p>
<h2>Beteiligungen</h2>
<p>Wir halten keine Beteiligungen an Stimmrechten oder dem Kapital von Versicherungsunternehmen. Es gibt keine Beteiligungen von Versicherungsunternehmen an den Stimmrechten oder dem Kapital unseres Unternehmens.</p>
<h2>Nachhaltigkeitsbezogene Offenlegung zum Vertrieb von Versicherungsanlageprodukten</h2>
<p>Wir verfolgen eine eigenständige Nachhaltigkeitsstrategie. Im Rahmen der Auswahl von Versicherungsgesellschaften und Versicherungsprodukten berücksichtigen wir die von den Versicherern zur Verfügung gestellten Informationen. Versicherer, die erkennbar keine Strategie zur Einbeziehung von Nachhaltigkeitsrisiken in ihre Investitionsentscheidungen einbeziehen, beziehen wir je nach Kundenwunsch nicht in unsere Empfehlungen ein. Im Rahmen der im Kundeninteresse erfolgenden individuellen Beratung stellen wir gesondert dar, wenn die Berücksichtigung der Nachhaltigkeitsrisiken bei der Investmententscheidung einen für uns erkennbaren Vor- bzw. Nachteil für den individuellen Kunden bedeutet.</p>
<h2>Schlichtungsstellen</h2>
<p><strong>Versicherungsombudsmann e.V.</strong><br>
Postfach 08 06 32 · Tel.: 0800 3696000 · Fax: 0800 3699000<br>
<a href="https://www.versicherungsombudsmann.de" target="_blank" rel="noopener">www.versicherungsombudsmann.de</a></p>
<p><strong>Ombudsmann für die Private Kranken- und Pflegeversicherung</strong><br>
Postfach 06 02 22, 10052 Berlin · Tel.: 0800 2550444 · Fax: 030 20458931<br>
<a href="https://www.pkv-ombudsmann.de" target="_blank" rel="noopener">www.pkv-ombudsmann.de</a></p>
<p>Online-Streitbeteiligung via EU: <a href="https://webgate.ec.europa.eu/odr" target="_blank" rel="noopener">https://webgate.ec.europa.eu/odr</a></p>
<h2>Beschwerdemanagement</h2>
<p>Bei Beschwerden über unsere Tätigkeit wenden Sie sich gerne an die oben genannten Kontaktdaten.</p>
<h2>Inhaltlich verantwortlich</h2>
<p>Andy Klag<br>Am Pfingstborn 21<br>67806 Rockenhausen</p>
<h2>Haftung und Inhalte</h2>
<p>Verpflichtungen zur Entfernung oder Sperrung der Nutzung von Informationen nach den allgemeinen Gesetzen bleiben hiervon unberührt. Eine diesbezügliche Haftung ist jedoch erst ab dem Zeitpunkt der Kenntnis einer konkreten Rechtsverletzung möglich. Bei Bekanntwerden von entsprechenden Rechtsverletzungen werden wir diese Inhalte umgehend entfernen.</p>
<h2>Berufshaftpflichtversicherung</h2>
<p>Besteht bei der Allianz Versicherung.</p>
<h2>Haftung und Links</h2>
<p>Unser Angebot enthält Links zu externen Websites Dritter, auf deren Inhalte wir keinen Einfluss haben. Deshalb können wir für diese fremden Inhalte auch keine Gewähr übernehmen. Für die Inhalte der verlinkten Seiten ist stets der jeweilige Anbieter oder Betreiber der Seiten verantwortlich. Die verlinkten Seiten wurden zum Zeitpunkt der Verlinkung auf mögliche Rechtsverstöße überprüft. Rechtswidrige Inhalte waren zum Zeitpunkt der Verlinkung nicht erkennbar.</p>
<p>Eine permanente inhaltliche Kontrolle der verlinkten Seiten ist jedoch ohne konkrete Anhaltspunkte einer Rechtsverletzung nicht zumutbar. Bei Bekanntwerden von Rechtsverletzungen werden wir derartige Links umgehend entfernen.</p>
<h2>Urheberrecht</h2>
<p>Die durch die Seitenbetreiber erstellten Inhalte und Werke auf diesen Seiten unterliegen dem deutschen Urheberrecht. Die Vervielfältigung, Bearbeitung, Verbreitung und jede Art der Verwertung außerhalb der Grenzen des Urheberrechtes bedürfen der schriftlichen Zustimmung des jeweiligen Autors bzw. Erstellers. Downloads und Kopien dieser Seite sind nur für den privaten, nicht kommerziellen Gebrauch gestattet.</p>
<p>Soweit die Inhalte auf dieser Website nicht vom Betreiber erstellt wurden, werden die Urheberrechte Dritter beachtet. Sollten Sie trotzdem auf eine Urheberrechtsverletzung aufmerksam werden, bitten wir um einen entsprechenden Hinweis. Bei Bekanntwerden von Rechtsverletzungen werden wir derartige Inhalte umgehend entfernen.</p>
"""

ERSTINFORMATION = f"""
<h1>Erstinformation</h1>
<h2>Name, Anschrift und Kontaktdaten</h2>
{CONTACT_BLOCK}
<h2>Tätigkeitsart und erteilte Erlaubnis</h2>
<p>Eingetragen im Vermittlerregister bei der Industrie- und Handelskammer Pfalz Versicherungsmakler mit Erlaubnis nach § 34d Abs. 1 GewO.</p>
<p>Registernummer D-EX3H-G2EX9-70</p>
<p>Aufsichtsbehörde: Industrie- und Handelskammer für die Pfalz, Rheinallee 18–20, 67061 Ludwigshafen · Tel. 0621/5904-0 · <a href="https://www.ihk.de/pfalz" target="_blank" rel="noopener">www.ihk.de/pfalz</a></p>
<h2>Gemeinsame Registerstelle</h2>
<p>Deutsche Industrie- und Handelskammer (DIHK), Breite Straße 29, 10178 Berlin · Tel. 0180 600 58 50 · <a href="https://www.vermittlerregister.info" target="_blank" rel="noopener">www.vermittlerregister.info</a></p>
<h2>Berufsrechtliche Regelungen</h2>
<ul><li>Versicherungsmakler mit Erlaubnis nach § 34d Abs. 1 GewO</li></ul>
<p>Die berufsrechtlichen Regelungen können Sie unter <a href="https://www.gesetze-im-internet.de" target="_blank" rel="noopener">www.gesetze-im-internet.de</a> einsehen.</p>
<h2>Beratung und Vergütung</h2>
<p>Wir bieten im Zuge der Vermittlung eine Beratung gemäß den gesetzlichen Vorgaben an und erhalten für die erfolgreiche Vermittlung eines Versicherungsvertrages eine Provision vom Produktanbieter. Diese Provision ist vom Kunden nicht separat an uns zu bezahlen, sondern bereits in der Versicherungsprämie enthalten. Sofern eine abweichende Regelung gewünscht wird oder von der Sache her geboten ist, wird unsere Dienstleistung durch Zahlung eines Honorars bzw. einer Aufwandsentschädigung abgegolten. Weitere Vergütungen erhalten wir im Zusammenhang mit der Beratung und Vermittlung nicht.</p>
<h2>Beteiligungen</h2>
<p>Wir halten keine Beteiligungen an Stimmrechten oder dem Kapital von Versicherungsunternehmen. Es gibt keine Beteiligungen von Versicherungsunternehmen an den Stimmrechten oder dem Kapital unseres Unternehmens.</p>
<h2>Nachhaltigkeitsbezogene Offenlegung</h2>
<p>Wir verfolgen eine eigenständige Nachhaltigkeitsstrategie und berücksichtigen bei der Produktauswahl die von Versicherern bereitgestellten Informationen zu Nachhaltigkeitsrisiken.</p>
<h2>Schlichtungsstellen</h2>
<p>Versicherungsombudsmann e.V. · Tel. 0800 3696000 · <a href="https://www.versicherungsombudsmann.de" target="_blank" rel="noopener">www.versicherungsombudsmann.de</a></p>
<p>Ombudsmann Private Kranken- und Pflegeversicherung · Tel. 0800 2550444 · <a href="https://www.pkv-ombudsmann.de" target="_blank" rel="noopener">www.pkv-ombudsmann.de</a></p>
<p>EU-Streitschlichtung: <a href="https://webgate.ec.europa.eu/odr" target="_blank" rel="noopener">https://webgate.ec.europa.eu/odr</a></p>
<h2>Beschwerdemanagement</h2>
<p>Bei Beschwerden wenden Sie sich an die oben genannten Kontaktdaten.</p>
<h2>Berufshaftpflichtversicherung</h2>
<p>Besteht bei der Allianz Versicherung.</p>
"""

EU_TRANSPARENZ = """
<h1>EU-Transparenzverordnung</h1>
<h2>Wie berücksichtigen wir Nachhaltigkeitsrisiken in unserer Beratung?</h2>
<p>Bei der Zusammenstellung der für unsere Kunden auswählbaren Produkte berücksichtigen wir neben der Sicherheits- und Ertragsorientierung der Produkte auch Nachhaltigkeitsrisiken (Umwelt, Soziales und Unternehmensführung). Wir stellen im Rahmen unserer Kundenberatung sicher, dass der individuelle Kundenbedarf hinsichtlich Risikoneigung, Risikotragfähigkeit, Renditeerwartungen und individuellen Nachhaltigkeitspräferenzen in die individuelle Produktauswahl einfließt. Dabei können Nachhaltigkeitsrisiken bewusst eingegangen werden, wenn dies dem Kundenbedarf entspricht.</p>
<h2>Inwieweit steht unsere Vergütungspolitik mit der Berücksichtigung von Nachhaltigkeitsrisiken in Einklang?</h2>
<p>Wir stellen im Rahmen unserer Vergütungspolitik sicher, dass im bestmöglichen Interesse unserer Kundinnen und Kunden gehandelt wird. Insbesondere werden durch die Vergütung keine Anreize gesetzt, ein Versicherungsanlage- oder Altersvorsorgeprodukt zu empfehlen, das den Bedürfnissen der Kundinnen und Kunden weniger entspricht. Die von uns gezahlte Vergütung ist neutral in Bezug auf die Einbeziehung von Nachhaltigkeitsrisiken.</p>
<h2>Auf welche Art und Weise beziehen wir Nachhaltigkeitsrisiken in die Versicherungsberatung mit ein?</h2>
<p>Bei der Zusammenstellung der für unsere Kunden auswählbaren Produkte berücksichtigen unsere Vertriebspartner neben der Sicherheits- und Ertragsorientierung der Produkte auch Nachhaltigkeitsrisiken. Diese stellen im Rahmen ihrer Kundenberatung sicher, dass der individuelle Kundenbedarf hinsichtlich Risikoneigung, Risikotragfähigkeit, Renditeerwartungen und individuellen Nachhaltigkeitspräferenzen in die individuelle Produktauswahl einfließt.</p>
"""

DATENSCHUTZ = f"""
<h1>Datenschutz</h1>
<h2>Datenschutz auf einen Blick</h2>
<h3>Allgemeine Hinweise</h3>
<p>Die folgenden Hinweise geben einen einfachen Überblick darüber, was mit Ihren personenbezogenen Daten passiert, wenn Sie diese Website besuchen. Personenbezogene Daten sind alle Daten, mit denen Sie persönlich identifiziert werden können.</p>
<h3>Datenerfassung auf dieser Website</h3>
<p><strong>Wer ist verantwortlich?</strong> Die Datenverarbeitung auf dieser Website erfolgt durch den Websitebetreiber. Kontaktdaten finden Sie im Abschnitt „Verantwortliche Stelle“.</p>
<p><strong>Wie erfassen wir Ihre Daten?</strong> Ihre Daten werden zum einen dadurch erhoben, dass Sie uns diese mitteilen (z. B. per Kontaktformular, E-Mail oder Telefon). Andere Daten werden automatisch beim Besuch der Website durch unsere IT-Systeme erfasst (technische Daten wie Browser, Betriebssystem, Zeitpunkt des Aufrufs).</p>
<p><strong>Wofür nutzen wir Ihre Daten?</strong> Ein Teil der Daten wird erhoben, um eine fehlerfreie Bereitstellung der Website zu gewährleisten. Andere Daten können zur Bearbeitung Ihrer Anfrage verwendet werden.</p>
<p><strong>Welche Rechte haben Sie?</strong> Sie haben jederzeit das Recht auf unentgeltliche Auskunft, Berichtigung, Löschung, Einschränkung der Verarbeitung, Datenübertragbarkeit und Beschwerde bei einer Aufsichtsbehörde.</p>
<h2>Hosting</h2>
<p>Diese Website wird über <strong>Cloudflare Pages</strong> (Cloudflare, Inc.) gehostet. Personenbezogene Daten, die auf dieser Website erfasst werden (z. B. in Server-Logfiles), werden auf Servern von Cloudflare verarbeitet. Rechtsgrundlage ist Art. 6 Abs. 1 lit. f DSGVO (berechtigtes Interesse an einer sicheren und effizienten Bereitstellung) sowie ggf. Art. 6 Abs. 1 lit. b DSGVO.</p>
<p>Weitere Informationen: <a href="https://www.cloudflare.com/privacypolicy/" target="_blank" rel="noopener">Cloudflare Datenschutz</a></p>
<h2>Verantwortliche Stelle</h2>
{CONTACT_BLOCK}
<h2>Speicherdauer</h2>
<p>Soweit keine speziellere Speicherdauer genannt wurde, verbleiben Ihre personenbezogenen Daten bei uns, bis der Zweck der Verarbeitung entfällt oder Sie Löschung verlangen, sofern keine gesetzlichen Aufbewahrungspflichten entgegenstehen.</p>
<h2>Widerruf und Widerspruch</h2>
<p>Sie können eine erteilte Einwilligung jederzeit widerrufen. Sie haben das Recht, aus Gründen Ihrer besonderen Situation Widerspruch gegen die Verarbeitung einzulegen (Art. 21 DSGVO), soweit die Verarbeitung auf Art. 6 Abs. 1 lit. e oder f DSGVO beruht.</p>
<h2>Beschwerderecht</h2>
<p>Sie haben das Recht, sich bei einer Datenschutz-Aufsichtsbehörde zu beschweren.</p>
<h2>SSL-/TLS-Verschlüsselung</h2>
<p>Diese Seite nutzt aus Sicherheitsgründen eine SSL- bzw. TLS-Verschlüsselung. Eine verschlüsselte Verbindung erkennen Sie am Schloss-Symbol und „https://“ in der Adresszeile.</p>
<h2>Datenerfassung auf dieser Website</h2>
<h3>Server-Log-Dateien</h3>
<p>Der Provider erhebt automatisch: Browsertyp, Betriebssystem, Referrer-URL, Hostname, Uhrzeit der Anfrage und IP-Adresse. Rechtsgrundlage: Art. 6 Abs. 1 lit. f DSGVO.</p>
<h3>Kontaktformular, E-Mail, Telefon</h3>
<p>Wenn Sie uns kontaktieren, speichern wir Ihre Angaben zur Bearbeitung der Anfrage. Rechtsgrundlage: Art. 6 Abs. 1 lit. b DSGVO (vertragliche/vorvertragliche Anfragen) oder Art. 6 Abs. 1 lit. f DSGVO (berechtigtes Interesse an der Bearbeitung von Anfragen).</p>
<h3>Local Storage (Theme-Einstellung)</h3>
<p>Wir speichern Ihre Auswahl für den Hell-/Dunkelmodus lokal im Browser (localStorage, Schlüssel „fvm-theme“). Es werden keine personenbezogenen Daten an Dritte übermittelt. Rechtsgrundlage: Art. 6 Abs. 1 lit. f DSGVO.</p>
<h2>Externe Dienste</h2>
<h3>Google Fonts</h3>
<p>Wir binden Schriftarten von Google ein. Dabei kann Google erfahren, dass Sie diese Website über Ihre IP-Adresse aufgerufen haben. Rechtsgrundlage: Art. 6 Abs. 1 lit. f DSGVO. Weitere Informationen: <a href="https://policies.google.com/privacy" target="_blank" rel="noopener">Google Datenschutz</a></p>
<h3>Externe Bilder</h3>
<p>Auf einzelnen Seiten können Bilder von externen Servern eingebunden sein. Beim Aufruf kann Ihre IP-Adresse an den jeweiligen Anbieter übermittelt werden.</p>
<h2>Widerspruch gegen Werbe-E-Mails</h2>
<p>Der Nutzung von im Rahmen der Impressumspflicht veröffentlichten Kontaktdaten zur Übersendung von nicht ausdrücklich angeforderter Werbung wird widersprochen.</p>
<p><em>Quelle: Inhalte übernommen und angepasst von der bisherigen Website <a href="https://fvm-versicherung.de/datenschutz/">fvm-versicherung.de</a> (Stand Website-Relaunch 2026).</em></p>
"""

PAGES = [
    ("impressum.html", "Impressum", "Impressum der FVM GmbH – Versicherungsmakler Rockenhausen.", IMPRESSUM),
    ("erstinformation.html", "Erstinformation", "Erstinformation gemäß § 15 VersVermV – FVM GmbH.", ERSTINFORMATION),
    ("datenschutz.html", "Datenschutz", "Datenschutzerklärung der FVM GmbH.", DATENSCHUTZ),
    ("eu-transparenzverordnung.html", "EU-Transparenzverordnung", "EU-Transparenzverordnung – FVM GmbH.", EU_TRANSPARENZ),
]

for filename, page_title, desc, content in PAGES:
    path = ROOT / filename
    path.write_text(shell(page_title, desc, content), encoding="utf-8")
    print(f"Wrote {filename}")
