import random

import pandas as pd

df = pd.read_csv('reported_enrolment.csv', index_col=0)
print(df.describe())
df2 = pd.read_csv('courses.csv')
fas_code_course_code = dict(zip(df2.fas_code, df2.course_code))

df['course_code'] = df.fas_code.map(fas_code_course_code)
df.drop_duplicates(inplace=True)
df.to_csv('course_enrolment.csv', index=False)

fas_code_enrollment = dict(zip(df.fas_code, df.enrollment))
df2['enrollment'] = df2.fas_code.map(fas_code_enrollment)
df2.to_csv('course_enrolment_verbose.csv', index=False)

# The difference of 1038 classes to 1331 courses is because some courses have two or more
# instructors but share the same FAS codes.
# Our calculations are not affected because the enrollment is the same for any unique FAS code.
print(df2.loc[df2.duplicated(subset=['fas_code'])])

# https://oir.harvard.edu/fact-book/enrollment
num_students = 7095
# num_students = 1000
num_classes_per_student = 4
fas_code_list = df.fas_code.tolist()
enrollment_list = df.enrollment.tolist()
students = []
students_cc = []

for i in range(num_students):
    classes_taken = []
    while len(classes_taken) < num_classes_per_student:
        class_candidate = random.choices(fas_code_list, enrollment_list)[0]
        print(class_candidate)
        if class_candidate not in classes_taken:
            classes_taken.append(class_candidate)
    students.append(classes_taken)
    students_cc.append([fas_code_course_code[fas_code] for fas_code in classes_taken])

pd.DataFrame(students).to_csv('random_generated_student_enrollment.csv', header=False)
pd.DataFrame(students_cc).to_csv('cc_random_generated_student_enrollment.csv', header=False)
