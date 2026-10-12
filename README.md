# BTF website (static HTML/CSS/vanilla JS)
Open index.html in a browser, or deploy the folder to GitHub Pages / Vercel (no build step needed).

## Where things live
- assets/css/style.css: design tokens (top of file) and all styles
- assets/js/*.js: main (nav, reveal, checklists, lightbox), assistant, learning, opportunities, media
- assets/data/site.js: contact facts and video list. assets/data/content.js: destinations, scholarships, glossary, quiz, articles
- build.py: optional; regenerates the HTML pages so header/footer stay identical. Edit it, run `python3 build.py`.

## Still needed from BTF
- Confirmed email, YouTube channel URL, office location (official site says Abeka Lapaz; Haatso reference unresolved)
- Foundation mission and real photos, testimonials, internship/NSS details, team and history
- Real domain: set DOMAIN in build.py (enables canonical, og:image, sitemap) and add assets/images/og.png
- A contact form needs a service such as Formspree; none is configured

## Not tested
Not opened in a real browser or Lighthouse. Test at 360, 390, 768, 1024, 1440px before launch.
