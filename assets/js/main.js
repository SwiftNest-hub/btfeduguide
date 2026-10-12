/* main.js: navigation, reveal-on-scroll, scroll-to-top, checklists, gallery lightbox. Loaded on every page. */
document.documentElement.classList.add("js");
(function(){
  // --- Mobile menu + dropdown ---
  var toggle=document.querySelector(".nav-toggle"), nav=document.getElementById("nav");
  if(toggle&&nav){
    toggle.addEventListener("click",function(){
      var open=nav.classList.toggle("open"); toggle.setAttribute("aria-expanded",open);
      toggle.textContent=open?"Close":"Menu"; document.body.classList.toggle("nav-open",open);
    });
  }
  function closeMenu(){if(nav&&nav.classList.contains("open")){nav.classList.remove("open");toggle.setAttribute("aria-expanded","false");toggle.textContent="Menu";document.body.classList.remove("nav-open")}}
  if(nav)nav.addEventListener("click",function(e){if(e.target.closest("a"))closeMenu()});
  window.addEventListener("resize",function(){if(window.innerWidth>1060)closeMenu()});
  document.querySelectorAll("[data-year]").forEach(function(y){y.textContent=new Date().getFullYear()});
  document.querySelectorAll(".has-dd > button").forEach(function(b){
    b.addEventListener("click",function(e){
      e.stopPropagation(); var li=b.parentNode, o=li.classList.toggle("open"); b.setAttribute("aria-expanded",o);
    });
  });
  document.addEventListener("click",function(){document.querySelectorAll(".has-dd.open").forEach(function(li){li.classList.remove("open");li.firstElementChild.setAttribute("aria-expanded","false")})});
  document.addEventListener("keydown",function(e){
    if(e.key!=="Escape")return;
    if(nav&&nav.classList.contains("open")){toggle.click();toggle.focus()}
    document.querySelectorAll(".has-dd.open").forEach(function(li){li.classList.remove("open")});
  });
  // --- Reveal on scroll ---
  var rev=[].slice.call(document.querySelectorAll(".reveal"));
  if("IntersectionObserver" in window){
    var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add("in");io.unobserve(e.target)}})},{threshold:.12});
    rev.forEach(function(el){io.observe(el)});
  } else rev.forEach(function(el){el.classList.add("in")});
  // --- Scroll to top ---
  var up=document.querySelector(".totop");
  if(up){window.addEventListener("scroll",function(){up.classList.toggle("show",window.scrollY>700)},{passive:true});
    up.addEventListener("click",function(){window.scrollTo({top:0})})}
  // --- Checklists (progress saved in this browser only, via localStorage) ---
  document.querySelectorAll("[data-checklist]").forEach(function(box){
    var key="btf:"+box.getAttribute("data-checklist"), saved={};
    try{saved=JSON.parse(localStorage.getItem(key)||"{}")}catch(e){}
    var inputs=box.querySelectorAll("input[type=checkbox]"), bar=box.querySelector(".progress i"), txt=box.querySelector(".pct");
    function paint(){var n=0;inputs.forEach(function(i){if(i.checked)n++});var p=Math.round(n/inputs.length*100);
      if(bar)bar.style.width=p+"%"; if(txt)txt.textContent=n+" of "+inputs.length+" done"}
    inputs.forEach(function(i,k){i.checked=!!saved[k];
      i.addEventListener("change",function(){saved[k]=i.checked;try{localStorage.setItem(key,JSON.stringify(saved))}catch(e){};paint()})});
    paint();
  });
  // --- Gallery lightbox (native <dialog>: Esc closes, focus is trapped by the browser) ---
  var dlg=document.getElementById("lightbox");
  if(dlg){
    document.querySelectorAll(".gal button").forEach(function(b){
      b.addEventListener("click",function(){
        dlg.querySelector(".cap").textContent=b.getAttribute("data-caption")||"";
        if(dlg.showModal)dlg.showModal(); else dlg.setAttribute("open","");
        dlg.querySelector(".close").focus();
      });
    });
    dlg.querySelector(".close").addEventListener("click",function(){dlg.close()});
    dlg.addEventListener("click",function(e){if(e.target===dlg)dlg.close()});
  }
})();
