/* media.js: click-to-load YouTube (privacy-enhanced domain, nothing loads until the visitor presses play). */
(function(){
  var stage=document.getElementById("stage"), eps=document.getElementById("eps"); if(!stage||!window.BTF_MEDIA)return;
  function esc(s){return String(s).replace(/[&<>"]/g,function(c){return({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"})[c]})}
  function show(m){
    stage.innerHTML='<img alt="" loading="lazy" src="https://i.ytimg.com/vi/'+m.id+'/hqdefault.jpg" onerror="this.remove()"><button class="play" type="button" aria-label="Play video: '+esc(m.title)+'"><span class="pbtn" aria-hidden="true">&#9654;</span></button>';
    stage.querySelector("button").addEventListener("click",function(){
      stage.innerHTML='<iframe src="https://www.youtube-nocookie.com/embed/'+m.id+'?autoplay=1" title="'+esc(m.title)+'" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowfullscreen loading="lazy"></iframe>'});
    document.getElementById("stage-title").textContent=m.title;document.getElementById("stage-desc").textContent=m.desc;
    document.getElementById("stage-link").href="https://www.youtube.com/watch?v="+m.id;
  }
  BTF_MEDIA.forEach(function(m){
    var d=document.createElement("div");d.className="ep";
    d.innerHTML='<div class="thumb"><img alt="" loading="lazy" src="https://i.ytimg.com/vi/'+m.id+'/mqdefault.jpg" onerror="this.remove()"></div><div><h3>'+esc(m.title)+'</h3><p>'+esc(m.topic)+'</p><button class="btn" type="button">Watch here</button></div>';
    d.querySelector("button").addEventListener("click",function(){show(m);stage.scrollIntoView({behavior:"smooth",block:"center"})});
    eps.appendChild(d)});
  show(BTF_MEDIA[0]);
})();
