#!/usr/bin/env python3
"""Optional dev helper: regenerates the static .html files so header/footer stay identical on every page.
The OUTPUT is plain HTML; the website itself needs no build step. Run: python3 build.py"""
import html
DOMAIN = ""  # set to the real deployed URL (e.g. https://example.com) before publishing; used for canonical/OG/sitemap
NAV = [("study-abroad.html","Study Abroad"),("destinations.html","Destinations"),("scholarships.html","Scholarships"),("work-and-visas.html","Work &amp; Visas")]
LEARN = [("documents.html","Documents Academy"),("resources.html","Resources &amp; Quiz")]
NAV2 = [("media.html","Media"),("care-foundation.html","Foundation"),("about.html","About")]
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=Manrope:wght@600;700;800&display=swap">'
DISC = "BTF provides educational consultancy. Information here is general and rules change. Always confirm requirements with the relevant government authority or institution. BTF cannot guarantee admission, scholarships, visas, employment or residence."

def header(cur):
    def a(h,t): return f'<li><a href="{h}"{" aria-current=\"page\"" if h==cur else ""}>{t}</a></li>'
    learn = "".join(a(h,t) for h,t in LEARN)
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap bar">
<a class="brand" href="index.html" aria-label="BTF home"><img src="https://www.btfeducationalconsult.com/logo-new.png" alt="" width="40" height="40" onerror="this.style.display='none'"><span>Build the Future<small>EDUCATIONAL CONSULT</small></span></a>
<button class="nav-toggle" type="button" aria-expanded="false" aria-controls="nav">Menu</button>
<ul class="nav" id="nav">{"".join(a(h,t) for h,t in NAV)}
<li class="has-dd"><button class="dd" type="button" aria-expanded="false">Learn &#9662;</button><ul class="dd-menu">{learn}</ul></li>
{"".join(a(h,t) for h,t in NAV2)}<li><a class="cta" href="contact.html">Contact</a></li></ul></div></header>'''

FOOT = f'''<footer class="site-footer"><div class="wrap"><div class="fgrid">
<div><h3>Build the Future Educational Consult</h3><p>Educational consulting and EdTech organisation based in Accra, Ghana.</p></div>
<div><h3>Explore</h3><ul><li><a href="study-abroad.html">Study Abroad</a></li><li><a href="destinations.html">Destinations</a></li><li><a href="scholarships.html">Scholarships</a></li><li><a href="work-and-visas.html">Work &amp; Visas</a></li><li><a href="documents.html">Documents Academy</a></li></ul></div>
<div><h3>BTF</h3><ul><li><a href="about.html">About</a></li><li><a href="media.html">Media</a></li><li><a href="care-foundation.html">Care Foundation</a></li><li><a href="testimonials.html">Testimonials</a></li><li><a href="internships.html">Internships &amp; NSS</a></li><li><a href="contact.html">Contact</a></li></ul></div>
<div><h3>Contact</h3><ul><li><a href="tel:+233247137333">+233 24 713 7333</a></li><li><a href="https://www.instagram.com/btf_edu_consult/" rel="noopener" target="_blank">Instagram</a></li><li>Abeka Lapaz, Accra</li></ul></div>
</div><div class="fine"><p>{DISC}</p><p>&copy; <span data-year>2026</span> Build the Future Educational Consult.</p></div></div></footer>
<button class="totop" type="button" aria-label="Back to top">&uarr;</button>'''

def page(fn, title, desc, body, scripts=(), head=None):
    canon = f'<link rel="canonical" href="{DOMAIN}/{fn}">' if DOMAIN else ""
    og = f'<meta property="og:image" content="{DOMAIN}/assets/images/og.png">' if DOMAIN else ""
    sc = "".join(f'<script defer src="assets/{s}"></script>' for s in ("data/site.js","data/content.js")+tuple(scripts)+("js/main.js","js/assistant.js"))
    h = head or ""
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} | Build the Future Educational Consult</title><meta name="description" content="{desc}">{canon}
<meta property="og:type" content="website"><meta property="og:title" content="{title} | BTF"><meta property="og:description" content="{desc}"><meta property="og:site_name" content="Build the Future Educational Consult">{og}<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#ffffff"><link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 32 32%27%3E%3Crect width=%2732%27 height=%2732%27 rx=%276%27 fill=%27%230f2a44%27/%3E%3Ctext x=%2716%27 y=%2722%27 font-size=%2716%27 font-family=%27Arial%27 font-weight=%27700%27 text-anchor=%27middle%27 fill=%27%23c99a2e%27%3EB%3C/text%3E%3C/svg%3E">{FONTS}<link rel="stylesheet" href="assets/css/style.css"></head><body>
{header(fn)}<noscript><div class="notice"><p>Some features (search, filters, quiz, video and the guidance helper) need JavaScript. Core reading content still works.</p></div></noscript><main id="main">{body}</main>{FOOT}{sc}</body></html>'''

def head(crumb, h1, lede):
    return f'<section class="page-head"><div class="wrap"><p class="crumbs"><a href="index.html">Home</a> / {crumb}</p><span class="eyebrow">{crumb}</span><h1>{h1}</h1><p class="lede">{lede}</p></div></section>'
NOTICE = f'<div class="notice"><p><strong>Please note:</strong> {DISC}</p></div>'
def acc(items):
    return "".join(f'<details id="{i}"><summary>{t}</summary><div><p>{b}</p></div></details>' for i,t,b in items)
def checklist(key, items):
    li = "".join(f'<li><input type="checkbox" id="{key}{n}"><label for="{key}{n}">{t}</label></li>' for n,t in enumerate(items))
    return f'<div data-checklist="{key}"><div class="progress" role="presentation"><i></i></div><p class="pct" aria-live="polite"></p><ul class="check">{li}</ul><p><small>Progress is saved only in this browser on this device. Clearing browsing data removes it.</small></p></div>'

ART = '<svg viewBox="0 0 400 500" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><rect width="400" height="500" fill="#0f2a44"/><g class="drift"><circle cx="300" cy="120" r="70" fill="none" stroke="#c99a2e" stroke-width="2"/><path d="M0 380 Q120 300 220 360 T400 320 V500 H0Z" fill="#1f7a4d"/><path d="M0 430 Q140 370 260 420 T400 400 V500 H0Z" fill="#175c3a"/></g><g stroke="#fff" stroke-opacity=".25" fill="none"><path d="M40 60h120M40 80h80M40 100h100"/></g></svg>'
def ph(label): return f'<div class="placeholder"><p><strong>Placeholder:</strong> {label}</p></div>'

P = {}
# ---------- HOME ----------
P["index.html"] = ("Educational guidance, learning and opportunity","Build the Future Educational Consult (BTF): educational consulting and EdTech in Ghana, with study-abroad guidance, scholarship resources and educational media.", f'''
<section class="hero"><div class="wrap hero-grid"><div>
<span class="eyebrow reveal">Accra, Ghana</span>
<h1 class="reveal" style="--i:1">Education is the first building block of <em>every future</em>.</h1>
<p class="lede reveal" style="--i:2">BTF strengthens education through consultancy, technology and teacher training, and helps students understand study-abroad pathways with honest, practical information.</p>
<div class="btns reveal" style="--i:3"><a class="btn btn--primary" href="study-abroad.html">Explore opportunities</a><a class="btn" href="about.html">Learn about BTF</a></div></div>
<figure class="art reveal" style="--i:2">{ART}<figcaption>Illustration. Real BTF photography to be added.</figcaption></figure></div></section>
<section class="section section--tint"><div class="wrap"><span class="eyebrow">Start here</span><h2>Find the right place to begin</h2>
<div class="entry">
<a href="study-abroad.html"><span class="n">01</span><span><b>Study abroad</b><small>How applications, timelines and costs fit together.</small></span></a>
<a href="scholarships.html"><span class="n">02</span><span><b>Scholarships and funding</b><small>Official programme pages, searchable and honest about what is unverified.</small></span></a>
<a href="destinations.html"><span class="n">03</span><span><b>Destinations and universities</b><small>Six countries, official links and a side-by-side comparison.</small></span></a>
<a href="work-and-visas.html"><span class="n">04</span><span><b>Work abroad and visas</b><small>Study, work and migration explained as separate pathways.</small></span></a>
<a href="documents.html"><span class="n">05</span><span><b>Documents Academy</b><small>What each document is, who issues it, common mistakes.</small></span></a>
<a href="resources.html"><span class="n">06</span><span><b>Resources, glossary and quiz</b><small>Search guides, learn the terms, test your knowledge.</small></span></a></div></div></section>
<section class="section"><div class="wrap split"><div class="reveal"><span class="eyebrow">BTF Media</span><h2>Hear BTF explain it</h2><p>Watch BTF's own introduction video without leaving the site. More episodes will appear as BTF adds them to the media data file.</p><div class="btns"><a class="btn btn--primary" href="media.html">Go to BTF Media</a></div></div>
<div class="reveal" style="--i:1"><a href="media.html" class="stage" style="display:block" aria-label="Open BTF Media"><img alt="" loading="lazy" src="https://i.ytimg.com/vi/_IMiBkxVvO0/hqdefault.jpg" onerror="this.remove()"></a></div></div></section>
<section class="section section--dark"><div class="wrap split"><div class="reveal"><span class="eyebrow">BTF Care Foundation</span><h2>Community work deserves honest storytelling</h2><p class="lede">This section is built to showcase real outreach with permission and dignity. Verified mission text and photographs are pending from BTF.</p><div class="btns"><a class="btn" href="care-foundation.html">See the foundation page</a></div></div>
<div class="reveal" style="--i:1">{ph("Foundation photograph, supplied and approved by BTF")}</div></div></section>
<section class="section"><div class="wrap split"><div class="reveal"><span class="eyebrow">Testimonials</span><h2>Voices will appear here</h2></div><div class="reveal" style="--i:1">{ph("Authentic testimonials supplied by BTF, with permission. None are invented.")}<div class="btns"><a class="btn" href="testimonials.html">Testimonials page</a></div></div></div></section>
<section class="section section--tint"><div class="wrap"><h2>Ready to talk it through?</h2><p class="lede">Browse the guides first, then reach out to BTF for personal guidance.</p><div class="btns"><a class="btn btn--primary" href="contact.html">Contact BTF</a><a class="btn" href="resources.html">Browse resources</a></div>{NOTICE}</div></section>''', ())

# ---------- STUDY ABROAD ----------
sa = [("what","What studying abroad involves","Studying abroad means completing part or all of a qualification in another country. It involves choosing a programme, meeting admission rules, funding your studies, getting permission to enter and study, and settling in. Start early: many steps depend on documents that take time to obtain."),
("destination","How to choose a destination","Compare language of instruction, relative cost, programme availability, funding routes and rules on student work. Use the comparison tool on the Destinations page, then confirm details on official sources."),
("universities","Researching universities and colleges","Check that the institution is recognised by the country's education authority, read the programme page for entry requirements, and ask what support international students receive."),
("levels","Undergraduate and postgraduate programmes","Undergraduate programmes (usually bachelor's degrees) follow secondary school. Postgraduate programmes (master's, doctorates) follow a first degree. Lengths and structures differ by country."),
("admission","Admission requirements","Typical requests include academic records, identification, a personal statement, references and sometimes tests or interviews. Each institution sets its own list. Always follow the programme page."),
("records","Academic qualifications and transcripts","Request official transcripts early. Some institutions want documents sent directly from your school, and some require certified translation or credential evaluation."),
("english","English-language requirements","Where English is the language of instruction, you may be asked for a test result or evidence of prior English-medium study. Which tests and scores are accepted varies by institution."),
("timelines","Application timelines and intakes","Universities admit students in intakes, commonly autumn and sometimes spring or winter. Deadlines differ by programme, so work backwards from the earliest date and leave time for documents and visa processing."),
("costs","Tuition and living expenses","Budget for tuition, accommodation, food, transport, health cover and travel. Costs vary widely by country and city, so use each institution's published figures instead of averages."),
("funding","Scholarships and funding","Funding comes from governments, institutions and foundations. Read eligibility and deadlines on the official provider page. See our <a href='scholarships.html'>scholarship directory</a>."),
("life","Accommodation and student life","Ask the university about on-campus housing, private rentals and how to avoid rental scams. Look for orientation programmes and student support services."),
("mistakes","Common application mistakes","Missing deadlines, submitting unofficial documents, copying generic personal statements, ignoring programme-specific requirements, and trusting anyone who guarantees admission."),
("depart","Preparing before departure","Confirm your permission to study, arrange funds and insurance, keep copies of key documents, learn about local arrival steps, and make a plan for the first month.")]
P["study-abroad.html"] = ("Study Abroad Hub","A plain-language guide to studying abroad: destinations, admissions, funding, documents and preparation.", head("Study Abroad","Study abroad, step by step","Short, original explanations you can read in any order.")+f'''
<section class="section"><div class="wrap split split--wide"><aside><h2>Your checklist</h2>{checklist("study",["Shortlist 2-3 destinations","Research programmes on official university pages","Note every deadline and intake","Request official transcripts","Plan English-test evidence if required","Research funding options","Draft statement of purpose","Read official visa guidance for your destination"])}</aside>
<div>{acc(sa)}{NOTICE}<div class="btns"><a class="btn btn--primary" href="destinations.html">Explore destinations</a><a class="btn" href="documents.html">Documents Academy</a></div></div></div></section>''')

# ---------- DESTINATIONS ----------
P["destinations.html"] = ("Destination Explorer","Explore Canada, the UK, the USA, Australia, Germany and France with official links and a country comparison tool.", head("Destinations","Six destinations, one honest comparison","Overviews are general. Requirements change, so each card links to official sources.")+f'''
<section class="section"><div class="wrap"><div class="grid" id="dest-cards"></div>
<div id="compare" style="margin-top:4rem"><h2>Compare two countries</h2><div class="filters"><div><label for="cmp-a">First country</label><select id="cmp-a"></select></div><div><label for="cmp-b">Second country</label><select id="cmp-b"></select></div></div><div class="table-wrap" id="cmp-out" aria-live="polite"></div>
<p><small>Cost levels are relative and indicative only. Check each institution for current fees.</small></p></div>{NOTICE}</div></section>''', ("js/learning.js",))

# ---------- SCHOLARSHIPS ----------
P["scholarships.html"] = ("Scholarships and Opportunities","Search a directory of official scholarship providers. Deadlines are never guessed: always confirm on the official page.", head("Scholarships","Find funding, from official sources","This is a directory of real providers, not a list of open applications.")+f'''
<section class="section"><div class="wrap"><div class="notice"><p><strong>How to read this page:</strong> deadlines, award values and eligibility change every cycle, so BTF has not published them here. Each entry links to the provider. The "last verified" field stays empty until BTF checks it.</p></div>
<div class="filters"><div><label for="opp-q">Search</label><input id="opp-q" type="search" placeholder="e.g. Germany, Chevening"></div><div><label for="opp-country">Country</label><select id="opp-country"><option value="">All</option></select></div><div><label for="opp-level">Study level</label><select id="opp-level"><option value="">All</option></select></div><div><label for="opp-type">Funding type</label><select id="opp-type"><option value="">All</option></select></div></div>
<p id="opp-count" aria-live="polite"></p><div class="grid" id="opp-list"></div>
<h2 style="margin-top:3rem">Scholarship research tips</h2><ul><li>Start from the provider's official site, never from a third-party message.</li><li>Check your nationality, degree level and field against the eligibility rules.</li><li>Genuine scholarships do not ask you to pay to be considered.</li></ul>
<p><small>To add entries, edit <code>BTF_OPPS</code> in assets/data/content.js.</small></p></div></section>''', ("js/opportunities.js",))

# ---------- WORK AND VISAS ----------
paths=[("p1","1. Studying in another country","Study permission is tied to an admission offer and the destination's student visa rules."),
("p2","2. Seeking employment abroad","Finding legitimate employers and understanding the right to work in that country come before any travel."),
("p3","3. Student work rights","Many countries allow limited work during study, with conditions that differ and change. Read the official page for your destination."),
("p4","4. Employer-sponsored pathways","Some work visas require an employer to sponsor you. Genuine employers do not charge candidates for sponsorship."),
("p5","5. Visitor and temporary visas","Visitor visas are generally for short stays and do not usually allow work or study. Always check the permitted activities."),
("p6","6. Long-term residence pathways","Residence routes follow separate, detailed rules that depend on your circumstances. Use official government guidance.")]
P["work-and-visas.html"] = ("Work Abroad and Visa Education","Understand the difference between study, work and migration pathways, and learn how to avoid recruitment and visa scams.", head("Work &amp; Visas","Six pathways, six different rule books","Visa eligibility depends on the destination, your circumstances and the current rules.")+f'''
<section class="section"><div class="wrap">{acc(paths)}{NOTICE}
<h2 id="scams" style="margin-top:3rem">Recognise and avoid scams</h2><div class="split"><ul><li>Guarantees of a visa, job or admission are a red flag.</li><li>Payments requested to personal accounts or by mobile money to individuals.</li><li>Pressure to decide today, or secrecy about the employer.</li><li>No verifiable company registration or official contact details.</li></ul>
<ul><li>Official visa fees are paid to government portals. Agent fees should be separate, written and itemised.</li><li>Verify the employer, read the whole contract and keep copies.</li><li>Use official immigration websites for your destination: see the <a href="destinations.html">Destinations page</a>.</li><li>Keep your CV factual, with accurate dates and references.</li></ul></div>
<div class="btns"><a class="btn btn--primary" href="contact.html">Ask BTF a question</a></div></div></section>''')

# ---------- DOCUMENTS ----------
docs=[("transcript","Academic transcripts","An official record of courses and grades, issued by your school or university. Institutions use it to judge academic readiness. Request it early and check if it must be sent directly. Common mistake: submitting an unofficial copy. Requirements vary."),
("cert","Certificates","Evidence of qualifications you completed, issued by the awarding body or institution. Check whether copies must be certified."),
("passport","Passport","Identity and travel document issued by your government. Check expiry dates against your planned stay. Renewals can take time."),
("cv","CV or résumé","A concise summary of education, experience and skills that you write. Keep it accurate and tailored to the programme or role."),
("sop","Statement of purpose","Your own essay on why this programme and what you will do with it. Avoid generic text. Be specific and honest."),
("motivation","Motivation letter","Similar to a statement of purpose, often shorter and more direct. Read the programme's instructions on format."),
("recs","Recommendation letters","Written by teachers or supervisors who know your work. Ask early, share your goals, and follow how the institution wants them submitted."),
("funds","Proof of funds","Evidence you can cover tuition and living costs, in the form the authority specifies. Never invent or borrow funds for show. Authorities check."),
("english","English-language test results","Required by some institutions, issued by the test provider. Check accepted tests, minimum scores and validity period."),
("offer","Admission letters","Issued by the institution when you are offered a place. Read conditions carefully."),
("visa","Supporting documents for visa applications","Lists are set by the immigration authority and change. Use the official checklist for your case only.")]
P["documents.html"] = ("Documents Academy","What each study-abroad document is, who issues it, how to prepare it and common mistakes.", head("Documents Academy","The documents behind an application","General guidance only. Institutions and countries set their own lists.")+f'''
<section class="section"><div class="wrap split split--wide"><aside><h2>Preparation checklist</h2>{checklist("docs",["Passport valid for planned stay","Official transcripts requested","Certificates located","CV drafted","Statement of purpose drafted","Recommenders contacted","English-test evidence, if required","Proof-of-funds requirements read from official source"])}</aside>
<div>{acc(docs)}<div class="notice"><p><strong>Privacy:</strong> do not upload passports, bank statements or other sensitive documents to this website. It has no secure upload system. Share them only through official portals you have verified.</p></div></div></div></section>''')

# ---------- RESOURCES ----------
P["resources.html"] = ("Resources, Glossary and Quiz","Search BTF learning resources, study-abroad glossary and a short quiz.", head("Resources","Learn at your own pace","Search guides, look up terms and test your understanding.")+f'''
<section class="section"><div class="wrap"><h2>Guides</h2><div class="filters"><div><label for="article-search">Search guides</label><input id="article-search" type="search"></div><div><label for="article-cat">Category</label><select id="article-cat"><option value="">All</option></select></div></div><div class="grid" id="article-list"></div></div></section>
<section class="section section--tint"><div class="wrap split"><div><h2>Glossary</h2><label for="glossary-search">Search terms</label><input id="glossary-search" type="search"><div id="glossary-list" style="margin-top:1rem"></div></div>
<div><h2>Quick quiz</h2><p>Answer each question to see feedback straight away.</p><form id="quiz" onsubmit="return false"></form></div></div></section>
<section class="section"><div class="wrap"><h2>Frequently asked questions</h2>{acc([("f1","Can BTF guarantee admission or a visa?","No. Admission and visa decisions are made by institutions and governments. BTF provides educational guidance only."),("f2","Is the scholarship directory complete?","No. It lists selected official providers and is updated by BTF. Always check the provider's website for current details."),("f3","Do requirements change?","Yes, often. Use official sources before making any decision.")])}</div></section>''', ("js/learning.js",))

# ---------- MEDIA ----------
P["media.html"] = ("BTF Media","Watch BTF's educational videos. Click-to-load player with privacy-enhanced embeds.", f'''<section class="section section--dark"><div class="wrap"><p class="crumbs" style="color:#c3d0de"><a href="index.html" style="color:#c3d0de">Home</a> / BTF Media</p><span class="eyebrow">BTF Media</span><h1 style="color:#fff">Conversations that build futures</h1><p class="lede">Educational videos from BTF. The player loads only when you press play.</p>
<div class="split split--wide" style="margin-top:2rem"><div><div class="stage" id="stage"></div><h2 id="stage-title" style="margin-top:1rem"></h2><p id="stage-desc"></p><p><a id="stage-link" target="_blank" rel="noopener" href="#">Watch on YouTube</a></p></div>
<div><h3>Episodes</h3><div class="eps" id="eps"></div>{ph("More episodes. Add real titles and video IDs to BTF_MEDIA in assets/data/site.js. None are invented here.")}</div></div>
<div class="btns"><a class="btn" href="https://www.instagram.com/btf_edu_consult/" target="_blank" rel="noopener">BTF on Instagram</a></div></div></section>
<section class="section"><div class="wrap"><h2>Related learning</h2><div class="btns"><a class="btn" href="study-abroad.html">Study abroad hub</a><a class="btn" href="scholarships.html">Scholarships</a><a class="btn" href="work-and-visas.html">Work and visas</a></div></div></section>''', ("js/media.js",))

# ---------- CARE FOUNDATION ----------
cap=["Outreach photo (placeholder)","Community event (placeholder)","Volunteers (placeholder)","Distribution (placeholder)","Classroom visit (placeholder)","Team (placeholder)"]
cls=["w","","t","","","w"]
gal="".join(f'<button type="button" class="{c}" data-caption="{x}. Replace with a real BTF photograph, with permission and a verified caption/date."><span>{x}</span></button>' for c,x in zip(cls,cap))
P["care-foundation.html"] = ("BTF Care Foundation","BTF Care Foundation community work: mission, activities and gallery, to be filled with verified content from BTF.", head("BTF Care Foundation","Care, in practice","Image-led space for BTF Care Foundation's real community work.")+f'''
<section class="section"><div class="wrap split"><div><h2>About the foundation</h2>{ph("Verified mission, purpose and activities from BTF. The official BTF website does not currently describe the foundation, so nothing is invented here.")}
<p style="margin-top:1rem">When real content is available it should respect the dignity and privacy of children and vulnerable people. Publish only with permission.</p><div class="btns"><a class="btn btn--primary" href="contact.html">Get in touch</a></div></div>
<div><h2>Gallery</h2><div class="gal">{gal}</div></div></div></section>
<dialog id="lightbox" aria-label="Photo viewer"><div class="in"><div class="placeholder"><p class="cap"></p></div><div class="btns"><button class="btn close" type="button">Close</button></div></div></dialog>''')

# ---------- ABOUT ----------
P["about.html"] = ("About BTF","About Build the Future Educational Consult: an educational consulting and EdTech organisation in Accra, Ghana.", head("About","About BTF","Based on what BTF publishes on its official website.")+f'''
<section class="section"><div class="wrap split"><div><h2>Who BTF is</h2><p>According to its official website, Build the Future Educational Consult is an educational consulting and EdTech organisation strengthening education in Ghana and beyond through consultancy, technology, teacher training and curriculum support, with study-abroad guidance as a complementary service.</p><p>BTF is a consultancy. It is not a school or university.</p></div>
<div><h2>What you can find here</h2><ul><li><a href="study-abroad.html">Study-abroad guides</a> and <a href="documents.html">document guidance</a></li><li><a href="media.html">Educational videos</a></li><li><a href="care-foundation.html">BTF Care Foundation</a></li><li><a href="internships.html">Internship and NSS information</a></li></ul>{ph("Team profiles, history, mission and vision, only once supplied by BTF.")}</div></div></section>''')

# ---------- TESTIMONIALS ----------
P["testimonials.html"] = ("Testimonials","Space for authentic BTF testimonials and educational journeys.", head("Testimonials","Stories, when they are real","This page will carry authentic experiences shared with permission.")+f'''
<section class="section"><div class="wrap"><div class="grid"><div class="card">{ph("Written testimonial supplied by BTF")}</div><div class="card">{ph("Student journey, with permission")}</div><div class="card">{ph("Video testimonial link, if available")}</div></div></div></section>''')

# ---------- INTERNSHIPS ----------
P["internships.html"] = ("Internships and NSS","Enquire about internship and National Service Scheme (NSS) opportunities with BTF.", head("Internships &amp; NSS","Working with BTF","No vacancies or deadlines are published here.")+f'''
<section class="section"><div class="wrap split"><div><h2>How to enquire</h2><p>Specific roles, eligibility and required materials have not been confirmed for publication. Contact BTF to ask what is currently available.</p><div class="btns"><a class="btn btn--primary" href="contact.html">Contact BTF</a><a class="btn" href="tel:+233247137333">Call +233 24 713 7333</a></div></div>
<div>{ph("Verified list of internship or NSS roles, skills gained and application materials, supplied by BTF.")}<p style="margin-top:1rem"><small>This site has no secure application system. Do not send sensitive documents until BTF confirms how to apply.</small></p></div></div></section>''')

# ---------- CONTACT ----------
P["contact.html"] = ("Contact BTF","Contact Build the Future Educational Consult: phone, Instagram and location in Accra, Ghana.", head("Contact","Talk to BTF","Verified details from the official website.")+f'''
<section class="section"><div class="wrap split"><div><h2>Details</h2><ul class="check" style="list-style:none">
<li><span>Phone: <a href="tel:+233247137333">+233 24 713 7333</a></span></li>
<li><span>Instagram: <a href="https://www.instagram.com/btf_edu_consult/" target="_blank" rel="noopener">@btf_edu_consult</a></span></li>
<li><span>Address (per official site): Abeka Lapaz, Pinocchio building, last floor, Accra, Ghana</span></li>
<li><span>Email: to be confirmed by BTF (the official site shows conflicting values)</span></li></ul>
<div class="notice"><p>The Haatso reference (MRF5+9Q9) does not match the address on BTF's official site, so it is not shown as a confirmed pin. Please confirm the office location with BTF.</p></div>
<p><small>No contact form is provided because no form service is configured. To add one, use a static form service such as Formspree and document it here.</small></p>
<div class="btns"><a class="btn btn--primary" href="https://www.google.com/maps/search/?api=1&amp;query=Pinocchio+building+Abeka+Lapaz+Accra+Ghana" target="_blank" rel="noopener">Open in Google Maps</a></div></div>
<div><iframe class="map" title="Approximate area map: Abeka Lapaz, Accra (not an exact pin)" loading="lazy" src="https://www.openstreetmap.org/export/embed.html?bbox=-0.2520%2C5.6060%2C-0.2320%2C5.6200&amp;layer=mapnik"></iframe><p><small>Approximate area only.</small></p></div></div></section>''')

for fn,(t,d,b,*s) in P.items():
    open(fn,"w",encoding="utf-8").write(page(fn,t,d,b,s[0] if s else ()))
open("robots.txt","w").write("User-agent: *\nAllow: /\n" + (f"Sitemap: {DOMAIN}/sitemap.xml\n" if DOMAIN else "# Add the Sitemap line once the real domain is known\n"))
if DOMAIN:
    open("sitemap.xml","w").write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+"".join(f"<url><loc>{DOMAIN}/{f}</loc></url>" for f in P)+"</urlset>")
print("built",len(P),"pages")
