//a fresh start
//do something about the heights I meant
var r = document.getElementById('lol');
r.innerHTML = screen.height;//r.offsetHeight; //this gets the dimensions of an element





function loadDoc()
{

var form  = document.forms['f1'];
var formData = new FormData(form);
var str = form.word.value;


var xhttp = new XMLHttpRequest();

xhttp.onreadystatechange = function()
{
if (xhttp.readyState == 4 && xhttp.status == 200)
{
document.getElementById("heading").innerHTML = xhttp.responseText;
}
};

//xhttp.open("GET","../wsgi/app.py?q="+str,true);
//xhttp.send();
xhttp.open("POST","http://localhost:8080",true);
xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
xhttp.send(formData); //can not get it to work with forms yet
}