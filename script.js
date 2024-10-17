var popunder="http://needgol.github.io/page-exemplo.html/"
function loadpopunder(){
win2=window.open(popunder[Math.floor(Math.random()*(popunder.length))])
win2.blur()
window.focus()
}
