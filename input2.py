a = "Trout"
fish = [a, "Salmon", "Halibut", "Catfish", "Goldfish", "Swordfish"]
id = [50, 33, 85, 92]
nothing = []
b = " World"                #This Should be ignored
c = 10
d = a + b
k = 7

fish[0] = "EEL"

def test():
        print "a is ", " b is ", " c is "
        return "Ten"

ten = test()
print fish
fish = [1, 2, 3]
print fish
fish = ["Shark", "Minnow", "Guppy"]
print fish

for x in range(1, 3):
    print "x is ", x
    for y in range(len(fish)):
        print fish[y]

if len(fish) > len(id):
    print "fish is larger than id"
else if len(fish) < len(id):
    print "fish is smaller than id"

print "finished program "
