let number = 0
let count = 0
let count1 = 0
while number<100:
	number+=1
	if (number == 1 || number == 3 || number == 5 || number == 7 || number == 11 || number == 13){
		count+=1
	}
	if (number % 2 !=0 ){
		count1+=1
	}
console.log(count+count1)