"""
Вы приехали помогать на ферму Дядюшки Джо и видите вокруг себя множество разных животных:

гусей "Серый" и "Белый"
корову "Маньку"
овец "Барашек" и "Кудрявый"
кур "Ко-Ко" и "Кукареку"
коз "Рога" и "Копыта"
и утку "Кряква"
Со всеми животными вам необходимо как-то взаимодействовать:
кормить
корову и коз доить
овец стричь
собирать яйца у кур, утки и гусей
различать по голосам(коровы мычат, утки крякают и т.д.)
Задание 1:
Реализовать родительский класс для всех животных и вынести общее поведение в него.
От родительского класса должны будут отнаследоваться все остальные животные.
В родительском классе должно быть 2-3 общих класса и общие поля.

Задание 2:
Используя методы из родительского класса, вызывать их в цикле у списка всех животных.
"""

class Animals():
    def __init__(self,name,weight):
        self.weight = weight
        self.name = name
    def eat(self,food):
      self.weight+=food
      return self.weight
class Artiodactyls(Animals):
    feature = "Парнокопытные"
    pass
class Birds(Animals):
    feature = "Птицы"
class AnimalsMilking(Artiodactyls):
  milk =0
  def produces(self, quantity_milkings):
    self.milk += quantity_milkings * 10
    return  f"{self.milk} литров молока"
class AnimalWool(Artiodactyls):
  wool = 0
  def produces(self, quantity_wool):
    self.wool += quantity_wool*5
    return f"{self.wool} килограмм шерсти"
class BirdsEggs(Birds):
  egg = 0
  def produces(self, number_times):
    self.egg += number_times*10
    return f"{self.egg} яиц"
class Cow(AnimalsMilking):
  view = "Корова"
  def makes_sound(self):
    return "Мууууу"
class Goat(AnimalsMilking):
  view = "Коза"
  def makes_sound(self):
    return "Беееее"
class Sheep (AnimalWool):
  view = "Овца"
  def makes_sound(self):
    return "Мееее"
class Duck (BirdsEggs):
  view = "Утка"
  def makes_sound(self):
    return "Кря-Кря"
class Chicken (BirdsEggs):
  view = "Курица"
  def makes_sound(self):
    return "Курлык"
class Goose (BirdsEggs):
  view = "Гусь"
  def makes_sound(self):
    return "Га-Га"

village = [
    Cow("Манька", 300),
    Goat("Дереза", 60),
    Goat("Копытце", 70),
    Sheep("Барашек", 50),
    Sheep("Кудрявый", 60),
    Chicken("Ко-ко", 1),
    Chicken("Кукареку", 2),
    Goose("Белый", 2),
    Goose("Серый", 3),
    Duck("Кряква", 2),
]

# n = int(input('Введите кол-во корма '))
# m = int(input('Введите кол-во доек '))
# s = int(input('Введите кол-во стрижек '))
# r = int(input('Введите сколько раз неслась курица '))
# for animal in village:
#   if isinstance(animal,Cow):
#     print(f'Наша {animal.name} это {animal.view} она издает звук {animal.makes_sound()}, относится к классу {animal.feature}. После употребления корма  ее вес составил {animal.eat(n)}. {animal.name} подаили и получили {animal.produces(m)} ''\n')
#   if isinstance(animal,Goat):
#     print(f'Наша {animal.name} это {animal.view} она издает звук {animal.makes_sound()}, относится к классу {animal.feature}. После употребления корма  его вес составил {animal.eat(n)}. {animal.name} подаили и получили {animal.produces(m)} ''\n')
#   if isinstance(animal,Sheep):
#     print(f'Наша {animal.name} это {animal.view} она издает звук {animal.makes_sound()}, относится к классу {animal.feature}. После употребления корма  его вес составил {animal.eat(n)}. {animal.name} подстригли и получили {animal.produces(s)} ''\n')
#   if isinstance(animal,Duck):
#     print(f'Наша {animal.name} это {animal.view} она издает звук {animal.makes_sound()}, относится к классу {animal.feature}. После употребления корма  его вес составил {animal.eat(n)}. {animal.name} снесла яйца в колличесве  {animal.produces(r)} ''\n')
#   if isinstance(animal,Chicken):
#     print(f'Наша {animal.name} это {animal.view} она издает звук {animal.makes_sound()}, относится к классу {animal.feature}. После употребления корма  его вес составил {animal.eat(n)}. {animal.name} снесла яйца в колличесве  {animal.produces(r)} ''\n')
#   if isinstance(animal,Goose):
#    print(f'Наша {animal.name} это {animal.view} она издает звук {animal.makes_sound()}, относится к к классу {animal.feature}. После употребления корма  его вес составил {animal.eat(n)}. {animal.name} снесла яйца в колличесве  {animal.produces(r)} ''\n')
#



# Задача 2
"""
Необходимо уметь хранить информацию по альбомам и трекам в них. Это можно сделать, используя классы Album и Track.
У класса Track есть поля:

Название;
Длительность в минутах(используется тип данных int). И метод show, выводящий информацию по треку в виде <Название-Длительность>.
У класса Album есть поля:

Название альбома
Группа
Список треков И три метода:
get_tracks - выводит информацию по всем трекам(используется метод show).
add_track - добавление нового трека в список треков.
get_duration - выводит длительность всего альбома.

Задание №1
Вместо метода show использовать магический метод __str__ у трека для вывода информации по треку.
Пример использования:
print(track1)
Bohemian rhapsody-6min
Задание №2:
У Класса Альбом также реализовать магический метод __str__ для вывода информации по альбому и его треков. 
Пример использования:
print(my_album)
Name group: Queen
Name album: Bohemian rhapsody
Tracks:
	Bohemian rhapsody-6min
	The show must go on-4min

"""

class Track:
 def __init__(self,name,duration):
  self.name = name
  self.duration= duration
 def __str__(self):
  return f'Название песни {self.name}, длительность  - {self.duration} минуты'
 def __repr__(self):
  return f'\n Название песни {self.name}, длительность  - {self.duration} минуты'
 def __lt__(self,other):
     return   self.duration < other.duration

track1 = Track ('Whatever it Takes ', 3)
track2 = Track ('Radioactive ', 4)
print(track1)
print(track2)
print(track1 < track2)

print()

list_song_1 = [
Track('Whatever it Takes ', 3),
Track('Believer', 3)
]

list_song_2 = [
Track('Radioactive ', 4),
Track('Demons', 4),
Track('Warriors', 4)
]

class Album:
 def __init__(self,name_a,group,tracklist):
  self.name_a = name_a
  self.group= group
  self.tracklist= tracklist
 def __str__(self):
     return f'Название группы: {self.group} \n Название альбома: {self.name_a} \n Песни:\n \t {self.tracklist}'
 def __lt__(self,other):
     return   len(self.tracklist) < len(other.tracklist)

first_album = Album('Evolve','Imagine Dragons',list_song_1)
second_album = Album('Night Visions', 'Imagine Dragons', list_song_2)
print(first_album)
print()
print(second_album)
print(first_album < second_album)