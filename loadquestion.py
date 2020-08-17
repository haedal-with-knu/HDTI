import csv

# 질문을 배열에 넣어주자
f = open('question.csv', 'r')
questions =[]

rdr = csv.reader(f)
for line in rdr:
    # print(line)
    questions += line

f.close()

