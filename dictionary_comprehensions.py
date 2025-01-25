import random


names = ['alex', 'beth', 'carolina', 'dave', 'eleanor', 'freddie']
# [new_key: new_value for item in dictionary]
students_scores = {student:random.randint(1, 100) for student in names}


# [new_key:new_value for (key, value) in dictionary.items() if test]
passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}
print(passed_students)

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day:(weather * 9/5) + 32 for (day, weather) in weather_c.items()}

print(weather_f)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words = sentence.split()
# print(words)
result = {word:len(word) for word in words}
print(result)
