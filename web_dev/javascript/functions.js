function fun1(fun) {
    fun();
}

function fun2() {
    console.log("this is function 2");
}

fun1(fun2);
console.log("-----------------------------------------")


function fun3(x, y) {
    console.log(`sum = ${x + y}`);
}
const a = fun3;
a(10, 20);
console.log("-----------------------------------------")

function fun4() {
    function fun5() {
        console.log("this is function 5");
    }
    fun5();
}
fun4();
console.log("-----------------------------------------")

function makeInBetweenFunc(min, max) {
    return function (value) {
        return value > min && value < max;
    }
}

const f1 = makeInBetweenFunc(1, 10);
const f2 = makeInBetweenFunc(11, 20);
const f3 = makeInBetweenFunc(21, 30);

console.log(f1(4)); // true
console.log(f1(13)); // false
console.log(f2(16)); // true
console.log(f2(34)); // false
console.log(f3(26)); // true
console.log(f3(130)); // false
console.log("-----------------------------------------")

const fun6 = function () { console.log("this is fun 6") }
fun6()
console.log("-----------------------------------------")

const obj1 = {
    name: "faheem",
    place: "thrissur",
    age: 21,
    print() {
        console.log(`My name is ${this.name}, Im from ${this.place} and Im ${this.age} years old`); // 'this' is essential
    }
}
obj1.print()
console.log("-----------------------------------------")

const fun7 = () => console.log("HELLO")
fun7()

const max = (a, b) => {
    if (a > b) return a
    else return b
}
console.log(max(1, 2))

const sum = (a, b) => a + b;
console.log(sum(10, 20));
console.log("-----------------------------------------")


