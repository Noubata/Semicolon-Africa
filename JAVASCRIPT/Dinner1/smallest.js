let numbers = 67530
let smallest = 0

for(let number = 0; number <=4; number++){
let eachOfNumbers = numbers%10
numbers = (numbers-(numbers % 10))/10
if (eachOfNumbers<smallest){
smallest = eachOfNumbers
}
}
console.log(smallest)
