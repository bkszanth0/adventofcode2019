#advent_of_code_challenge_1

#define function to calculate fuel requirement for each of the modules
def calculate_fuel(mass):
    mod = mass%3
    fuel = (mass-mod)/3 - 2
    return fuel

#open and read source .txt
with open('/Users/bkszanth0/Desktop/py/git_practice/modules_input.txt', 'r') as f:

	#create variable for total fuel requirement, set it to 0
	total_fuel_requirement = 0

	#loop through all elements of the .txt file, calculate fuel requirements for each of them, add them to total
	for module in f:
	    total_fuel_requirement = total_fuel_requirement + calculate_fuel(float(module))

#print result
print('The total fuel requirement is ', total_fuel_requirement)