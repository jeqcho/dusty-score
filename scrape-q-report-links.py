from bs4 import BeautifulSoup
import pandas as pd

with open('QReports.html', 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')

rows = []

for link in soup.find_all('a'):
    if 'bluera' not in link.get('href'):
        continue
    segments = link.get_text().split(' ')
    segments = [segment for segment in segments if segment.strip() != '']
    # get the course code eg MATH 22A
    course_code = segments[0] + ' ' + segments[1].split('-')[0]
    text = ' '.join(segments)[len(course_code) + 1:]
    print(text)
    course_title, course_teacher, _ = text.split('\n')
    course_teacher = course_teacher.strip()[1:-1]
    row = [
        course_code.strip(),
        course_title.strip(),
        course_teacher.strip(),
        link.get('href'),
        link.get('name')
    ]
    rows.append(row)

pd.DataFrame(rows, columns=['course_code', 'course_title', 'course_teacher', 'link', 'fas_code']).to_csv("courses.csv",
                                                                                                         index=None)

print(len(rows))
