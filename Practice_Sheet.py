# Method Overriding
# Pass
class unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

class attack_unit(unit):
    def __init__(self, name, hp, speed, damage):
        unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


class flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))


class flyable_attack_unit(attack_unit, flyable):
    def __init__(self, name, hp, damage, flying_speed):
        attack_unit.__init__(self, name, hp, 0, damage) # 지상 speed = 0
        flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)


vulture = attack_unit("벌쳐", 80, 10, 20)

BatttleCruiser = flyable_attack_unit("배틀크루저", 500, 25, 3)

vulture.move("11시")
BatttleCruiser.fly(BatttleCruiser.name, "9시")

BatttleCruiser.move("9시")

#-----------------------------------------------------

class building_unit(unit):
    def __init__(self, name, hp, location):
        pass


supply_depot = building_unit("서플라이 디폿", 500, "7시")


def game_start_():
    print("[알림] 새로운 게임을 시작합니다.")


def game_over():
    pass


game_start_()
game_over()