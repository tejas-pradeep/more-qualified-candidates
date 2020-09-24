"""Trading Class"""
import random
from .universe_creation import TechLevel


class Market:
    """Market class"""
    def __init__(self, techlevel):
        self.items = self.create_items(techlevel)

    def create_items(self, techlevel):
        """Create Items"""
        items = []
        for i in range(10):
            random_int = random.randint(0, 100)
            if random_int >= 90:
                items[i] = FoodItem(techlevel)
            elif random_int >= 75:
                items[i] = TechItem(techlevel)
            elif random_int >= 60:
                items[i] = WeaponItem(techlevel)
            elif random_int >= 50:
                items[i] = ClothingItem(techlevel)
            elif random_int >= 45:
                items[i] = EntertainmentItem(techlevel)
            elif random_int >= 43:
                items[i] = RareItem(techlevel)
            elif random_int >= 38:
                items[i] = UpgradeItem(techlevel)
            elif random_int >= 28:
                items[i] = FuelItem(techlevel)
            elif random_int >= 14:
                items[i] = MaterialItem(techlevel)
            else:
                items[i] = LootItem(techlevel)
        return items


class Item:
    """Item class"""
    def __init__(self, name, desc, price):
        self.name = name
        self.desc = desc
        self.price = price


class TechItem(Item):
    """TechItem class"""
    def __init__(self, techlevel):
        if techlevel == TechLevel.NOMADIC:
            pass
        elif techlevel == TechLevel.AGRICULTURE:
            pass
        elif techlevel == TechLevel.MEDIEVAL:
            pass
        elif techlevel == TechLevel.RENAISSANCE:
            pass
        elif techlevel == TechLevel.INDUSTRIAL:
            pass
        elif techlevel == TechLevel.MODERN:
            pass
        else:
            pass


class FoodItem(Item):
    """FoodItem class"""
    def __init__(self, techlevel):
        if techlevel == TechLevel.NOMADIC:
            pass
        elif techlevel == TechLevel.AGRICULTURE:
            pass
        elif techlevel == TechLevel.MEDIEVAL:
            pass
        elif techlevel == TechLevel.RENAISSANCE:
            pass
        elif techlevel == TechLevel.INDUSTRIAL:
            pass
        elif techlevel == TechLevel.MODERN:
            pass
        else:
            pass


class WeaponItem(Item):
    """Weapon Items"""
    def __init__(self, techlevel):
        if techlevel == TechLevel.NOMADIC:
            pass
        elif techlevel == TechLevel.AGRICULTURE:
            pass
        elif techlevel == TechLevel.MEDIEVAL:
            pass
        elif techlevel == TechLevel.RENAISSANCE:
            pass
        elif techlevel == TechLevel.INDUSTRIAL:
            pass
        elif techlevel == TechLevel.MODERN:
            pass
        else:
            pass


class ClothingItem(Item):
    """Clothing Items"""
    def __init__(self, techlevel):
        if techlevel == TechLevel.NOMADIC:
            pass
        elif techlevel == TechLevel.AGRICULTURE:
            pass
        elif techlevel == TechLevel.MEDIEVAL:
            pass
        elif techlevel == TechLevel.RENAISSANCE:
            pass
        elif techlevel == TechLevel.INDUSTRIAL:
            pass
        elif techlevel == TechLevel.MODERN:
            pass
        else:
            pass


class EntertainmentItem(Item):
    """Entertainment Items"""
    def __init__(self, techlevel):
        if techlevel == TechLevel.NOMADIC:
            pass
        elif techlevel == TechLevel.AGRICULTURE:
            pass
        elif techlevel == TechLevel.MEDIEVAL:
            pass
        elif techlevel == TechLevel.RENAISSANCE:
            pass
        elif techlevel == TechLevel.INDUSTRIAL:
            pass
        elif techlevel == TechLevel.MODERN:
            pass
        else:
            pass


class RareItem(Item):
    """Rare Items"""
    def __init__(self, techlevel):
        if techlevel == TechLevel.NOMADIC:
            pass
        elif techlevel == TechLevel.AGRICULTURE:
            pass
        elif techlevel == TechLevel.MEDIEVAL:
            pass
        elif techlevel == TechLevel.RENAISSANCE:
            pass
        elif techlevel == TechLevel.INDUSTRIAL:
            pass
        elif techlevel == TechLevel.MODERN:
            pass
        else:
            pass


class UpgradeItem(Item):
    """Upgrade Items"""
    def __init__(self, techlevel):
        if techlevel == TechLevel.NOMADIC:
            pass
        elif techlevel == TechLevel.AGRICULTURE:
            pass
        elif techlevel == TechLevel.MEDIEVAL:
            pass
        elif techlevel == TechLevel.RENAISSANCE:
            pass
        elif techlevel == TechLevel.INDUSTRIAL:
            pass
        elif techlevel == TechLevel.MODERN:
            pass
        else:
            pass


class FuelItem(Item):
    """Fuel Items"""
    def __init__(self, techlevel):
        if techlevel == TechLevel.NOMADIC:
            pass
        elif techlevel == TechLevel.AGRICULTURE:
            pass
        elif techlevel == TechLevel.MEDIEVAL:
            pass
        elif techlevel == TechLevel.RENAISSANCE:
            pass
        elif techlevel == TechLevel.INDUSTRIAL:
            pass
        elif techlevel == TechLevel.MODERN:
            pass
        else:
            pass


class MaterialItem(Item):
    """Material Items"""
    def __init__(self, techlevel):
        if techlevel == TechLevel.NOMADIC:
            pass
        elif techlevel == TechLevel.AGRICULTURE:
            pass
        elif techlevel == TechLevel.MEDIEVAL:
            pass
        elif techlevel == TechLevel.RENAISSANCE:
            pass
        elif techlevel == TechLevel.INDUSTRIAL:
            pass
        elif techlevel == TechLevel.MODERN:
            pass
        else:
            pass


class LootItem(Item):
    """Loot Items"""
    def __init__(self, techlevel):
        if techlevel == TechLevel.NOMADIC:
            pass
        elif techlevel == TechLevel.AGRICULTURE:
            pass
        elif techlevel == TechLevel.MEDIEVAL:
            pass
        elif techlevel == TechLevel.RENAISSANCE:
            pass
        elif techlevel == TechLevel.INDUSTRIAL:
            pass
        elif techlevel == TechLevel.MODERN:
            pass
        else:
            pass
