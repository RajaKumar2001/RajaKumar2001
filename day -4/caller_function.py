def show1():
    print("This is show1 function.")

def show2():
    print("This is show2 function.")

def show3():
    print("This is show3 function.")

def caller(func):
    func()

caller(show1)
caller(show2)
caller(show3)
