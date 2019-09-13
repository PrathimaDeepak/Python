import random

class Coin:
    def __init__(self, rare=False, clean=True, heads=True, **kwargs):
        for key,value in kwargs.items():
            setattr(self, key, value)
       
        self.is_rare = rare
        self.is_clean = clean
        self.heads=heads
        if self.is_rare:
            self.value = self.original_value * 1.25
        else:
            self.value = self.original_value
        if self.is_clean:
            self.colour = self.clean_colour
        else:
            self.colour = self.rusty_colour

    def rust(self):
        self.colour = self.rusty_colour

    def clean(self):
        self.colour = self.clean_colour

    def __del__(self):
        print("Coin spent")

    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice

    def __str__(self):
        if self.original_value >= 1.00:
            return "£{} coin".format(int(self.original_value))
        else:
            return "{}p coin".format(int(self.original_value *100))
            
class One_pence(Coin):
    def __init__(self):
        data = {
            "original_value" : 0.01,
            "clean_colour" : "bronze",
            "rusty_colour" : "grey",
            "num_edges" : 1,
            "diameter" : 20.3,
            "thickness" : 1.52,
            "mass" : 3.56
            }
        super().__init__(**data)

class Two_pence(Coin):
    def __init__(self):
        data = {
            "original_value" : 0.02,
            "clean_colour" : "bronze",
            "rusty_colour" : "grey",
            "num_edges" : 1,
            "diameter" : 25.9,
            "thickness" : 1.85,
            "mass" : 7.12
            }
        super().__init__(**data)

class Five_pence(Coin):
    def __init__(self):
        data = {
            "original_value" : 0.05,
            "clean_colour" : "silver",
            "rusty_colour" : None,
            "num_edges" : 1,
            "diameter" : 18.0,
            "thickness" : 1.77,
            "mass" : 3.25
            }
        super().__init__(**data)

    def rust(self):
        self.colour = self.clean_colour

class Ten_pence(Coin):
    def __init__(self):
        data = {
            "original_value" : 0.10,
            "clean_colour" : "silver",
            "rusty_colour" : None,
            "num_edges" : 1,
            "diameter" : 24.0,
            "thickness" : 1.85,
            "mass" : 6.50
            }
        super().__init__(**data)

    def rust(self):
        self.colour = self.clean_colour

class Twenty_pence(Coin):
    def __init__(self):
        data = {
            "original_value" : 0.20,
            "clean_colour" : "silver",
            "rusty_colour" : None,
            "num_edges" : 1,
            "diameter" : 24.0,
            "thickness" : 1.85,
            "mass" : 6.50
            }
        super().__init__(**data)

    def rust(self):
        self.colour = self.clean_colour

class Fifty_pence(Coin):
    def __init__(self):
        data = {
            "original_value" : 0.50,
            "clean_colour" : "silver",
            "rusty_colour" : None,
            "num_edges" : 1,
            "diameter" : 24.0,
            "thickness" : 1.85,
            "mass" : 6.50
            }
        super().__init__(**data)

    def rust(self):
        self.colour = self.clean_colour

class Pound(Coin):
    def __init__(self):
        data = {
            "original_value" : 1.00,
            "clean_colour" : "gold",
            "rusty_colour" : "brown",
            "num_edges" : 1,
            "diameter" : 22.5,
            "thickness" : 3.15,
            "mass" : 9.5
            }
        super().__init__(**data)


class Two_Pound(Coin):
    def __init__(self):
        data = {
            "original_value" : 2.00,
            "clean_colour" : "gold",
            "rusty_colour" : "brown",
            "num_edges" : 1,
            "diameter" : 22.5,
            "thickness" : 3.15,
            "mass" : 9.5
            }
        super().__init__(**data)


coins = [One_pence(), Two_pence(), Five_pence(), Ten_pence(), Twenty_pence(),
         Fifty_pence(), Pound(), Two_Pound()]

for coin in coins:
    arguments = [coin, coin.colour, coin.value, coin.diameter, coin.thickness,
                 coin.num_edges, coin.mass]

    string = "{} -  colour: {}, value: {}, diameter: {}, thickness: {}, number of edges: {}, mass: {}".format(*arguments)
    print(string)
    
