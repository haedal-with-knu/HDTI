import csv
import pandas as pd

# 질문을 배열에 넣어주자.. 하나는 판다스로 하나는 그냥 파일 입출력으로..
df1 = pd.read_csv('question.csv', encoding='utf-8')
f2 = open('track.csv', 'r', encoding='utf-8')
questions = []
tracks = []


rdr2 = csv.reader(f2)
randf = df1.sample(n=len(df1))
questions = [x[0] for x in randf.iloc[:, :1].values.tolist()]
types = randf.iloc[:, 1:].values.tolist()



for line in rdr2:
    tracks += line
f2.close()