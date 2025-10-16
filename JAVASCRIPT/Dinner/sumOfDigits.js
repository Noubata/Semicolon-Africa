let number= 1403;

let number1 = number/1000;
let number2 = (number%1000)/100;
let number3 = (number%100)/10;
let number4 = number%10;

let sum = number1+number2+number3+number4;

console.log(sum)