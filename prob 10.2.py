# prob 10.2
class Thing2():
    def __init__(self,letters):
        self.letters = letters

ex = Thing2('abc')
ex.letters = 'xyz'
ex.name = 'dung'
print(ex.letters)
print(ex.name)