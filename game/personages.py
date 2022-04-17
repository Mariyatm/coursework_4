from abc import  ABC

from game.skills import Skill, ferecious_kick, powerful_thust


class Personage(ABC):
    name: str = NotImplemented
    max_health: float = NotImplemented
    max_stamina: float = NotImplemented
    stamina: float = NotImplemented
    attack: float = NotImplemented
    armor: float = NotImplemented
    skill: Skill = NotImplemented

class Warrior(Personage):
    name = 'Воин'
    max_health = 60.0
    max_stamina = 30.0
    stamina = 0.9
    attack = 0.8
    armor = 1.2
    skill = ferecious_kick

class Thief(Personage):
    name = 'Вор'
    max_health = 50.0
    max_stamina = 25.0
    stamina = 1.2
    attack = 1.5
    armor = 1.0
    skill = powerful_thust
