/* learning.js: glossary search, article filter, quiz, destination cards + comparison. Needs content.js. */
(function(){
  function el(t,c,h){var e=document.createElement(t);if(c)e.className=c;if(h!==undefined)e.innerHTML=h;return e}
  function esc(s){return String(s).replace(/[&<>"]/g,function(c){return({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"})[c]})}
  // Glossary
  var g=document.getElementById("glossary-list"), gs=document.getElementById("glossary-search");
  if(g&&window.BTF_GLOSSARY){
    var draw=function(q){g.innerHTML="";var n=0;BTF_GLOSSARY.forEach(function(x){
      if((x[0]+" "+x[1]).toLowerCase().indexOf(q)>-1){n++;g.appendChild(el("div","",'<details><summary>'+esc(x[0])+'</summary><div><p>'+esc(x[1])+'</p></div></details>'))}});
      if(!n)g.appendChild(el("p","","No matching terms."))};
    draw(""); gs.addEventListener("input",function(){draw(gs.value.trim().toLowerCase())});
  }
  // Articles
  var al=document.getElementById("article-list");
  if(al&&window.BTF_ARTICLES){
    var as=document.getElementById("article-search"), ac=document.getElementById("article-cat");
    var cats=[];BTF_ARTICLES.forEach(function(a){if(cats.indexOf(a.cat)<0)cats.push(a.cat)});
    cats.forEach(function(c){var o=el("option","",esc(c));o.value=c;ac.appendChild(o)});
    var run=function(){al.innerHTML="";var q=as.value.toLowerCase(),c=ac.value,n=0;
      BTF_ARTICLES.forEach(function(a){if((!c||a.cat===c)&&(a.t+" "+a.d).toLowerCase().indexOf(q)>-1){n++;
        al.appendChild(el("article","card",'<span class="tag">'+esc(a.cat)+'</span><h3><a href="'+a.u+'">'+esc(a.t)+'</a></h3><p>'+esc(a.d)+'</p>'))}});
      if(!n)al.appendChild(el("p","","No resources match."))};
    run();as.addEventListener("input",run);ac.addEventListener("change",run);
  }
  // Quiz
  var qz=document.getElementById("quiz");
  if(qz&&window.BTF_QUIZ){
    BTF_QUIZ.forEach(function(x,i){
      var f=el("fieldset","quiz-q",'<legend>'+(i+1)+'. '+esc(x.q)+'</legend>');
      x.o.forEach(function(o,j){var l=el("label","",'<input type="radio" name="q'+i+'" value="'+j+'"> <span>'+esc(o)+'</span>');f.appendChild(l)});
      var fb=el("p","fb");fb.setAttribute("aria-live","polite");f.appendChild(fb);qz.appendChild(f);
      f.addEventListener("change",function(e){var ok=+e.target.value===x.a;fb.className="fb "+(ok?"ok":"no");fb.textContent=(ok?"Correct. ":"Not quite. ")+x.why})});
  }
  // Destinations: cards + comparison
  var dl=document.getElementById("dest-cards");
  if(dl&&window.BTF_DEST){
    BTF_DEST.forEach(function(d,i){
      var links=d.official.map(function(o){return '<li><a href="'+o[1]+'" rel="noopener" target="_blank">'+esc(o[0])+'</a></li>'}).join("");
      var s=el("section","card reveal",'<h3 id="'+d.slug+'">'+esc(d.name)+'</h3><p>'+esc(d.systems)+'.</p><p><strong>Language:</strong> '+esc(d.lang)+'</p><p><strong>Funding research:</strong> '+esc(d.funding)+'.</p><p><strong>Student work:</strong> '+esc(d.work)+'.</p><p><strong>Official sources</strong></p><ul>'+links+'</ul>');
      s.style.setProperty("--i",i%3);dl.appendChild(s)});
    var a=document.getElementById("cmp-a"),b=document.getElementById("cmp-b"),out=document.getElementById("cmp-out");
    BTF_DEST.forEach(function(d,i){[a,b].forEach(function(s){var o=el("option","",esc(d.name));o.value=i;s.appendChild(o)})});b.value=1;
    var cmp=function(){var x=BTF_DEST[a.value],y=BTF_DEST[b.value];
      var rows=[["Language","lang"],["Cost level (relative)","cost"],["Funding research","funding"],["Student work","work"],["Education system","systems"]];
      out.innerHTML='<table><caption class="hidden">Country comparison</caption><thead><tr><th>Factor</th><th>'+esc(x.name)+'</th><th>'+esc(y.name)+'</th></tr></thead><tbody>'+
       rows.map(function(r){return '<tr><th scope="row">'+r[0]+'</th><td>'+esc(x[r[1]])+'</td><td>'+esc(y[r[1]])+'</td></tr>'}).join("")+'</tbody></table>'};
    a.addEventListener("change",cmp);b.addEventListener("change",cmp);cmp();
  }
})();
