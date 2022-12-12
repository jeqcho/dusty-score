import pandas as pd
import networkx as nx

df = pd.read_csv('data/dummy.csv')
fas_code_list = df.fas_code.tolist()

df_students = pd.read_csv('student_class_choices.csv', header=None)

memberships = []

for index, row in df_students.iterrows():
    membership_row = [row[0]] + [0] * len(fas_code_list)
    for i in range(1, len(row)):
        print(row[i])
        if row[i] in fas_code_list:
            # membership_row[fas_code_list.index(row[i]) + 1] = 1
            membership_row[fas_code_list.index(row[i]) + 1] = 1
    memberships.append(membership_row)

# add Dusty
dusty_row = [len(df_students)] + [0] * len(fas_code_list)
# dusty_row[fas_code_list.index('FAS-207485-2218-1-1-001') + 1] = 1
dusty_row[fas_code_list.index('MATH 22A') + 1] = 1
memberships.append(dusty_row)
df_membership = pd.DataFrame(memberships, columns=['index'] + fas_code_list)
df_membership.to_csv('membership.csv', index=False)
