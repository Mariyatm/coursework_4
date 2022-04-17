from dataclasses import dataclass


@dataclass
class Skill:
    name: str
    damage: int
    stamina: int


ferecious_kick = Skill(name='Свирепый пинок', damage=12, stamina=6)
powerful_thust = Skill(name='Мощный укол', daamage=15, stamina=5)
