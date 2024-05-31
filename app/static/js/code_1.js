var eye = document.getElementById("icon_eye");
var input = document.getElementById("contrasena");

eye.addEventListener("click", function() {
    if (input.type === "password") {
        input.type = "text";
        eye.style.color= "#f05205";
    } else {
        input.type = "password";
        eye.style.color= "#999";
    }
});

function redirectToIndex() {
    window.location.href = '/';
}

