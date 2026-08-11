const box = document.getElementById("box");
const card = document.getElementById("loginCard");

setTimeout(() => {
    box.style.transition = "all 1s ease";

    box.style.width = "320px";
    box.style.height = "250px";

    box.style.left = "190px";
    box.style.bottom = "75px";

    setTimeout(() => {
        box.style.opacity = "0";
        card.classList.add("show");
    }, 1000);

}, 3000);