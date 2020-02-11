#advent_of_code_challenge_1p2

#define function to calculate fuel requirement for each of the modules
def calculate_fuel(mass):
    mod = mass%3
    fuel = (mass-mod)/3 - 2
    return fuel

#open and read source .txt
with open('/Users/bkszanth0/Desktop/py/git_practice/modules_input.txt', 'r') as f:
	#set variable for total fuel to zero
	total_fuel = 0

	#loop through elements of .txt file
	for module in f:

		#x will be used to calculate fuel requirements 
		x = float(module)
		while x>=9:

			#calculate fuel from x
			x = calculate_fuel(x)

			#add calcualted value to total fuel requirements
			total_fuel = total_fuel + x


	print('Total fuel requirements (fuel4fuel included): ', total_fuel)
