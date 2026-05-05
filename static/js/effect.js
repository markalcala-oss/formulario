
const card = document.getElementById("card");

document.addEventListener("mousemove", (e) => {
    const xAxis = (window.innerWidth / 2 - e.pageX) / 25;
    const yAxis = (window.innerHeight / 2 - e.pageY) / 25;

    card.style.transform = `rotateY(${xAxis}deg) rotateX(${yAxis}deg)`;
});

document.addEventListener("mouseenter", () => {
    card.style.transition = "none";
});

document.addEventListener("mouseleave", () => {
    card.style.transition = "transform 0.5s ease";
    card.style.transform = "rotateY(0deg) rotateX(0deg)";
});
