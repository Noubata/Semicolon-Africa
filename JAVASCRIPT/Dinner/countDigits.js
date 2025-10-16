let number = 2345;
let toSeparate = 0;
let rr = 0
let count = 0
for(let toCheck = 0; toCheck < 5; toCheck++){
toSeparate = number%10
number = (number-(number%10))/10
count+=1
}
console.log(count)