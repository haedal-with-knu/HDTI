import csv
import random
#CSV 파일만 쓰는 버전

all_Question_data = []
questions = []
tracks = []
types = []

f1 = open('question.csv', encoding='utf-8')

rdr1 = csv.reader(f1)
for index, line in enumerate(rdr1):
    if (index != 0):
        line[2] = int(line[2])
        all_Question_data.append(line)

random.shuffle(all_Question_data)

for data in all_Question_data:
    questions.append(data[0])
    types.append([data[1], data[2]])


f2 = open('track.csv', 'r', encoding='utf-8')

rdr2 = csv.reader(f2)

for line in rdr2:
    tracks += line
f2.close()