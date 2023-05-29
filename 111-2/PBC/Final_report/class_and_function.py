import time 
import random

def random_number(a,b):
    return random.randint(a,b)

def random_weather(weather):
    return random.choice(weather)

def print_with_delay(text, delay):
    for char in text:
        print(char, end='', flush=True)  
        time.sleep(delay)
    return print()

class water:
    def __init__(self,quantity):
        self.quantity = quantity
    def add_water(self,amount):
        self.quantity = self.quantity + amount
    def consume_water(self,amount):
        if self.quantity >= amount:
            self.quantity = self.quantity - amount
        else:
            print('You don\'t have enough water!')
    def get_quantity(self):
        return self.quantity
    
class food:
    def __init__(self,quantity):
        self.quantity = quantity
    def add_food(self,amount):
        self.quantity = self.quantity + amount
    def consume_food(self,amount):
        if self.quantity >= amount:
            self.quantity = self.quantity - amount
        else:
            print('You don\'t have enough food!')
    def get_quantity(self):
        return self.quantity

class material:
    def __init__(self,quantity):
        self.quantity = quantity
    def add_material(self,amount):
        self.quantity = self.quantity + amount
    def consume_material(self,amount):
        if self.quantity >= amount:
            self.quantity = self.quantity - amount
        else:
            print('You don\'t have enough material!')
    def get_quantity(self):
        return self.quantity

class medkit:
    def __init__(self,quantity):
        self.quantity = quantity
    def add_medkit(self,amount):
        self.quantity = self.quantity + amount
    def consume_medkit(self,amount):
        if self.quantity >= amount:
            self.quantity = self.quantity - amount
        else:
            print('You don\'t have enough medkit!')
    def get_quantity(self):
        return self.quantity