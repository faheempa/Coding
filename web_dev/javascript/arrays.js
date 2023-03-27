let a = [1, 2, 3]
console.log(a)
let b = ["hey", "abc", "hello"]
console.log(b)
let c = [true, false, false]
console.log(c)
console.log(a[0])
console.log(a[1])
console.log(a[2])
console.log(a[3])
let d = [1, "faheem", true, 'abc', 1.043, NaN]
console.log(d)
console.log(d.length)
console.log("-----------------------------------------")

// push - add element to the end
let arr = [1, 2, 3]
console.log(arr)
arr.push(4)
console.log(arr)
arr.push(5, 6)
console.log(arr)
arr.push(7, 8, 9, 10)
console.log(arr)
arr.push("faheem")
console.log(arr)
arr.push(true)
console.log(arr)
arr.push(NaN)
console.log(arr)
console.log("-----------------------------------------")

// pop - removes element from end
console.log(arr)
let x = arr.pop()
console.log(x)
console.log(arr)
x = arr.pop()
console.log(x)
console.log(arr)
arr.pop()
console.log(arr)
arr.pop()
console.log(arr)
console.log("-----------------------------------------")

// shift - remives element from front
let arr2 = [3, 4, 5]
let y = arr2.shift()
console.log(y)
console.log(arr2)
arr2.shift()
console.log(arr2)
console.log("-----------------------------------------")

// sunhift - add element from front
let arr3 = [1, 2, 3]
arr3.unshift(4)
console.log(arr3)
arr3.unshift(5, 6, 7)
console.log(arr3)
console.log("-----------------------------------------")

let a1 = [1, 2, 3]
let a2 = [4, 5]
let a3 = a1.concat(a2)
console.log(a3)

console.log(a1.includes(1))
console.log(a1.includes(5))

a1.reverse()
console.log(a1)

console.log(a3)
let a4 = a3.slice(2)
console.log(a4)
a4 = a3.slice(2, 4)
console.log(a4)
a4 = a3.slice(0, 4)
console.log(a4)

console.log(a3)
console.log("-----------------------------------------")

// we need change numbers to [1,2,3,4,5,6,7,8,9,10,11,12,13]
let numbers = [1, 2, 4, 5, 9, 7, 8, 9, 12, 44, 13]
console.log(numbers)
numbers.splice(2, 0, 3) // [1,2,3,4,5,9,7,8,9,12,44,13]
console.log(numbers)
numbers.splice(5, 1, 6) // [1,2,3,4,5,6,7,8,9,12,44,13]
console.log(numbers)
numbers.splice(9, 0, 10, 11) // [1,2,3,4,5,6,7,8,9,10,11,12,44,13]
console.log(numbers)
numbers.splice(12, 1) // [1,2,3,4,5,6,7,8,9,10,11,12,13]
console.log(numbers)
console.log("-----------------------------------------")

let num = [1, 2, 3, 4, 5, 6]
console.log(num)
num.fill(0)
console.log(num)
num = [1, 2, 3, 4, 5, 6]
console.log(num)
console.log(num.toString())
console.log(typeof num.toString())
let chars = ['a', 'b', 'c', 'd']
console.log(chars.toString())
console.log(typeof chars.toString())
console.log("-----------------------------------------")

let nums = [1, 2, 3, 4, 5]
function isOdd(n) {
    return n % 2 == 1
}
const oddvals = nums.filter(isOdd)
console.log(oddvals)

const evenvals = nums.filter(n => n % 2 == 0)
console.log(evenvals)

const doubles = nums.map(val => val * 2)
console.log(nums)
console.log(doubles)

const evenDoubles = nums.filter(n => n % 2 == 0).map(n => n * 2)
console.log(evenDoubles)
console.log("-----------------------------------------")

vals = [2, 3, 5, 7]
function isPrime(n) {
    for (let i = 2; i <= Math.sqrt(n); i++) {
        if (n % i == 0) return false
    }
    return true
}
console.log(vals.every(isPrime))
console.log(vals.every(n => n < 10))
console.log(vals.every(n => n < 5))

console.log(vals.some(n => n > 10))
console.log(vals.some(n => n == 5))
console.log("-----------------------------------------")

const prices = [10, 20, 30, 40, 50]

const sum = prices.reduce((total, val) => total + val)
console.log(sum)

const maxprice = prices.reduce((max, val) => {
    if(max<val) return val
    else return max
})
console.log(maxprice)


