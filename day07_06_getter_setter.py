#naming convention

class Duck():
    color = "white"
    def __init__(self,input_name):
        self.__name = input_name

    @property
    def name(self):
        print('inside the getter')
        return self.__name

    @property
    def name(self, input_name):
        print('inside the setter')

        self.__name = input_name

don = Duck("induck")
print(don._Duck__name)