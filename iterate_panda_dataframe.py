import pandas

student_dict = {
    'students': ['Pinky', 'Angela', 'James', 'Lily'],
    'scores':[45,56,67,78]
}

for (key, value) in student_dict.items():
    print(value)


# using pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# loop through dataframe
for (key, value) in student_data_frame.items():
    print(value)

# pandas have inbuilt for data frames
for (index, row) in student_data_frame.iterrows():
    # print(index)
    # print(row)
    # print(row.students)
    # print(row.scores)
    if row.students == 'Pinky':
        print(row.scores)
