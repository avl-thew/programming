from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum, StrEnum, unique
from random import randint, choice


@unique
class DamageType(StrEnum):
    PHYSICAL = "🗡️"
    FIRE = "🔥"
    ICE = "🧊"
    LIGHTNING = "⚡"
    POISON = "💀"
    HEALING = "❤️"


@unique
class DamageRange(Enum):
    MELEE = 0
    RANGE = 1


@dataclass
class Skill:
    name: str
    type: DamageType
    range: DamageRange
    damage: int = 0


class Character(ABC):
    classname = None

    @abstractmethod
    def __init__(self, name=None):
        self.name = name
        self._health = 100
        self._mana = 100
        self._resist = None
        self._skills = ()
        self._attack_var_percent = 20


    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        if value > 100:
            self._health = 100
        else:
            self._health = value if value > 0 else 0

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, value):
        if value > 100:
            self._mana = 100
        else:
            self._mana = value if value > 0 else 0
    
    def attack(self):
        picked_skill = Skill(**choice(self._skills).__dict__)
        damage_change = picked_skill.damage * randint(-self._attack_var_percent,
            self._attack_var_percent) / 100
        picked_skill.damage += int(damage_change)
        return picked_skill

    def __str__(self):
        return f"{self.classname} {self.name} 🔴{self.health} 🔵{self.mana}"

    def __repr__(self):
        return str(self)
class Rus(Character):
    classname = "Рус"

    def __init__(self, name):
        super().__init__(name)
        self._skills = (
            Skill(
                "Славянский прострел сундука",
                DamageType.PHYSICAL,
                DamageRange.RANGE,
                15,
            ),
            Skill(
                "Древнерусский удар с вертушки",
                DamageType.PHYSICAL,
                DamageRange.RANGE,
                20,
            ),
            Skill(
                "Бахнул воды байкальской и погнал",
                DamageType.HEALING,
                DamageRange.MELEE,
                10,
            ),
        )

class Lizard(Character):
    classname = "Ящер"

    def __init__(self, name):
        super().__init__(name)
        self._skills = (
            Skill(
                "Ящерский удар хвостом",
                DamageType.PHYSICAL,
                DamageRange.MELEE,
                15,
            ),
            Skill(
                "Отравленная чешуя",
                DamageType.POISON,
                DamageRange.MELEE,
                20,
            ),
            Skill(
                "Взрыв Гипербореи",
                DamageType.FIRE,
                DamageRange.RANGE,
                25,
            ),
        )