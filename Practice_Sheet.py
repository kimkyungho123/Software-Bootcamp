# real estate example

class house:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)


House = []
House1 = house("강남", "아파트", "매매", "10억", "2010년")
House2 = house("마포", "오피스텔", "전세", "5억", "2007년")
House3 = house("송파", "빌라", "월세", "500/50", "2000년")
House.append(House1)
House.append(House2)
House.append(House3)

print("총 {0}대의 매물이 있습니다.".format(len(House)))
for house in House:
    house.show_detail()
