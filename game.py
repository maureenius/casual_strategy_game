from enum import IntEnum, auto
from camp import Camp
from map import Map_node

import random, sys

class Game:
    def __init__(self, map_size, num_camp):
        self.turn = 0
        self.action_dict = ["BOOST", "DRAFT", "INVADE"]
        self.entire_map = self.make_entire_map(map_size)
        self.camps = [Camp(i, self.action_dict, money=10000, mil_power=1000) for i in range(num_camp)]
        for i in range(len(self.entire_map)):
            random.choice(self.get_empty_nodes()).ruler = i

    def process(self):
        self.turn += 1
        # ターン開始前処理
        for i in range(len(self.camps)):
            self.camps[i].money += sum([i.prosperity for i in self.get_our_nodes(i)])
        
        for i in range(len(self.camps)):
            choice, target, strength = self.camps[i].action()
            if choice == "BOOST":
                if self.camps[i].spend_money(strength):
                    self.boost(random.choice(self.get_our_nodes(i)), strength)
            elif choice == "DRAFT":
                if self.camps[i].spend_money(strength):
                    self.armament(self.camps[i], strength)
            elif choice == "INVADE":
                self.invade(self.camps[i], self.camps[target])
            else:
                sys.stderr.writelines("存在しないアクションが指定されました：" + str(i))

        return self.isFinished()
    
    def draw(self):
        print(str(self.turn) + "ターン目")
        for i in range(len(self.camps)):
            print("陣営:" + self.camps[i].camp_name + ", 領域:" + str([j.name for j in self.get_our_nodes(i)]) + \
            ", 資金：" + str(round(self.camps[i].money)) + ", 軍事力:" + str(round(self.camps[i].mil_power)) + ", 国力:" + str(round(self.get_sum_prosperity(i))))

    def boost(self, node, money):
        EFFICIENCY = 0.5
        node.prosperity += money * EFFICIENCY
    
    def armament(self, camp, money):
        EFFICIENCY = 1.0
        camp.mil_power += money * EFFICIENCY
    
    def invade(self, attacker, defencer):
        DEF_EFFICIENCY = 2.0

    
    def get_node(self, node_id):
        if node_id >= len(self.entire_map):
            sys.stderr.writelines("存在しないマップノード番号が指定されました:" + str(node_id))
        return self.entire_map[node_id]
    
    def get_our_nodes(self, camp_id):
        return [i for i in self.entire_map if i.ruler == camp_id]
    
    def get_empty_nodes(self):
        return [i for i in self.entire_map if i.ruler == None]
    
    def get_sum_prosperity(self, camp_id):
        return sum([i.prosperity for i in self.get_our_nodes(camp_id)])

    def make_entire_map(self, map_size):
        answer = [Map_node(i) for i in range(map_size)]
        # 暫定的に環状のネットワークを作成する
        for i in range(map_size):
            if i < map_size-1:
                answer[i].neighbor_nodes.append(answer[i+1])
                answer[i+1].neighbor_nodes.append(answer[i])
            else:
                answer[i].neighbor_nodes.append(answer[0])
                answer[0].neighbor_nodes.append(answer[i])
        return answer

    def isFinished(self):
        return self.turn >= 10
    
    def who_is_strongest(self):
        return max([i.mil_power for i in self.camps])
