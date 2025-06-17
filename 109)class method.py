class Mobile:
    def __init__(self):
        print("object is created")
    @staticmethod
    def Display():
        print("i am constructor")
        print("i will work irrsepective of object creation")
Mobile.Display()
m1=Mobile()
m1.Display()

