class AC():
    def make_cool(self):
        ''''制冷'''
        pass

    def make_hot(self):
        ''''制热'''
        pass

    def make_test(self):
        ''''测试'''
        pass

class Meidi(AC):
    def make_cool(self):
        print("美的制冷")

    def make_hot(self):
        print("美的制热")

    def make_test(self):
        print("美的测试")


class Geli(AC):
    def make_cool(self):
        print("格力制冷")

    def make_hot(self):
        print("格力制热")

    def make_test(self):
        print("格力测试")

def cool(AC:AC):
    AC.make_cool()

def hot(AC:AC):
    AC.make_hot()

def test(AC:AC):
    AC.make_test()
    
meidi = Meidi()
geli = Geli()

cool(meidi)
hot(meidi)
test(meidi)

cool(geli)
hot(geli)
test(geli)