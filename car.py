class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12

    def display_all(self):
        print "Price: {}\nSpeed: {}\nFuel: {}\nMileage: {}\nTax: {}".format(str(self.price), str(self.speed), str(self.fuel), str(self.mileage),str(self.tax))
        print ""

car1 = Car(300, "40mph", "Half", "1mpg")
car2 = Car(303240, "420mph", "Empty", "12mpg")
car3 = Car(98320, "310mph", "Full", "55mpg")
car4 = Car(374895, "730mph", "3/4", "3.2mpg")
car5 = Car(2, "35mph", "Full", "15mpg")
car6 = Car(4039, "12mph", "Almost empty", "0.1mpg")

car1.display_all()
car2.display_all()
car3.display_all()
car4.display_all()
car5.display_all()
car6.display_all()