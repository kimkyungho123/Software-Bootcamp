def fibo_recu(n) :
	if n == 0 :
		return 0
	elif n == 1 :
		return 1
	else :
		return fibo_recu(n-1) + fibo_recu(n-2)


def fibo_iteration(n):
    r = list()
    p1, p2 = 1, 2
    for _ in range(n):
        r.append(p1)
        p1, p2 = p2, p1 + p2
    return r[-1]


print('피보나치 수 --> 0 1 ', end='')
for i in range(2, 40) :
	print(f'{i} : {fibo_iteration(i)}') #repetition
    # print(f'{i} : {fibo_recu(i)}') #recurtion
