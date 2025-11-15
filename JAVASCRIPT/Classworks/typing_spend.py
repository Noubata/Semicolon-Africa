import random
import time

my_array = ["I love java", "c'est beau", "Je t'aime", "Una no get sense", "Okef", "Djow"]


to_calculate= random.randint(0, len(my_array) - 1)

random_item = my_array[to_calculate]
print(f"Type this sentence: {random_item}")

the_time = time.monotonic()
user_input = input("Type it here: ") 
end_time = time.monotonic()

the_difference = end_time - the_time
time_in_seconds = the_difference

time_in_minute = time_in_seconds / 60

the_short_string = min(len(random_item), len(user_input))


count_the_error = 0
for check in range(the_short_string):
	if random_item[check] != user_input[check]:
		count_the_error += 1

count_the_error += abs(len(random_item) - len(user_input))

every_typed_character = len(user_input) 

gross_WPM = every_typed_character / (5 * time_in_minute)

net_WPM = gross_WPM - count_the_error

correct_characters = every_typed_character - count_the_error

accurancy_percentage = (correct_characters / every_typed_character) * 100

print(f"You spent {time_in_seconds:.2f} seconds to type the sentence")
print(f"Words per minute: {net_WPM:.2f}")
print(f"Accuracy Percentage: {accurancy_percentage:.2f}")