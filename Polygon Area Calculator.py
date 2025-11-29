# class square
class square:

    def __init__(self):
        # private attribute
        self._side = 10

    def area(self):
        print("Side :", self._side)
        print("My area is :", self._side**2)

ob = square()
# updating value of private attribute
ob._side = 15
# calling area method to check the changes
ob.area()