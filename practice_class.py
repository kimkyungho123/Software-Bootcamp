class unit:
    def __init__(self):
        print("unit 생성자")


class flyable:
    def __init__(self):
        print("flyable 생성자")


class flyable_unit(flyable, unit):
    def __init__(self):
        #super().__init__()
        unit.__init__(self)
        flyable.__init__(self)


dropship = flyable_unit()