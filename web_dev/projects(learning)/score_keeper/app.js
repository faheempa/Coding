const p1 = {
    score: 0,
    button: document.querySelector("#player1"),
    display: document.querySelector("#p1Display")
}
const p2 = {
    score: 0,
    button: document.querySelector("#player2"),
    display: document.querySelector("#p2Display")
}
const winning_score_selection = document.querySelector("#winscore");
let winning_score = 3;
let game_over = false;
const reset_button = document.querySelector("#reset")

p1.button.addEventListener("click", function (e) {
    updateScore(p1, p2);
})

p2.button.addEventListener("click", function (e) {
    updateScore(p2, p1);
})

reset_button.addEventListener("click", reset)

winning_score_selection.addEventListener("change", function (e) {
    winning_score = parseInt(this.value);
    reset();
})

function updateScore(p, e) {
    if (!game_over) {
        p.score += 1;
        p.display.innerText = p.score;
        if (p.score == winning_score) {
            game_over = true;
            p.display.classList.add("green");
            e.display.classList.add("red");
            p.button.disabled = true;
            e.button.disabled = true;
            p.button.classList.add("grey");
            e.button.classList.add("grey");
        }
    }
}

function reset() {
    for (let p of [p1, p2]) {
        p.score = 0;
        p.display.innerText = 0;
        p.display.classList.remove("red", "green");
        p.button.disabled = false;
        p.button.classList.remove("grey");
    }
    game_over = false;
}
