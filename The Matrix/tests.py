# Output says "1 people's data"
import people

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
			

def GeneratePeople():
	personCount = InputForceResponseType('How many people would you like to generate? ', int)
	replace = InputBool('Would you like to replace the current list? (Will add to list if not) ')

	people.Generate(personCount, replaceList = replace)
	print('Generated ' + str(personCount) + " people's data and sent it to people_data.json")

GeneratePeople()