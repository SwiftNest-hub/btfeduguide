/* Educational content. General guidance only; rules change. Edit this file to update the site. */
window.BTF_DEST = [
 {slug:"canada",name:"Canada",lang:"English / French",cost:"Medium to high",funding:"Mostly institutional and provincial; research funding at graduate level",work:"Rules for study-related work exist and change; check official page",systems:"Universities, colleges and polytechnics; many programmes include co-op",official:[["Study in Canada (official)","https://www.canada.ca/en/immigration-refugees-citizenship/services/study-canada.html"],["EduCanada","https://www.educanada.ca/"]]},
 {slug:"uk",name:"United Kingdom",lang:"English",cost:"High (international fees)",funding:"Chevening, Commonwealth and university scholarships",work:"Student visa conditions limit work; check official page",systems:"Universities with shorter degrees (often 3-year bachelor's, 1-year master's)",official:[["Student visa (GOV.UK)","https://www.gov.uk/student-visa"],["Chevening","https://www.chevening.org/"]]},
 {slug:"usa",name:"United States",lang:"English",cost:"High to very high",funding:"Merit and need aid at institutions; assistantships for graduates",work:"Strict limits, mainly on-campus; check official page",systems:"Community colleges, public and private universities; liberal-arts structure",official:[["Study in the States (DHS)","https://studyinthestates.dhs.gov/"],["EducationUSA","https://educationusa.state.gov/"]]},
 {slug:"australia",name:"Australia",lang:"English",cost:"Medium to high",funding:"Australia Awards and university scholarships",work:"Student work conditions apply; check official page",systems:"Universities, TAFE and vocational providers",official:[["Study Australia","https://www.studyaustralia.gov.au/"],["Home Affairs: Study","https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/student-500"]]},
 {slug:"germany",name:"Germany",lang:"German and English (varies by programme)",cost:"Lower tuition at many public universities; living costs still apply",funding:"DAAD and foundation scholarships",work:"Student work rules apply; check official page",systems:"Universities and universities of applied sciences",official:[["DAAD","https://www.daad.de/en/"],["Make it in Germany","https://www.make-it-in-germany.com/en/"]]},
 {slug:"france",name:"France",lang:"French (English-taught programmes exist)",cost:"Lower public tuition; living costs vary by city",funding:"Government and institutional scholarships",work:"Student work rules apply; check official page",systems:"Universities and grandes écoles",official:[["Campus France","https://www.campusfrance.org/en"],["France-Visas","https://france-visas.gouv.fr/en/"]]}
];
/* Directory of REAL programme providers. Deadlines, values and eligibility are intentionally NOT stated: see official page. lastVerified is null until BTF checks each link. */
window.BTF_OPPS = [
 {name:"Chevening Scholarships",country:"United Kingdom",provider:"UK Government (FCDO)",level:"Postgraduate",type:"Government-funded",cover:"See official page",elig:"Eligibility depends on your country and profile.",deadline:"See official page",link:"https://www.chevening.org/",lastVerified:null},
 {name:"Commonwealth Scholarships",country:"United Kingdom",provider:"Commonwealth Scholarship Commission",level:"Postgraduate",type:"Government-funded",cover:"See official page",elig:"Different schemes have different rules.",deadline:"See official page",link:"https://cscuk.fcdo.gov.uk/",lastVerified:null},
 {name:"DAAD Scholarships",country:"Germany",provider:"DAAD",level:"Postgraduate",type:"Government-funded",cover:"See official page",elig:"Programme-specific; use the DAAD database.",deadline:"See official page",link:"https://www.daad.de/en/study-and-research-in-germany/scholarships/",lastVerified:null},
 {name:"Australia Awards",country:"Australia",provider:"Australian Government",level:"Postgraduate",type:"Government-funded",cover:"See official page",elig:"Open to selected countries; check yours.",deadline:"See official page",link:"https://www.dfat.gov.au/people-to-people/australia-awards",lastVerified:null},
 {name:"EducationUSA advising and funding guidance",country:"United States",provider:"U.S. Department of State",level:"Undergraduate",type:"Advising / guidance",cover:"Information, not a scholarship",elig:"Open to prospective students.",deadline:"Not applicable",link:"https://educationusa.state.gov/",lastVerified:null},
 {name:"Campus France scholarship search",country:"France",provider:"Campus France",level:"Undergraduate",type:"Directory",cover:"Directory of options",elig:"Varies by programme.",deadline:"Varies",link:"https://www.campusfrance.org/en",lastVerified:null},
 {name:"EduCanada scholarship information",country:"Canada",provider:"Government of Canada",level:"Undergraduate",type:"Directory",cover:"Directory of options",elig:"Varies by programme.",deadline:"Varies",link:"https://www.educanada.ca/",lastVerified:null}
];
window.BTF_GLOSSARY = [
 ["Transcript","An official record of your courses and grades, issued by your school or university."],
 ["Statement of purpose","A written explanation of why you want a programme and how it fits your goals."],
 ["Motivation letter","Similar to a statement of purpose; common in European applications."],
 ["Intake","A period when a university admits new students, e.g. autumn or spring."],
 ["Proof of funds","Evidence that you can pay tuition and living costs, in the form the authority requires."],
 ["Conditional offer","An offer that depends on you meeting stated requirements, such as final grades."],
 ["Unconditional offer","An offer with no outstanding academic conditions."],
 ["Visa","Permission from a country's authorities to enter or stay for a stated purpose."],
 ["Accreditation","Formal recognition that an institution or programme meets quality standards."],
 ["Bachelor's / Master's","Undergraduate and postgraduate degree levels."],
 ["Tuition","The fee charged for teaching, separate from living costs."],
 ["Recruitment scam","A fake offer of jobs, admissions or visas, usually asking for payment up front."]
];
window.BTF_QUIZ = [
 {q:"A person says they can guarantee your visa if you pay today. What is the sensible response?",o:["Pay quickly so you don't lose the chance","Treat it as a warning sign and check the official immigration website","Send your passport copy as proof of interest"],a:1,why:"No one can guarantee a visa. Decisions are made by immigration authorities."},
 {q:"Where should you confirm current visa fees?",o:["On the official government immigration website","From any agent's price list","From social media comments"],a:0,why:"Official fees are published by the government. Agent fees are separate and should be itemised."},
 {q:"Which is true about admission requirements?",o:["They are identical in every country","They vary by country, institution and programme","They never change"],a:1,why:"Always read the specific programme page on the institution's website."},
 {q:"Should you upload your passport or bank statements to a general website?",o:["Yes, if it looks professional","Only to official portals or trusted channels you have verified","Always, to speed things up"],a:1,why:"Sensitive documents belong on verified official portals only."}
];
window.BTF_ARTICLES = [
 {t:"What studying abroad really involves",cat:"Study abroad",d:"From choosing a programme to arriving on campus: the big picture.",u:"study-abroad.html#what"},
 {t:"How to choose a destination",cat:"Study abroad",d:"Cost, language, programme fit and long-term goals.",u:"study-abroad.html#destination"},
 {t:"Documents you will probably need",cat:"Documents",d:"A plain-language tour of transcripts, letters and proof of funds.",u:"documents.html"},
 {t:"Spotting recruitment and visa scams",cat:"Work & visas",d:"Warning signs and safer ways to verify an offer.",u:"work-and-visas.html#scams"},
 {t:"Researching scholarships safely",cat:"Scholarships",d:"Where to look and how to read eligibility properly.",u:"scholarships.html"},
 {t:"Comparing countries",cat:"Destinations",d:"Use the comparison tool to weigh language, cost and funding.",u:"destinations.html#compare"}
];
