const query = window.location.search;
const urlParams = new URLSearchParams(query);
const search_text = urlParams.get('search');
links = document.querySelectorAll('ul#Sort-Links a');
console.log(links);
for(link of links)
{
    link.href = link.href + '&serch=' + search_text
};