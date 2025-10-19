let numbers = 67530
let largest = 0

for(let number = 0; number <=4; number++){
let eachOfNumbers = numbers%10
numbers = (numbers-(numbers % 10))/10
if (eachOfNumbers>largest){
largest = eachOfNumbers
}
}
console.log(largest)
