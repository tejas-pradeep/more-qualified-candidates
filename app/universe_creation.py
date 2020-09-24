"""Universe Creation"""
import random
from enum import Enum


class Game:
    """Game class"""

    def __init__(self, player, difficulty):
        self.player = player
        self.difficulty = difficulty.capitalize()

    def start_game(self):
        """Start Game"""
        self.player.region = Universe.regions()[0]
        self.special_region = Universe.regions()[2].name
        print('BLEACHER' + Universe.regions()[2].name)
        self.player.ship = Ship('Explorer')
        for region in Universe.regions():
            region.market.calculate_prices(self.player.merchant_points)

    def update(self):
        """Update Game"""


class TechLevel(Enum):
    """Tech Level enum"""
    NOMADIC = ("Nomadic", 0)
    AGRICULTURE = ("Agricultural", 1)
    MEDIEVAL = ("Medieval", 2)
    RENAISSANCE = ("Renaissance Period", 3)
    INDUSTRIAL = ("Industrial", 4)
    MODERN = ("Modern", 5)
    FUTURISTIC = ("Futuristic", 6)


class Region:
    """Region class"""

    def __init__(self, x_coordinate, y_coordinate, tech_level, name):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.tech_level = tech_level
        self.name = name
        self.market = Market(self)


class Universe:
    """Universe class"""
    __instance = None
    __regions = []

    @staticmethod
    def get_instance():
        """Get Instance"""
        region_names = ["Sombrero Galaxy", "Milky Way", "Andromeda", "Messier 81",
                        "Black Eye", "Cigar Galaxy", "Whirpool Galaxy", "Tadpole Galaxy",
                        "Cartwheel Galaxy", "Butterfly Galaxy"]
        return Universe(region_names).__instance

    @staticmethod
    def regions():
        """Regions"""
        return Universe.__regions

    def __init__(self, region_names):
        if Universe.__instance is not None:
            Universe.__regions = []
            for i in range(10):
                x_coordinate = random.randrange(401) - 200
                y_coordinate = random.randrange(401) - 200
                for j in range(len(Universe.__regions)):
                    while abs(Universe.__regions[j].x_coordinate - x_coordinate) < 15:
                        x_coordinate = random.randrange(401) - 200
                        j = 0
                    while abs(Universe.__regions[j].y_coordinate - y_coordinate) < 15:
                        y_coordinate = random.randrange(401) - 200
                        j = 0
                tech_level = random.choice(list(TechLevel))
                name = region_names.pop(random.randrange(len(region_names)))
                Universe.__regions.append(Region(x_coordinate, y_coordinate, tech_level, name))
        Universe.__instance = self


class Player:
    """Player class"""

    def __init__(self, name, difficulty, pilot_points,
                 fighter_points, merchant_points, engineer_points):
        self.name = name.capitalize()
        if difficulty == 'easy':
            self.credits = 1600
        elif difficulty == 'normal':
            self.credits = 1200
        else:
            self.credits = 800
        self.pilot_points = float(pilot_points)
        self.fighter_points = float(fighter_points)
        self.merchant_points = float(merchant_points)
        self.engineer_points = float(engineer_points)
        self.currency = (random.randint(50, 75) / 100) * self.credits
        self.region = None
        self.ship = None
        self.inventory = []
        self.karma = 0

    def get_market(self):
        """Get Market"""
        return self.region.market

    def get_market_listings(self):
        """Get Market Listings"""
        return self.get_market().market_list

    def buy(self, item):
        """Buy"""
        self.get_market().buy(self, self.credits, item)


class Ship:
    """Ship class"""

    def __init__(self, name):
        self.name = name
        self.cargo_max = 50
        self.fuel_max = 1000
        self.health_max = 100
        self.current_cargo = 0
        self.current_fuel = 1000
        self.current_health = 100

    def upgrade(self, cargo_max, fuel_max, health_max):
        """Upgrade"""
        self.cargo_max = cargo_max
        self.fuel_max = fuel_max
        self.health_max = health_max

    def add_cargo(self, cargo):
        """Add Cargo"""
        if self.current_cargo + cargo > self.cargo_max:
            self.current_cargo = self.cargo_max
        else:
            self.current_cargo += cargo

    def add_fuel(self, fuel):
        """Add Fuel"""
        if self.current_fuel + fuel > self.fuel_max:
            self.current_fuel = self.fuel_max
        else:
            self.current_fuel += fuel

    def add_health(self, health):
        """Add Health"""
        if self.current_health + health > self.health_max:
            self.current_health = self.health_max
        else:
            self.current_health += health


# In the front end each region has a market, and the front end must show the item list.
# The player once he chooses an item, the buy method in market is called,
# and if the 'if' fails, the player cant buy it and a message must be displayed.
class Market:
    """Market Class"""

    def __init__(self, region):
        self.region = region
        market_dic = {'Bread': [10, 10], 'Apples': [5, 5], 'Orange': [4, 4], 'Penicilin': [15, 15],
                      'Gold': [20, 20], 'Wood': [5, 5], 'Iron sword': [17, 17],
                      'Chestplate': [25, 25], 'Boots': [10, 10],
                      'Helmet': [12, 12], 'Plough': [7, 7],
                      'Rice': [3, 3]}
        if region.tech_level.value[1] > 3:
            market_dic['Computer'] = [region.tech_level.value[1] * 8,
                                      region.tech_level.value[1] * 8]
        if region.tech_level.value[1] > 5:
            market_dic['Mobile'] = [region.tech_level.value[1] * 7, region.tech_level.value[1] * 7]
        self.market_list = market_dic
        for i, j in self.market_list.items():
            self.market_list[i][0] *= random.randint(0, 100) / 100 + 1

    # if player cant buy it as in cargo is not enough or credits aren't enough display a message

    def buy(self, player, item):
        """Buy"""
        if player.ship.current_cargo + 1 <= player.ship.cargo_max \
                and (player.currency - self.market_list[item][0] > 0):
            player.currency -= self.market_list[item][0]
            player.currency = round(player.currency, 2)
            player.ship.current_cargo += 1
            player.inventory.append(item)

    def sell(self, player, item):
        """Sell"""
        if player.ship.current_cargo - 1 >= 0 and item in player.inventory:
            player.currency += self.market_list[item][1]
            player.currency = round(player.currency, 2)
            player.ship.current_cargo -= 1
            player.inventory.remove(item)

    def calculate_prices(self, merchant_skill):
        """Calculate Prices"""
        self.__init__(self.region)
        for i, j in self.market_list.items():
            if self.market_list[i][0] - merchant_skill >= 0:
                self.market_list[i][0] -= merchant_skill / 2
            else:
                self.market_list[i][0] = 1.00
            self.market_list[i][0] = round(self.market_list[i][0], 2)
            self.market_list[i][1] = round(self.market_list[i][0] * 0.88, 2)


class NPC:
    """NPC"""
    def __int__(self, npctype):
        self.npc = npctype

    def interact(self, player, interaction_type):
        """Interact Method"""
        self.npc.interact(player, interaction_type)


class Bandit(NPC):
    """Bandit"""
    def __init__(self):
        self.damage = random.randint(0, 30)
        self.health = random.randint(0, 5)
        self.credits = random.randint(0, 300)
        self.fly = random.randint(0, 5)
        self.inventory = []
        self.credit_demand = random.randint(10, 100)

    def interact(self, player, interaction_type):
        """Interact Method"""
        # implement some way to link a variable form frontend to here
        # display this credit demand when the first interaction is chosen
        if interaction_type == 1:
            if player.currency < self.credit_demand:
                if not player.inventory:
                    player.ship.current_health -= self.damage
                else:
                    self.inventory = player.inventory
                    player.inventory = []
            else:
                player.currency -= self.credit_demand
                self.credit_demand += self.credit_demand
        if interaction_type == 2:
            if not random.randint(0, player.pilot_points) > random.randint(0, self.fly):
                self.credits = player.currency
                player.currency = 0
                player.ship.current_health -= self.damage
                # implement way to cancel the travel.
        else:
            if random.randint(0, player.fighter_points) > random.randint(0, self.health):
                player.currency += random.randint(0, int(self.credits / 25))
            else:
                # implement cancel travel
                self.credits += player.currency
                player.currency = 0
                player.ship.current_health -= self.damage


class Police(NPC):
    """Police"""
    def __init__(self):
        self.items = []
        self.damage = random.randint(0, 40)
        self.health = random.randint(0, 7)
        self.fly = random.randint(0, 6)
        self.credits = random.randint(0, 100)

    def interact(self, player, interaction_type):
        """Interact Method"""
        # cancel the interaction if player does not have any items.
        if not player.inventory:
            pass
        if interaction_type == 1:
            temp_lis = []
            for i in range(random.randint(0, len(player.inventory)) + 1):
                j = random.randint(0, i)
                if j not in temp_lis:
                    temp_lis.append(j)
            for i in temp_lis:
                self.items.append(player.inventory[i])
                del player.inventory[i]
        if interaction_type == 2:
            if interaction_type == 2:
                if not random.randint(0, player.pilot_points) > self.fly:
                    for i in range(random.randint(0, len(player.inventory)) + 1):
                        j = random.randint(0, i)
                        if j not in temp_lis:
                            temp_lis.append(j)
                    for i in temp_lis:
                        self.items.append(player.inventory[i])
                        del player.inventory[i]
                    player.ship.current_health -= self.damage
                    fine = int(random.random() * self.credits)
                    player.currency -= fine
                    self.credits += fine
                    player.karma -= 1
                    # implement way to cancel the travel.
        else:
            if not random.randint(0, player.fighter_points) > random.randint(0, self.health):
                for i in range(random.randint(0, len(player.inventory)) + 1):
                    j = random.randint(0, i)
                    if j not in temp_lis:
                        temp_lis.append(j)
                    for i_item in temp_lis:
                        self.items.append(player.inventory[i_item])
                        del player.inventory[i_item]
                    player.ship.current_health -= self.damage
                    fine = int(random.random() * self.credits)
                    player.currency -= fine
                    self.credits += fine


class Trader(NPC):
    """Trader"""
    def __init__(self):
        self.damage = random.randint(0, 20)
        self.health = random.randint(0, 5)
        self.credits = random.randint(0, 350)
        self.inventory = []
        trader_dic = {'Bread': [10, 10], 'Apples': [5, 5], 'Orange': [4, 4], 'Penicillin': [15, 15],
                      'Gold': [20, 20], 'Wood': [5, 5], 'Iron Sword': [17, 17],
                      'Chestplate': [25, 25], 'Boots': [10, 10],
                      'Helmet': [12, 12], 'Plough': [7, 7],
                      'Rice': [3, 3], 'Computer': [25, 25], 'Mobile': [20, 20]}
        for i, j in trader_dic.items():
            trader_dic[i][1] *= random.randint(0, 100) / 100 + 1
        self.item = random.choice(list(trader_dic.keys()))
        self.item_price = trader_dic[self.item][0]
        self.item_sell = trader_dic[self.item][1]
        self.amount = random.randint(1, 4)

    def interact(self, player, interaction_type):
        """Interact Method"""
        if interaction_type == 1:
            if player.ship.current_cargo + self.amount <= player.ship.cargo_max \
                    and (player.currency - self.amount * self.item_price > 0):
                player.currency -= self.amount * self.item_price
                player.currency = round(player.currency, 2)
                player.ship.current_cargo += self.amount
                for x_items in range(self.amount):
                    player.inventory.append(self.item)
        if interaction_type == 2:
            pass
        if interaction_type == 3:
            if random.randint(0, player.fighter_points + 1) > random.randint(0, self.health):
                if player.ship.current_cargo + self.amount <= player.ship.cargo_max:
                    for x_items in range(self.amount):
                        player.inventory.append(self.item)
            else:
                # implement cancel travel
                player.ship.current_health -= self.damage
            player.karma -= 1
        if interaction_type == 4:
            if random.randint(0, player.merchant_points + 1) > random.randint(0, self.health):
                self.item_price = self.item_price - 1 *\
                                  player.merchant_points if self.item_price - 1 *\
                                                            player.merchant_points > 0 else 0
