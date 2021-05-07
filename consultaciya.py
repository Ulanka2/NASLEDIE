# 2)Создайте класс Plane, конструктор которого принимает brand,
# model. Пропишите в классе метод info. Пусть он возвращает
# brand и model самолета. Создайте подклассы Destroyer
# (Истребитель), Stelth (Стэлс), Kukuruznik (Кукурузник). В классе
# Destroyer перегрузите метод конструктор с помощью функции
# super(), добавьте поле can_fire = True и выведите его в экземпляре класса.
#  Также создайте в классе
# Destroyer метод fire (стрелять). В классе Stelth перегрузите метод
# конструктор с помощью функции super(), добавьте поле is_visible = False и выведите его в экземпляре класса. 
# Также добавьте метод hide (прятаться) в класс Stelth. А в
# классе Kukuruznik перегрузите метод конструктор с помощью
# функции super(), добавьте поле can_fertilize = True и выведите его в экземпляре класса. Создайте в классе метод fertilize (распылять удобрения). Используйте созданные классы
# и методы.


class Plane:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def info(self):
        print(f"{self.brand, self.model}")

class Destroyer(Plane):
    
    def __init__(self,brand, model):
        super().__init__(brand,model)
        self.can_fire = True
    
    def fire(self):
        print(F"I can {self.can_fire} strelyayo")
   
class Stelth(Plane):
    
    def __init__(self,brand,model):
        super().__init__(brand,model)
        self.is_visible = False

    def hide(self):
        print("Pryatatssy")

class Kukuruznik(Plane):
    
    def __init__(self,brand,model):
        super().__init__(brand,model)
        self.can_fertilize = True

    def fertilize(self):
        print("распылять удобрения")

estroyer = Destroyer("a1", "a2")
telth = Stelth("b1", "b2")
ukuruznik = Kukuruznik("c1", "c2")

estroyer.fire()
estroyer.info()
telth.hide()
telth.info()
ukuruznik.fertilize()
ukuruznik.info()