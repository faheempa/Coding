const cursor = document.querySelector(".cursor");
var timeout;

document.addEventListener("mousemove", e => {
    let x = e.pageX;
    let y = e.pageY;
    cursor.style.left = x + "px";
    cursor.style.top = y + "px";
    cursor.style.display = "block";

    function mousestopped() {
        cursor.style.display = "none";
    }

    clearTimeout(timeout);
    timeout = setTimeout(mousestopped, 1000);
})

document.addEventListener("mouseout", e => {
    cursor.style.display = "none";
})