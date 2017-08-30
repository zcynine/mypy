class Human(object):
    def __init__(self, name):
        self.__name = name
    def walk(self):
        print self.name + " is walking"
    def get_name(self):
        return self.__name
    def set_name(self, name):
        if len(name) <= 10:
            self.__name = name

human_a = Human("alan")
print human_a.get_name()

human_a.set_name("bob")
print human_a.get_name()

class Man(Human):
    def __init__(self, name, has_husband):
        super(Man, self).__init__(name)
        self.__has_husband = has_husband
    def smoke(self):
        print "A man maybe smoke"
    def drink(self):
        print "A man maybe drink"

class Woman(Human):
    def __init__(self, name, has_husband):
        super(Woman, self).__init__(name)
        self.__has_husband = has_husband
    def shopping(self):
        print "A woman always go shopping"
    def make_up(self):
        print "A woman always make up"
