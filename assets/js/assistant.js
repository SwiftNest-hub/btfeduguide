/* assistant.js: RULE-BASED guidance helper (no AI model, no network calls). Extend the TREE object to add topics.
   Each node: say (text), links [[label,url]], next [node ids shown as buttons]. */
(function(){
  var TREE={
   start:{say:"Hello. I can point you to the right part of this site. What are you looking for?",next:["study","funding","work","docs","media","contact"]},
   study:{say:"Which level are you thinking about?",next:["ug","pg"]},
   ug:{say:"For undergraduate study, start with how to choose a destination and what admissions usually ask for.",links:[["Study abroad hub","study-abroad.html"],["Compare destinations","destinations.html#compare"]],next:["funding","docs","start"]},
   pg:{say:"For postgraduate study, funding and your statement of purpose matter early. Research programme-specific rules on each university's site.",links:[["Study abroad hub","study-abroad.html"],["Scholarship directory","scholarships.html"],["Documents Academy","documents.html"]],next:["start"]},
   funding:{say:"Funding rules differ by provider. Our directory links only to official pages and never lists unverified deadlines.",links:[["Scholarships and funding","scholarships.html"]],next:["docs","start"]},
   work:{say:"Studying, working and migrating are different pathways with different rules. Nobody can guarantee a visa or a job, so verify everything with official authorities.",links:[["Work and visa education","work-and-visas.html"],["Spot scams","work-and-visas.html#scams"]],next:["start"]},
   docs:{say:"Our Documents Academy explains common documents and has checklists that save to your browser. Please do not upload sensitive documents to this site.",links:[["Documents Academy","documents.html"]],next:["start"]},
   media:{say:"BTF shares educational videos. You can watch them without leaving this site.",links:[["BTF Media","media.html"]],next:["start"]},
   contact:{say:"For personal guidance, contact BTF directly. I cannot give legal or immigration advice.",links:[["Contact BTF","contact.html"]],next:["start"]}
  };
  var LABEL={study:"Study abroad",ug:"Undergraduate",pg:"Postgraduate",funding:"Scholarships",work:"Working abroad",docs:"Documents",media:"Watch videos",contact:"Contact BTF",start:"Start over"};
  var fab=document.createElement("button");fab.className="a-fab";fab.type="button";fab.setAttribute("aria-expanded","false");fab.setAttribute("aria-controls","a-panel");fab.textContent="Guidance helper";
  var p=document.createElement("div");p.className="a-panel";p.id="a-panel";p.setAttribute("role","dialog");p.setAttribute("aria-label","Guidance helper");
  p.innerHTML='<div class="a-head"><span>Guidance helper</span><button type="button" aria-label="Close helper">&times;</button></div><div class="a-log" aria-live="polite"></div><div class="a-opts"></div><p class="a-note">Rule-based guide, not a live AI. It cannot promise admissions, scholarships, visas or jobs.</p>';
  document.body.appendChild(fab);document.body.appendChild(p);
  var log=p.querySelector(".a-log"),opts=p.querySelector(".a-opts"),started=false;
  function add(t,me,links){var d=document.createElement("div");d.className="a-msg"+(me?" me":"");d.textContent=t;
    (links||[]).forEach(function(l){var a=document.createElement("a");a.href=l[1];a.textContent=l[0];d.appendChild(a)});log.appendChild(d);log.scrollTop=log.scrollHeight}
  function go(id,user){var n=TREE[id];if(user)add(LABEL[id],true);add(n.say,false,n.links);opts.innerHTML="";
    n.next.forEach(function(k){var b=document.createElement("button");b.type="button";b.textContent=LABEL[k];b.addEventListener("click",function(){go(k,true)});opts.appendChild(b)})}
  function setOpen(o){p.classList.toggle("open",o);fab.setAttribute("aria-expanded",o);if(o&&!started){started=true;go("start")}if(o)opts.querySelector("button")&&opts.querySelector("button").focus()}
  fab.addEventListener("click",function(){setOpen(!p.classList.contains("open"))});
  p.querySelector(".a-head button").addEventListener("click",function(){setOpen(false);fab.focus()});
  document.addEventListener("keydown",function(e){if(e.key==="Escape"&&p.classList.contains("open")){setOpen(false);fab.focus()}});
})();
