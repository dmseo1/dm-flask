import datetime

class DatetimeDecorator :
    def __init__(self, f) :
        self.func = f
    
    def __call__(self, *args, **kwargs) :
        print(datetime.datetime.now())
        self.func()
        print(datetime.datetime.now())
    

class MainClass :
    @DatetimeDecorator
    def main_function_1() :
        print('MAIN FUNCTION 1 CALLED')

    @DatetimeDecorator
    def main_function_2() :
        print('MAIN FUNCTION 2 CALLED')

    @DatetimeDecorator
    def main_function_3() :
        print('MAIN FUNCTION 3 CALLED')

    @DatetimeDecorator
    def main_function_4() :
        print('MAIN FUNCTION 4 CALLED')

    @DatetimeDecorator
    def main_function_5() :
        print('MAIN FUNCTION 5 CALLED')

m = MainClass()
m.main_function_1()
m.main_function_2()
m.main_function_3()
m.main_function_4()
m.main_function_5()
