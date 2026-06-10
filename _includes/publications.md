<h2 id="publications">Publications</h2>

<div class="publications">
<ol class="bibliography">

{% for link in site.data.publications.main %}

<li>
<div class="pub-row">
  <div class="col-sm-3 abbr" style="position: relative;padding-right: 15px;padding-left: 15px;">
    {% if link.image contains ".mp4" %}
    <video class="teaser img-fluid z-depth-1" autoplay loop muted playsinline>
      <source src="{{ link.image }}" type="video/mp4">
    </video>
    {% elsif link.image %}
    <img src="{{ link.image }}" class="teaser img-fluid z-depth-1" style="width=100;height=40%">
    {% endif %}
  </div>
  <div class="col-sm-9" style="position: relative;padding-right: 15px;padding-left: 20px;">
      <div class="title"><a href="{% if link.page %}{{ link.page }}{% else %}{{ link.pdf }}{% endif %}">{{ link.title }}</a></div>
      <div class="author">{{ link.authors }}</div>
      <div class="periodical"><em>{{ link.conference }}</em>
      </div>
    <div class="links">
      {% if link.pdf %} 
      <a href="{{ link.pdf }}" class="btn btn-sm z-depth-0" role="button" target="_blank" style="font-size:12px;">PDF</a>
      {% endif %}
      {% if link.code %} 
      <a href="{{ link.code }}" class="btn btn-sm z-depth-0" role="button" target="_blank" style="font-size:12px;">Code</a>
      {% endif %}
      {% if link.page %} 
      <a href="{{ link.page }}" class="btn btn-sm z-depth-0" role="button" target="_blank" style="font-size:12px;">Project Page</a>
      {% endif %}
      {% if link.bibtex %} 
      <a class="btn btn-sm z-depth-0 fakelink bibtex-toggle" role="button" style="font-size:12px;">BibTeX</a>
      {% endif %}
      {% if link.notes %} 
      <span class="pub-award">{{ link.notes }}</span>
      {% endif %}
      {% if link.others %} 
      {{ link.others }}
      {% endif %}
    </div>
    {% if link.bibtex %}
    <div class="bibref-box">
      <button class="bib-copy" type="button" aria-label="Copy BibTeX" title="Copy BibTeX"><i class="far fa-copy"></i></button>
      <pre class="bibref">{{ link.bibtex }}</pre>
    </div>
    {% endif %}
  </div>
</div>
</li>

{% endfor %}

</ol>
</div>

<script>
document.addEventListener("DOMContentLoaded", function() {
  document.querySelectorAll(".bibtex-toggle").forEach(function(btn) {
    btn.addEventListener("click", function() {
      var box = btn.closest(".col-sm-9").querySelector(".bibref-box");
      if (box) box.style.display = (box.style.display === "block") ? "none" : "block";
    });
  });
  document.querySelectorAll(".bib-copy").forEach(function(btn) {
    btn.addEventListener("click", function() {
      var pre = btn.parentNode.querySelector(".bibref");
      navigator.clipboard.writeText(pre.textContent.trim()).then(function() {
        var icon = btn.querySelector("i");
        icon.className = "fas fa-check";
        setTimeout(function() { icon.className = "far fa-copy"; }, 1500);
      });
    });
  });
});
</script>

