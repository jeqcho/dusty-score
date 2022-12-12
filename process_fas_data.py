import pandas as pd

with open('Class_Detail_121222.csv', 'r') as f:
    data = f.readlines()

current_row = []
rows = []
courses = []

for row in data:
    if row.split(',')[0] != '':
        rows.append(current_row)
        print(current_row)
        current_row = []
    if "EXPOS 20" not in row.split(',')[1].strip() and "EXPOS 10" not in row.split(',')[1].strip():
        current_row.append(row.split(',')[1].strip())
        courses.append(row.split(',')[1].strip())

rows.append(current_row)
rows.pop(0)
courses = list(set(courses))

pd.DataFrame(rows).to_csv('student_class_choices.csv', header=False)
df = pd.DataFrame()
df['fas_code'] = courses
df['course_code'] = courses
df.to_csv('data/dummy.csv')
