# Enhancements: Percentage-based stats, such as job, name, gender, etc

import random
import json

# DEFINE VARIABLES
personCount = 2
nullSchedule = []

masculineFirstNameList = ['Liam', 'Noah', 'Oliver', 'Elijah', 'William', 'James', 'Benjamin', 'Lucas', 'Henry', 'Alexander']
feminineFirstNameList = ['Olivia', 'Emma', 'Ava', 'Charlotte', 'Sophia', 'Amelia', 'Isabella', 'Mia', 'Evelyn', 'Harper']
lastNameList = ['Cervantes', 'Wall', 'Mckinney', 'Jenkins', 'Henderson', 'Holmes', 'Villegas', 'French', 'Hurley', 'Hunter']
jobList = ['Budget Analyst', 'Security Guard', 'Middle School Teacher', 'Environmental Scientist', 'Art Director', 'Hairdresser', 'Truck Driver', 'Veterinarian', 'Physician', 'Reporter']

# DEFINE A NULL SCHEDULE. THIS IS THE STARTING SCHEDULE OF EVERY PERSON, BEFORE BEING FILLED OUT
#for i in range(24):
#	nullSchedule.append('null')

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

def generateOccupation():
	return random.choice(jobList)

# DEFINE A DICTIONARY OF GARBAGE DATA ON A FEW PEOPLE. THIS IS USED FOR TESTING
people = {
	'person1':
	{
		'name': generateName('male'),
		'gender': 'male',
		'occupation': generateOccupation(),
		'schedule': nullSchedule
	},
	'person2':
	{
		'name': generateName('female'),
		'gender': 'female',
		'occupation': generateOccupation(),
		'schedule': nullSchedule
	},
	'person3':
	{
		'name': generateName('other'),
		'gender': 'other',
		'occupation': generateOccupation(),
		'schedule': nullSchedule
	}
}

print(people)

with open('json_data.json', 'w') as outfile:
    json.dump(people, outfile, indent = 4)