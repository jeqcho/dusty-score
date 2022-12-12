import pandas as pd

df = pd.read_csv('random_generated_student_enrollment.csv')
print(df)

df_course = pd.read_csv('output.csv')
print(df_course)
print(df_course.loc[df_course.duplicated(subset=['course_code'])])