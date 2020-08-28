import loadquestion
from flask import render_template,  Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', questions=loadquestion.questions, tracks=loadquestion.tracks)

@app.route('/result', methods=["POST"])
def result():
    score_A = score_T = score_R = score_F = score_E = score_C = score_P = score_I = score_gae = score_gi = 0

    types = [i[0] for i in loadquestion.types]
    scores = []
    for i in range(len(loadquestion.types)):
        # 파라미터 변수 만들어주기
        temp_temp = 'q' + str(i)

        # request로 값 받아서 scores 배열에 집어넣고 형 변환하기
        temp = request.form[temp_temp]
        scores.append(temp)
        scores[i] = int(scores[i])

    # 각 항목별 점수 계산
    if types[i] == 'A':
        score_A += scores[i]
    elif types[i] == 'T':
        score_T += scores[i]
    elif types[i] == 'R':
        score_R += scores[i]
    elif types[i] == 'F':
        score_F += scores[i]
    elif types[i] == 'E':
        score_E += scores[i]
    elif types[i] == 'C':
        score_C += scores[i]
    elif types[i] == 'P':
        score_P += scores[i]
    elif types[i] == 'I':
        score_I += scores[i]
    elif types[i] == '개':
        score_gae += scores[i]
    elif types[i] == '기':
        score_gi += scores[i]

    # 타입 만들기
    if score_A > score_T:
        type_1 = 'A'
    else:
        type_1 = 'T'
    if score_R > score_F:
        type_2 = 'R'
    else:
        type_2 = 'F'
    if score_E > score_C:
        type_3 = 'E'
    else:
        type_3 = 'C'
    if score_P > score_I:
        type_4 = 'P'
    else:
        type_4 = 'I'
    if score_gae > score_gi:
        type_5 = '개'
    else:
        type_5 = '기'
    type_result = type_1 + type_2 + type_3 + type_4 + '-' + type_5

    # type_result에 따른 explanation과 img 리소스 추가하기!!

    # 이제 트랙 추천, 트랙 질문은 랜덤 아니고 순서 정해져 있음 / 치어리더-프렌즈-퐁-리킹-득근-하이-빅데이터-해유-곰-세돈권
    scores_track = []
    lists_track = [
        '치어리더도 없는게', '프렌즈', '조립퐁', '수박 겉햝기', '김득근', 'H A.I.', '해달 데이터센타', 'HAE-U', '곰비임비', '세상은 돈과 권력'
    ]
    track_5 = []
    track_4 = []
    track_3 = []
    track_2 = []
    track_1 = []

    for i in range(len(loadquestion.tracks)):
        temp_temp_track = 't' + str(i)

        # 값 받아오기 및 배열에 추가 및 정수로 형변환
        temp_track = request.form[temp_temp_track]
        scores_track.append(temp_track)
        scores_track[i] = int(scores_track[i])

        if scores_track[i] == 5:
            track_5.append(lists_track[i])
        elif scores_track[i] == 4:
            track_4.append(lists_track[i])
        elif scores_track[i] == 3:
            track_3.append(lists_track[i])
        elif scores_track[i] == 2:
            track_2.append(lists_track[i])
        elif scores_track[i] == 1:
            track_1.append(lists_track[i])

    if track_5:
        track = sorted(track_5)
        track = ', '.join(track)
    elif track_4:
        track = sorted(track_4)
        track = ', '.join(track)
    elif track_3:
        track = sorted(track_3)
        track = ', '.join(track)
    elif track_2:
        track = sorted(track_2)
        track = ', '.join(track)
    elif track_1:
        track = sorted(track_1)
        track = ', '.join(track)
    return render_template('result.html', img='back.img', type=type_result, explanation='back.explanation', tracks=track)

@app.route('/types')
def types():
    return render_template('types.html')
if __name__ == '__main__':
    app.run(debug=1)