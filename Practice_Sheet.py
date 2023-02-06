#전역변수&지역변수

gun = 10


def checkpoint(soldiers):
    global gun
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))


def checkpoint_return(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun


print("전체 총 : {0}".format(gun))
# checkpoint(2)
gun = checkpoint_return(gun, 2)
print("남은 총 : {0}".format(gun))