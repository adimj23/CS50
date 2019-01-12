var modal = document.getElementById('myModal');

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal
btn.onclick = function() {
    modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

function idForm(){
  if(document.getElementById('career').checked && document.getElementById('pts').checked) {
  window.open('/career-pts.html','_self')
}else if(document.getElementById('career').checked && document.getElementById('ast').checked) {
  window.open('/career-ast.html','_self')
}
else if(document.getElementById('career').checked && document.getElementById('reb').checked) {
  window.open('/career-reb.html','_self')
}
else if(document.getElementById('season').checked && document.getElementById('pts').checked) {
  window.open('/season-pts.html','_self')
}
else if(document.getElementById('season').checked && document.getElementById('ast').checked) {
  window.open('/season-ast.html','_self')
}
else if(document.getElementById('season').checked && document.getElementById('reb').checked) {
  window.open('/season-reb.html','_self')
}
else if(document.getElementById('alltime').checked) {
  window.open('alltime.html','_self')
}
else {
  window.alert("One choice must be selected from each field")
}
};

function uncheck(){
  if (document.getElementById('alltime').checked){
    document.getElementById("career").checked = false;
    document.getElementById("season").checked = false;
    document.getElementById("pts").checked = false;
    document.getElementById("ast").checked = false;
    document.getElementById("reb").checked = false;
  }

};

function uncheckrank(){
  if (document.getElementById("career").checked || document.getElementById("season").checked || document.getElementById("pts").checked || document.getElementById("ast").checked || document.getElementById("reb").checked) {
    document.getElementById('alltime').checked = false;
  }
}

