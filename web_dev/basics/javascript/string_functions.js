let str = "HELLO asa asxasx axsax"
let str2 = "WORLD"
let str3="   abc   "
console.log(str)
console.log(str.length)
console.log(str.charAt(1))
console.log(str.charCodeAt(1))
console.log(str.concat(str))
console.log(str.endsWith("LO"))
console.log(str.endsWith("XOX"))
console.log(str.includes("LL"))
console.log("-----------------------------------------------------")
console.log(str.lastIndexOf("L"))
console.log(str.localeCompare(str)) // return 0 for equality
console.log(str.localeCompare(str2)) // return 1 for greater 
console.log(str2.localeCompare(str)) // return -1 for lesser
console.log(str.normalize())
console.log(str.trim())
console.log(str.padEnd(10,"*"))
console.log(str.padStart(10,"*"))
console.log(str.repeat(3))
console.log(str.replace("LL", "XX"))
console.log("-----------------------------------------------------")
console.log(str.search("XX")) // -1 for not found
console.log(str.search("LL")) // return index if found
console.log(str.slice(2,4)) // from 2nd position to 4th position(excluding 4th position)
console.log(str.split(" "))
console.log(str.startsWith("a"))
console.log(str.startsWith("H"))
console.log(str.toLowerCase())
console.log(str.toUpperCase())
console.log(str3.trimEnd())
console.log(str3.trimStart())
console.log("-----------------------------------------------------")
let name="faheem pa"
let age=20
let place="Thrissur"
let name_age_place = `My name is ${name.toUpperCase()}. Im ${age} years old and Im from ${place}` // using back ticks `
console.log(name_age_place)
console.log("-----------------------------------------------------")
let a ="hello"
console.log(typeof a)
a=10
console.log(typeof a)
a=true
console.log(typeof a)
a=null
console.log(typeof a)
a='hey'
console.log(typeof a)