class A:
    def __init__(self):
        self._te = 0
        self.__tes = 0
    def show(self):
        print(self._te)
        print(self.__tes)

a = A()
a.show()
try:
    print(A._te) 
except:
    print('error')
    pass  