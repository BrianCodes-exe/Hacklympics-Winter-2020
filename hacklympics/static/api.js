var popup = document.getElementById("myPopup");
var span = document.getElementsByClassName("close")[0];
var command = "{{ command }}";
if (command == "/weather") {
    popup.style.display = "block";
}
if (command == "no city") {
    alert("Proper use of /weather command is:\n/weather <city-name>")
}
if (command == "error") {
    alert("Enter in a valid command")
}
span.onclick = function() {
    popup.style.display = "none";
}