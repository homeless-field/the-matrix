# Enhancements: Percentage-based stats, such as job, name, gender, etc
# Known Bugs: 1) Input is not type-sensitive. Incorrect input crashes program 2) Output says "1 people's data"

import os.path
import random
import json

# DEFINE VARIABLES
personCount = 2
dataFileName = 'person_data.json'
nullSchedule = []

genderList = ['male', 'female', 'other']
masculineFirstNameList = ['Liam', 'Noah', 'Oliver', 'Elijah', 'William', 'James', 'Benjamin', 'Lucas', 'Henry', 'Alexander']
feminineFirstNameList = ['Olivia', 'Emma', 'Ava', 'Charlotte', 'Sophia', 'Amelia', 'Isabella', 'Mia', 'Evelyn', 'Harper']
lastNameList = ['Cervantes', 'Wall', 'Mckinney', 'Jenkins', 'Henderson', 'Holmes', 'Villegas', 'French', 'Hurley', 'Hunter']
jobList = ['Budget Analyst', 'Security Guard', 'Middle School Teacher', 'Environmental Scientist', 'Art Director', 'Hairdresser', 'Truck Driver', 'Veterinarian', 'Physician', 'Reporter']

# DEFINE A NULL SCHEDULE. THIS IS THE STARTING SCHEDULE OF EVERY PERSON, BEFORE BEING FILLED OUT
for i in range(24):
	nullSchedule.append('null')

def generateName(gender):
	if gender == 'male':
		firstName = random.choice(masculineFirstNameList)
	elif gender == 'female':
		firstName = random.choice(feminineFirstNameList)
	else:
		if (random.randrange(0, 1)) == 0:
			firstName = random.choice(masculineFirstNameList)
		else:
			firstName = random.choice(feminineFirstNameList)

	lastName = random.choice(lastNameList)

	return [firstName, lastName]

def generatePeople(num):
	people = []
	x = 0

	while (x < num):
		gender = random.choice(genderList)
		people.append({
			'name': generateName(gender),
			'gender': gender,
			'occupation': random.choice(jobList),
			'schedule': nullSchedule
		})
		x += 1

	return people

# BEGIN PROGRAM LOGIC
addOrReplace = int(input('Would you like to add people to the current list or replace the list? (1 or 2) '))
personCount = int(input('How many people would you like to generate? '))
newData = generatePeople(personCount)

# WRITE THE CORRECT AMOUNT OF PEOPLE TO A JSON FILE AS REQUESTED
if (os.path.exists('person_data.json') == False or addOrReplace == 2):
	with open(dataFileName, 'w') as dataFile:
		json.dump(newData, dataFile, indent = 4)
elif (addOrReplace == 1):
	with open(dataFileName, 'r+') as dataFile:
		try:
			currentData = json.loads(dataFile.read())
		except json.decoder.JSONDecodeError:
			currentData = []

		currentData.extend(newData)
		dataFile.seek(0)
		json.dump(currentData, dataFile, indent = 4)
else:
	raise Exception('Invalid Answer')

print('Generated ' + str(personCount) + " people's data and sent it to person_data.json")