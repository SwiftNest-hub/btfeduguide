/* opportunities.js: search + filters over BTF_OPPS (assets/data/content.js). */
(function(){
  var list=document.getElementById("opp-list"); if(!list||!window.BTF_OPPS)return;
  var f={q:document.getElementById("opp-q"),country:document.getElementById("opp-country"),level:document.getElementById("opp-level"),type:document.getElementById("opp-type")};
  function uniq(k){var r=[];BTF_OPPS.forEach(function(o){if(r.indexOf(o[k])<0)r.push(o[k])});return r.sort()}
  [["country","country"],["level","level"],["type","type"]].forEach(function(p){uniq(p[1]).forEach(function(v){var o=document.createElement("option");o.value=v;o.textContent=v;f[p[0]].appendChild(o)})});
  function esc(s){return String(s).replace(/[&<>"]/g,function(c){return({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"})[c]})}
  function run(){
    var q=f.q.value.toLowerCase(),n=0;list.innerHTML="";
    BTF_OPPS.forEach(function(o){
      if((f.country.value&&o.country!==f.country.value)||(f.level.value&&o.level!==f.level.value)||(f.type.value&&o.type!==f.type.value))return;
      if((o.name+" "+o.provider+" "+o.country).toLowerCase().indexOf(q)<0)return;
      n++;var a=document.createElement("article");a.className="card";
      a.innerHTML='<span class="tag">'+esc(o.country)+'</span><span class="tag tag--gold">'+esc(o.level)+'</span><h3>'+esc(o.name)+'</h3><p>'+esc(o.provider)+' &middot; '+esc(o.type)+'</p><p><strong>Funding:</strong> '+esc(o.cover)+'<br><strong>Eligibility:</strong> '+esc(o.elig)+'<br><strong>Deadline:</strong> '+esc(o.deadline)+'<br><strong>Last verified by BTF:</strong> '+(o.lastVerified?esc(o.lastVerified):'not yet verified')+'</p><p><a href="'+o.link+'" target="_blank" rel="noopener">Official page (opens in new tab)</a></p>';
      list.appendChild(a)});
    document.getElementById("opp-count").textContent=n+" result"+(n===1?"":"s");
    if(!n){var p=document.createElement("p");p.textContent="Nothing matches those filters.";list.appendChild(p)}
  }
  Object.keys(f).forEach(function(k){f[k].addEventListener("input",run)});run();
})();
