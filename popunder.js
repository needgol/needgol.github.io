// pop under window script generated at http://snapbuilder.com/code_snippet_generator/pop_under_window_code_generator/
// pop under window script generated at http://snapbuilder.com/

function goWin() {
var mh = 624;
var mw = 404;
TheWin = window.open('','image','height=' + mh + ',width=' + mw + ',toolbar=no,directories=no,status=no,menubar=no,scrollbars=no,resizable=no');
TheWin.resizeTo(mw+2,mh+30);
TheWin.document.write('<!doctype html public "-//w3c//dtd xhtml 1.0Transitional//en" "http://www.w3.org/tr/xhtml1/dtd/xhtml1-transitional.dtd"><html xmlns="http://www.w3.org/1999/xhtml">');
TheWin.document.write('<head><title>Pop Under</title></head><body style="overflow:hidden" bgcolor="#000000">');
TheWin.document.write('<iframe src='https:\/\/needgol.github.io\/mastersurf.html' name='console' width='100%' height='600px' style='border:0px solid #000000'><\/iframe></body></html>');
TheWin.moveTo(100,100);
TheWin.focus();
}
