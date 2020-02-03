import datetime

def datetime_decorator(func) :
    def decorated() :
        print(datetime.datetime.now())
        func()
        print(datetime.datetime.now())
    decorated()
    #return decorated

@datetime_decorator
def main_function_1() :
    print('MAIN FUNCTION 1 CALLED')

#main_function_1()