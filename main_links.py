from flask import Flask
from class_candidate import Candidate, load_json, page_general, page_candidate_x, page_candidate_skill
app = Flask(__name__)

candidats_list = load_json()  #сразу подгрузили список словарей кандидатов

person_list = []  #создадим пустой список персонажей - объектов
for candidate in candidats_list:
    id = candidate['id']
    name = candidate['name']
    picture = candidate['picture']
    position = candidate['position']
    gender = candidate['gender']
    age = candidate['age']
    skills = candidate['skills']
    person = Candidate(id, name, picture, position, gender, age, skills)
    person_list.append(person)


@app.route('/', methods=['GET', 'POST'])  # главная страница, выводящая список json
def main_page():
    return page_general(person_list)


@app.route('/candidate/<int:x>/', methods=['GET', 'POST'])  # страница, выводящая конкретного кандидата по его id
def main_candidate_x(x):
    return page_candidate_x(person_list, x)


@app.route('/skill/<skill>/', methods=['GET', 'POST'])  # страница, выводящая список кандидатов, у которых содержится конкретный навык
def main_candidate_skill(skill):
    return page_candidate_skill(person_list, skill)


if __name__ == '__main__':
    app.run(debug=True)