# Simple python code that rolls two dices and returns a tuple of random values from them

import random
class Dice:
    def roll(self):
        dice_value = random.randint(1,6)
        return dice_value


def returnTuple(dice1,dice2):
    dice_values = (dice1,dice2)
    return dice_values

dice1 = Dice()
dice1_value = dice1.roll()
dice2 = Dice()
dice2_value = dice2.roll()

print(f"Dice values: {returnTuple(dice1_value,dice2_value)}")
    

