// Get the modal
var modall = document.getElementById('myModall');

// Get the button that opens the modal
var btnn = document.getElementById("modall");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal 
btn.onclick = function() {
    modall.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modall.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modall) {
        modall.style.display = "none";
    }
}