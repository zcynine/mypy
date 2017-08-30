#list
game = ["dota", "dota2", "lol"]

print game

print len(game)

game.append("wow")
print game

game.insert(2, "war3")
print game

game.pop()
print game

game.pop(1)
print game


print "-------------------------"
#dic
name = {1: "alan", 2: "bob", 3: "lucy"}
print name[2]
print name.get(5)
print name.get(5, "default")

name[4] = "mac"
print name

name.pop(1)
print name

print name.keys()
print name.values()
print name.items()


print "-------------------------"
#set
girls_1 = set(['lucy', 'lily'])
girls_2 = set(['lily', 'anna'])

print girls_1 & girls_2
print girls_1 | girls_2

girls_1.add('marry')
girls_1.remove('lucy')
print girls_1







