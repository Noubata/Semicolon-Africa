const prompt = require('prompt-sync')();	
const myArray = ["I love java", "c'est beau", "Je t'aime", "Una no get sense", "Okef", "Djow"]

let toCalculate = Math.floor(Math.random()*myArray.length);

let randomItem = myArray[toCalculate];
console.log(`Type this sentence: ${randomItem}`)

let theTime = performance.now()
let userInput = prompt("Type it here: ")
let endTime = performance.now()

let theDifference = endTime - theTime ;
let timeInSeconds = theDifference/1000;

let theShortString = Math.min(randomItem.length, userInput.length)

let countTheerror = 0
for( let check = 0; check < theShortString; check++){
if(randomItem[check] != userInput[check]){
countTheerror++
}
}

let timeInMinute = timeInSeconds/60;
let everyTypedCharacter = userInput.length

let grossWPM = everyTypedCharacter/(5 *timeInMinute)

let netWPN = grossWPM - countTheerror;

let correctCharacters = everyTypedCharacter - countTheerror;

let accurancyPercentage = (correctCharacters/everyTypedCharacter)*100

console.log(`You spent ${timeInSeconds.toFixed(2)} seconds to type the sentence`);
console.log(`Words per minute: ${netWPN.toFixed(2)}`)
console.log(`Accuracy Percentage: ${accurancyPercentage.toFixed(2)}`)