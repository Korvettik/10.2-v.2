import json


def load_json():
    """Функция загружает список словарей с кандидатами из json файла"""
    with open('candidates.json', 'r', encoding='utf-8') as json_file:
        cand_list = json.load(json_file)
    return cand_list

class Candidate:
    """класс содержит в себе все параметры кандидата"""

    def __init__(self, id, name, picture, position, gender, age, skills) -> object:
        """динамические атрибуты"""
        self.id = id  # порядковый идентификатор
        self.name = name  # имя
        self.picture = picture  # ссылка на изображение
        self.position = position  # профессия
        self.gender = gender  # пол
        self.age = age  # возраст
        self.skills = skills  # навыки


def page_general(person_list):
    """ функция, , выводящая всех персонажей (все персонажи - объекты)"""
    printing_list = []
    for person in person_list:
        printing_list.append(f'Имя кандидата - {person.name}')
        printing_list.append(f'Позиция кандидата {person.position}')
        printing_list.append(f'{person.skills}')
        printing_list.append(' ')

    return '<pre>'+'\n'.join(printing_list)+'<pre>'


def page_candidate_x(person_list, x):
    """ функция, , выводящая конкретного персонажа по его id"""
    printing_list = []
    for person in person_list:
        if person.id == x:
            printing_list.append(f'Имя кандидата - {person.name}')
            printing_list.append(f'Позиция кандидата {person.position}')
            printing_list.append(f'{person.skills}')
            printing_list.append(' ')
    return '<img src=person.picture>' +'<pre>'+'\n'.join(printing_list)+'<pre>'


def page_candidate_skill(person_list, skill):
    """ функция, , выводящая всех персонажей, у кого есть необходимый skill"""
    printing_list = []
    for person in person_list:
        if skill in person.skills.lower().split(', '):  # не учитываем регистр
            printing_list.append(f'Имя кандидата - {person.name}')
            printing_list.append(f'Позиция кандидата {person.position}')
            printing_list.append(f'{person.skills}')
            printing_list.append(' ')
    return '<pre>' + '\n'.join(printing_list) + '<pre>'
