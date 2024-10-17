  function popupWin() {
  text +=  "<html>\n<head>\n<title>Win</title>\n<body>\n";
  text += "<center>
\n<br>";
  text += "<img src='https://needgol.github.io/gifs-de-raio_needgol.gif'>";
  text += "</center>
\n</body>\n</html>\n";
  setTimeout('windowProp(text)', 3000);  // time up
  }
  function windowProp(text) {
  newWindow = window.open('https://needgol.github.io/page','newWin','width=600,height=600');
  newWindow.document.write(text);
  setTimeout('closeWin(newWindow)', 30000); // time up to exit
  }
  function closeWin(newWindow) {
  newWindow.close();
  }
  
  window.onload = popupWin();
