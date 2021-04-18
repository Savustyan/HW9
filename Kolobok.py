"""
Описать сказку про Колобка (не обязательно про колобка) классами.
Ссылка на текст сказки  - https://nukadeti.ru/skazki/kolobok
Нужно создать классы деда, бабки, колобка, лисы (по желанию можно добавить героев) с методами, которые будут имитировать
реплики героев в сказке. Описывать реплики можно не полностью, вызывать методы нужно в очередности сценария,
как использовать - дело фонтазии))
к примеру:
class Fox(ParentClass):
    def eat_kolobok(self, kolobok):
        print('MMMM yammy') реплика лисы
        kolobok.die() метод, который описывает смерть колобка
fox = Fox()
fox.eat_kolobok(kolobok)
Тут описан пример как можно вызвать метод колобка в методе лисы, т.е. действие обязательно вызовет измение другого
объекта. Не стоит забывать что в питоне все типы подобны и мы можем передавать параметрами в метод/функцию любой
питоновский объект
"""


class Hero:
    def __init__(self, name):
        self.name = name


class Ded(Hero):
    def ask_babka_to_bake_kolobok(self, babka):
        print('Babka, bake a Kolobok')
        babka.bake_kolobok()


class Babka(Hero):

    def bake_kolobok(self):
        print('Babka scrape along the bottom')
        print('Babka cooked Kolobok')


class Kolobok(Hero):
    def escape(self, from1):
        print('Kolobok escape from', from1)

    def sings_a_song(self, from2):
        print('Sings a song for', from2)

    def die(self):
        print('Kolobok eaten by Fox. End')


class Hare(Hero):
    def MeetHare(self):
        print('Hare: Hello, Kolobok, I want to eat you')


class Wolf(Hero):
    def MeetWolf(self):
        print('Wolf: Hello, Kolobok, I want to eat you')


class Bear(Hero):
    def MeetBear(self):
        print('Bear: Hello, Kolobok, I want to eat you')


class Fox(Hero):

    def MeetFox(self):
        print('Fox: Hello, Kolobok, I want to eat you')

    def eat_kolobok(self, kolobok):
        print('Fox eat Kolobok')
        kolobok.die()


def tale():
    #  ded - Объект, Ded - экземпляр класса Hero, 'ded1' - name
    ded = Ded('ded1')
    babka = Babka('babka1')
    kolobok = Kolobok('kolobok1')
    hare = Hare('hare1')
    wolf = Wolf('wolf1')
    bear = Bear('Bear1')
    fox = Fox('fox1')

    ded.ask_babka_to_bake_kolobok(babka)
    kolobok.escape(babka.name)
    hare.MeetHare()
    kolobok.sings_a_song(hare.name)
    kolobok.escape(hare.name)
    wolf.MeetWolf()
    kolobok.sings_a_song(wolf.name)
    kolobok.escape(wolf.name)
    bear.MeetBear()
    kolobok.sings_a_song(bear.name)
    kolobok.escape(bear.name)
    fox.MeetFox()
    kolobok.sings_a_song(fox.name)
    kolobok.sings_a_song(fox.name)
    kolobok.sings_a_song(fox.name)
    fox.eat_kolobok(kolobok)


tale()
