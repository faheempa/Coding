function sum(...nums) // rest
{
    return nums.reduce((total, val) => total + val)
}
console.log(sum(1, 2, 3, 4, 5))

let a = [1, 2, 3, 4, 5]
console.log(sum(...a)) // spread
console.log("--------------------------------------------")

const [n1, n2, ...n3] = a;
console.log(n1)
console.log(n2)
console.log(n3)
console.log("--------------------------------------------")

let odd = [1, 3, 5], even = [2, 4, 6]
let all = [...odd, ...even]
console.log(all)
console.log("--------------------------------------------")

let obj1 = { name: "faheem", age: 20 }
let obj2 = { place: "thrissur", age: 21 }
let obj3 = { ...obj1, ...obj2 }
console.log(obj3)

let user = { name: "faheem", email: "faheem@gamil.com", password: "12345678" }
let newUser = { ...user, id: 12322, admin: false }
console.log(newUser)
console.log("--------------------------------------------")

let { name, email, password } = user;
console.log(`name: ${name}, email: ${email}, password: ${password}`)

let { name: username, email: useremail, password: userpass } = user;
console.log(`name: ${username}, email: ${useremail}, password: ${userpass}`)
console.log("--------------------------------------------")

function fun({name, email})
{
    console.log(name)
    console.log(email)
}
fun(user)
