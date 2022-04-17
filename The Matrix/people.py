# TODO: Percentage-based stats, such as job, name, gender, etc
# TODO: Move names, jobs, etc to seperate JSON file

import uuid
import os.path
import random
import json

nullSchedule = []
for i in range(24):
	nullSchedule.append('null')

peopleJsonFile = 'people_data.json'
genderList = ['male', 'female', 'other']
masculineFirstNameList = ['Liam', 'Noah', 'Oliver', 'Elijah', 'William', 'James', 'Benjamin', 'Lucas', 'Henry', 'Alexander']
feminineFirstNameList = ['Olivia', 'Emma', 'Ava', 'Charlotte', 'Sophia', 'Amelia', 'Isabella', 'Mia', 'Evelyn', 'Harper']
lastNameList = ['Cervantes', 'Wall', 'Mckinney', 'Jenkins', 'Henderson', 'Holmes', 'Villegas', 'French', 'Hurley', 'Hunter']
jobList = ['Budget Analyst', 'Security Guard', 'Middle School Teacher', 'Environmental Scientist', 'Art Director', 'Hairdresser', 'Truck Driver', 'Veterinarian', 'Physician', 'Reporter']

def _GenerateName(gender):
	lastName = random.choice(lastNameList)

	if gender == 'male':
		return [random.choice(masculineFirstNameList), lastName]
	elif gender == 'female':
		return [random.choice(feminineFirstNameList), lastName]
	else:
		if (random.choice([True, False])):
			return [random.choice(masculineFirstNameList), lastName]
		else:
			return [random.choice(feminineFirstNameList), lastName]

def _GenerateNewPeople(num):
	newPeople = {}

	for i in range(num):
		personID = str(uuid.uuid4())
		gender = random.choice(genderList)
		name = _GenerateName(gender)
		occupation = random.choice(jobList)
		schedule = nullSchedule

		newPeople[personID] = {'name': name, 'gender': gender, 'occupation': occupation, 'schedule': schedule}

	return newPeople

def Generate(num, replaceList = False):
	newPeople = _GenerateNewPeople(num)
	
	if (replaceList == True or os.path.exists(peopleJsonFile) == False):
		with open(peopleJsonFile, 'w') as jsonData:
			json.dump(newPeople, jsonData, indent = 4)
	else:
		with open(peopleJsonFile, 'r+') as jsonData:
			peopleData = json.loads(jsonData.read())
			peopleData.update(newPeople)

			jsonData.seek(0)
			json.dump(peopleData, jsonData, indent = 4)