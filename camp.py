import random

class Camp:
    def __init__(self, camp_id, action_dict, name="", money=0, mil_power=0):
        self.camp_id = camp_id
        self.action_dict = action_dict
        if name == "":
            self.camp_name = str(self.camp_id)
        else:
            self.camp_name = name
        self.money = money
        self.mil_power = mil_power
    
    def action(self):
        act_kind = random.choice(self.action_dict)
        if act_kind != "INVADE":
            target = 0
        else:
            target = random.randint(0,2)
        strength = self.money * 0.5

        return act_kind, target, strength
    
    def spend_money(self, amount):
        if amount > self.money:
            return False
        self.money -= amount
        return True
        