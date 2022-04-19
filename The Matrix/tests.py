import people
import string

def InputForceResponseType(inputText, type):
	while True:
		if (type == int):
			try:
				return int(input(inputText))
			except ValueError:
				print('Please submit an integer value\n')
		else:
			raise Exception('PROGRAM ERROR: Requested invalid input type')

def InputBool(inputText):
	while True:
		response = input(inputText)
		if (response in ['y', 'yes']):
			return True
		elif (response in ['n', 'no']):
			return False
		else:
			print("Valid responses are y, n, yes, and no\n")

def InputOrNone(inputText, cap = False):
	response = input(inputText)

	if (response == ''):
		return None
	elif (cap == True):
		response = string.capwords(response)
	return response
			
def GeneratePeople():
	personCount = InputForceResponseType('How many people would you like to generate? ', int)
	replace = InputBool('Would you like to replace the current list? (Will add to list if not) ')

	people.Generate(personCount, replaceList = replace)

	if (personCount == 1):
		print("\nGenerated 1 person's data and sent it to people_data.json")
	else:
		print('\nGenerated ' + str(personCount) + " people's data and sent it to people_data.json")

def GenerateCustomPerson():
	print('Creating a custom person. To randomly generate a field, just leave it blank')

	while True:
		name = InputOrNone('What should their name be? (First and Last: ex. Jane Doe) ', cap = True)
		if (name == None):
			break
		else:
			name = name.split()

		if (len(name) == 2):
			break
		else:
			print('Please submit a first and last name (ex. Jane Doe)\n')

	gender = InputOrNone('And their gender? (Any string is permitted) ', cap = True)
	occupation = InputOrNone('Okay, and what should their job be? ', cap = True)
	schedule = None

	people.GenerateCustom(name, gender, occupation, schedule)
	print('\nGenerated ' + name[0] + ' ' + name[1] + "'s data and sent it to people_data.json")

# Begin Program Logic
customOrRandom = ''
while customOrRandom not in ['custom', 'Custom', 'random', 'Random']:
	customOrRandom = input("Would you like to randomly generate people, or create a custom person? (Valid responses are 'custom' and 'random') ")

if (customOrRandom in ['custom', 'Custom']):
	GenerateCustomPerson()
elif (customOrRandom in ['random', 'Random']):
	GeneratePeople()