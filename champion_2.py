class Champion:
    def __init__(self,name):
        self.name=name
    def cham_info(self):
        print('-'*17,"현재",self.name,"의 정보",'-'*17)
        HP=1000
        print("체력 :",HP,",회복 :",15,",속도 :",300)

class Attack(Champion):
    def __init__(self,name,attack_cham,attack):
        self.name=name
        self.attack_cham=attack_cham
        self.attack=attack
    def attack(self):
        print("#"*9,self.name,"이(가)",self.attack_cham,"을",self.attack,"만큼 피해를 입혔습니다!","#"*9)

