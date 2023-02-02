let start=1
let end=5

for (let index = 0; index < 1000; index++) {
    random_no=Math.floor(Math.random()*10*(end+start))%(end-start+1)+start
    if (random_no>end || random_no<start) {
        console.log(random_no)
    }
}
for (let index = 0; index < 1000; index++) {
    random_no=Math.floor(Math.random()*10*(end+start))%(end-start)+start
    if (random_no>=end || random_no<start || random_no==NaN) {
        console.log(random_no)
    }
}
for (let index = 0; index < 1000; index++) {
    random_no=Math.floor(Math.random()*10*(end+start))%(end-start-1)+start+1
    if (random_no>=end || random_no<=start || random_no==NaN) {
        console.log(random_no)
    }
}
console.log("all correct")


// to generate random value from start to end, inclusivily
// Math.floor(Math.random()*10*(end+start))%(end-start+1)+start

// to generate random value from start(including) to end(excluding)
// Math.floor(Math.random()*10*(end+start))%(end-start)+start

// to generate random value from start(excluding) to end(excluding)
// Math.floor(Math.random()*10*(end+start))%(end-start-1)+start+1

