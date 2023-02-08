# Linear List

friends = ["Chandler", "Joy", "Ross", "Rachel", "Phoebe"]


def insert_data(position, friend):

    if position < 0 or position >= len(friends):
        print("Out of range!")
        return

    friends.append(None)
    f_len = len(friends)

    for i in range(f_len-1, position, -1):
        friends[i] = friends[i-1]
        friends[i-1] = None

    friends[position] = friend


insert_data(3, "Monica")
print(friends)