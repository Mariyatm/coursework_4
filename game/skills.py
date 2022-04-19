from dataclasses import dataclass


@dataclass
class Skill:
    name: str
    damage: float
    stamina: float


ferecious_kick = Skill(name='Свирепый пинок', damage=12, stamina=6)
powerful_thust = Skill(name='Мощный укол', damage=15, stamina=5)
