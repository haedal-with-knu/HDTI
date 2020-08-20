import csv

# 질문을 배열에 넣어주자
f = open('question.csv', 'r', encoding='utf-8')
f2 = open('track.csv', 'r', encoding='utf-8')
questions = []
tracks = []

rdr = csv.reader(f)
rdr2 = csv.reader(f2)

for line in rdr:
    # print(line)
    questions += line
f.close()

for line in rdr2:
    tracks += line
f.close()