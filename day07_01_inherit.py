#inherit

#클래스 생성
class Car():    #Yogo의 부모
    def exclaim(self):        # excalim 매서드 생성
        print("I'm a Car!")

class Yogo(Car): #Car의 자식
    #def exclaim(self):     #매서드 덮어쓰기 가능
    #    print("yogo!")
    def need_a_push(self):
        print("A little help here")


print(issubclass(Yogo, Car)) #True

#객체 생성
give_me_a_car = Car()   #객체 give_me_a_car 생성
give_me_a_yogo = Yogo()

#매서드 사용
give_me_a_car.exclaim()
give_me_a_yogo.exclaim()  #Yogo도 부모의 매서드를 상속받아 사용할 수 있음






