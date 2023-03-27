const body = document.querySelector("body");

function changeColor(color, delay) {
    return new Promise((resole, reject) => {
        setTimeout(() => {
            body.style.backgroundColor = color;
            resole();
        }, delay);
    })
}


async function rainbow() {
    while (1) {
        await changeColor("red", 100);
        await changeColor("orange", 100);
        await changeColor("yellow", 100);
        await changeColor("green", 100);
        await changeColor("blue", 100);
        await changeColor("indigo", 100);
        await changeColor("violet", 100);
    }
    return "done"
}

rainbow();
