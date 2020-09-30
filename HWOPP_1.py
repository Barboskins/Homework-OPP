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
Нужно реализовать классы животных и определить методы взаимодействия с животными.
Для каждого животного из списка должен существовать экземпляр класса.
Каждое животное требуется накормить и подоить/постричь/собрать яйца, если надо.

Задание 2:
У каждого животного должно быть определено имя(self.name) и вес(self.weight).
Необходимо посчитать общий вес всех животных(экземпляров класса);
Вывести название самого тяжелого животного.
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
class Animals_milking(Artiodactyls):
  milk =0
  def produces(self, quantity_milkings):
    self.milk += quantity_milkings * 10
    return  f"{self.milk} литров молока"
class Animal_wool(Artiodactyls):
  wool = 0
  def produces(self, quantity_wool):
    self.wool += quantity_wool*5
    return f"{self.wool} килограмм шерсти"
class Birds_eggs(Birds):
  egg = 0
  def produces(self, number_times):
    self.egg += number_times*10
    return f"{self.egg} яиц"
class Cow(Animals_milking):
  view = "Корова"
  def makes_sound(self):
    return "Мууууу"
class Goat(Animals_milking):
  view = "Коза"
  def makes_sound(self):
    return "Беееее"
class Sheep (Animal_wool):
  view = "Овца"
  def makes_sound(self):
    return "Мееее"
class Duck (Birds_eggs):
  view = "Утка"
  def makes_sound(self):
    return "Кря-Кря"
class Chicken (Birds_eggs):
  view = "Курица"
  def makes_sound(self):
    return "Курлык"
class Goose (Birds_eggs):
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

n = int(input('Введите кол-во корма '))
m = int(input('Введите кол-во доек '))
s = int(input('Введите кол-во стрижек '))
r = int(input('Введите сколько раз неслась курица '))
for animal in village:
  if isinstance(animal,Cow):
    print(f'Наша {animal.name} это {animal.view} она издает звук {animal.makes_sound()}, относится к классу {animal.feature}. После употребления корма  ее вес составил {animal.eat(n)}. {animal.name} подаили и получили {animal.produces(m)} ''\n')
  if isinstance(animal,Goat):
    print(f'Наша {animal.name} это {animal.view} она издает звук {animal.makes_sound()}, относится к классу {animal.feature}. После употребления корма  его вес составил {animal.eat(n)}. {animal.name} подаили и получили {animal.produces(m)} ''\n')
  if isinstance(animal,Sheep):
    print(f'Наша {animal.name} это {animal.view} она издает звук {animal.makes_sound()}, относится к классу {animal.feature}. После употребления корма  его вес составил {animal.eat(n)}. {animal.name} подстригли и получили {animal.produces(s)} ''\n')
  if isinstance(animal,Duck):
    print(f'Наша {animal.name} это {animal.view} она издает звук {animal.makes_sound()}, относится к классу {animal.feature}. После употребления корма  его вес составил {animal.eat(n)}. {animal.name} снесла яйца в колличесве  {animal.produces(r)} ''\n')
  if isinstance(animal,Chicken):
    print(f'Наша {animal.name} это {animal.view} она издает звук {animal.makes_sound()}, относится к классу {animal.feature}. После употребления корма  его вес составил {animal.eat(n)}. {animal.name} снесла яйца в колличесве  {animal.produces(r)} ''\n')
  if isinstance(animal,Goose):
   print(f'Наша {animal.name} это {animal.view} она издает звук {animal.makes_sound()}, относится к к классу {animal.feature}. После употребления корма  его вес составил {animal.eat(n)}. {animal.name} снесла яйца в колличесве  {animal.produces(r)} ''\n')

def max_weight_ (sum_weight,max_weight):
  for animal in village:
    sum_weight+= animal.weight
    if animal.weight > max_weight:
         max_weight = animal.weight
  return f'Общий вес всех животных {sum_weight}. Самое тяжелое животное весит {max_weight}'

print(max_weight_(0,0))


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
Задание:
Создать 2 альбома с 3 треками. Для каждого вывести его длительность.

"""

class Track:
 def __init__(self,name,duration):
  self.name = name
  self.duration= duration
 def show(self):
  return f'Название песни {self.name}, длительность  - {self.duration} минуты'

list_song_1 = [
Track('Whatever it Takes ', 3),
Track('Believer', 3),
Track('Thunder', 3)
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
 def get_track(self):
  track_list=''
  for track in self.tracklist:
    track_list += track.show() + '\n'
  return (track_list)
 def add_tracks(self,song):
  track_name, duration = song
  track = Track(track_name, duration)
  self.tracklist.append(track)
  return  self.tracklist
 def get_duration(self):
  sum_time = 0
  for track in self.tracklist:
   sum_time += track.duration
  return f'Длительность всего альбома составляет {sum_time} минут'

first_album = Album('Evolve','Imagine Dragons',list_song_1)
second_album = Album('Night Visions', 'Imagine Dragons', list_song_2)



print(first_album.add_tracks(('Natural',3)))
print (first_album.get_track())
print (first_album.get_duration())

print(second_album.add_tracks(('Sucker for Pain',4)))
print (second_album.get_track())
print (second_album.get_duration())
