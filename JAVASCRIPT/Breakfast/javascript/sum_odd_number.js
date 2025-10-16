let number = 2345;
let toSeparate = 0;
let sum =0
let toCheck = 0
while toCheck < 5:
	toCheck+=1
	toSeparate = number%10
	number = (number-(number%10))//10
	if number % 2 == 1:
		sum+=number
console.log(sum)