import os
from jinja2 import Environment, FileSystemLoader, select_autoescape
from random import randint, sample

def main():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html'])
    )
    template = env.get_template('template.html')

    os.makedirs('characters', exist_ok=True)
    question = int(input('Сколько карточек вы хотите создать? '))

    for number in range(question):
        races = ["Человек", "Эльф", "Орк", "Гном"]
        character_race = races[randint(0,3)]

        classes = ["Маг", "Воин", "Охотник", "Ассасин", "Бард"]
        character_class = classes[randint(0,4)]


        classes_base = {
                "Маг" : {
                    'skills' : ['Стрела ледяного огня', 'Снятие проклятия', 'Огненный взрыв', 'Обледенение', 'Ледяное копье', 'Конус холода', 'Прилив сил', 'Морозный доспех'],
                    'stats' : {'strength' : randint(1,3), 'agility' : randint(1,3), 'intelligence' : 15, 'luck' : randint(1,3), 'temper' : randint(1,3)},
                    'image' : '../images/wizard.png',
                },
                "Воин" : {
                    'skills' : ['Блок щитом', 'Казнь', 'Рывок', 'Боевой крик', 'Вихрь', 'Парирование', 'Мощный удар', 'Глубокие раны'],
                    'stats' : {'strength' : 15, 'agility' : randint(1,3), 'intelligence' : randint(1,3), 'luck' : randint(1,3), 'temper' : randint(1,3)},
                    'image' : '../images/warrior.png',
                },
                "Охотник" : {
                    'skills' : ['Верный выстрел', 'Чародейский выстрел', 'Стенающая стрела', 'Стрелы ветра', 'Призыв питомца', 'Глаз зверя', 'Осветительная ракета', 'Приручение животного'],
                    'stats' : {'strength' : randint(1,3), 'agility' : 15, 'intelligence' : randint(1,3), 'luck' : randint(1,3), 'temper' : randint(1,3)},
                    'image' : '../images/archer.png',
                },
                "Ассасин" : {
                    'skills' : ['Отравление', 'Взлом замка', 'Подлый трюк', 'Исчезновение', 'Ложный выпад', 'Внезапный удар', 'Ошеломление', 'Спринт'],
                    'stats' : {'strength' : randint(1,3), 'agility' : randint(1,3), 'intelligence' : randint(1,3), 'luck' : 15, 'temper' : randint(1,3)},
                    'image' : '../images/assasin.png',
                },    
                "Бард" : {
                    'skills' : ['Аккорды ветра', 'Аккорды воды', 'Исцеление', 'Соната жизни', 'Пауза', 'Плач сирен', 'Песнь ветра', 'Реквием'],
                    'stats' : {'strength' : randint(1,3), 'agility' : randint(1,3), 'intelligence' : randint(1,3), 'luck' : randint(1,3), 'temper' : 15},
                    'image' : '../images/bard.webp',
                }
            }



        current_class = classes_base[character_class]
        skills = sample(current_class['skills'], 3)
        rendered_page = template.render(
            name = "Артемис",
            race = character_race,
            character_class = character_class,
            **current_class['stats'],
            image = current_class['image'],
            first_skill = skills[0],
            second_skill = skills[1],
            third_skill = skills[2],
        )

        with open(f'characters/index{number+1}.html', 'w', encoding="utf8") as file:
            file.write(rendered_page)


if __name__ == '__main__':
    main()