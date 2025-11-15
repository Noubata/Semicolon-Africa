let lists = [1, 2, 3, 4, 5, 6, 0, 7]

let newArray = [];

for(let check = 0; check < lists.length; check++){
if (lists[check] >= 1 || lists[check] <= 5){
	newArray+=[check]
}

}	
console.log(newArray)
