// pop under window script generated at http://snapbuilder.com/code_snippet_generator/pop_under_window_code_generator/
// pop under window script generated at http://snapbuilder.com/

function goWin() {
var mh = 624;
var mw = 624;
TheWin = window.open('','image','height=' + mh + ',width=' + mw + ',toolbar=no,directories=no,status=no,menubar=no,scrollbars=no,resizable=no');
TheWin.resizeTo(mw+2,mh+30);
TheWin.document.write('<!doctype html public "-//w3c//dtd xhtml 1.0Transitional//en" "http://www.w3.org/tr/xhtml1/dtd/xhtml1-transitional.dtd"><html xmlns="http://www.w3.org/1999/xhtml">');
TheWin.document.write('<head><title>Pop Under</title></head><body style="overflow:hidden" bgcolor="#000000">');
TheWin.document.write('<html>
<head><title>Master surf<\/title>
<script>
window.onbeforeunload = function() {
return "Forbidden to redirect force";
}
<\/script>
<style type="text\/css">
body {
   margin:0;
}
<\/style>
<style type="text\/css">
 .page{
  position: relative; width:100%; height:100%; overflow:hidden;
 }
 .page iframe {
 position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
 }
 <\/style>
<\/head>
<body>
<script language="JavaScript">
  function popupWin() {
  text += "<html>\n<head>\n<title>New windows<\/title>\n<body>\n";
  text += "<center>\n<br>";
  text += "<img src='https:\/\/needgol.github.io\/gifs-de-raio_needgol.gif'>";
  text += "<\/center>\n<\/body>\n<\/html>\n";
  setTimeout('windowProp(text)', 3000);  \/\/
  }
  function windowProp(text) {
  newWindow = window.open('https:\/\/needgol.github.io\/mastersurf.html','newWin','width=800,height=700');
  newWindow.document.write(text);
  setTimeout('closeWin(newWindow)', 30000); \/\/
  }
  function closeWin(newWindow) {
  newWindow.close();
  }
  
  window.onload = popupWin();
  
  <\/script>
<div class="page">
        <iframe src="https:\/\/needgol.github.io\/" frameborder="0" allowfullscreen><\/iframe>
 <\/div>
   <\/br>
<\/body>
<\/html><div align="center"><a href="#" onclick="self.close();return false;">Close Window</a></div></body></html>');
TheWin.moveTo(100,100);
TheWin.focus();
}
