class node():
    def __init__(self):
        self.data = None
        self.link = None


node1 = node()
node1.data = "피카츄"
node1.link = node1

node2 = node()
node2.data = "라이츄"
node1.link = node2
node2.link = node1

node3 = node()
node3.data = "꼬북이"
node2.link = node3
node3.link = node1

node4 = node()
node4.data = "파이리"
node3.link = node4
node4.link = node1

node5 = node()
node5.data = "야도란"
node4.link = node5
node5.link = node1

new_node = node()
new_node.data = "이상해씨"
new_node.link = node2.link
node2.link = new_node

node2.link = node3.link
del node3

current = node1
print(current.data, end=' ')
while current.link is not node1:
    current = current.link
    print(current.data, end=' ')
