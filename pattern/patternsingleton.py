"""
This is a singleton design pattern
"""

#--------------------------------------------------------------
#----- This approach involves using metaclasses and class decorators
#--------------------------------------------------------------

class Singleton(type):
    #--- A bit of magic here
    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

class SingletonExample(metaclass=Singleton):

    def __init__(self):
        self.data = 0

    def method1 (self, parameter):
        self.data = parameter

    def method2 (self):
        return self.data;

#--------------------------------------------------------------
#----- This approach uses a private nested class
#--------------------------------------------------------------

class SingletonExampleNested:
    #---- Private instance of the class
    #---- Have to put all the data variables here
    class __SingletonExampleNested:
        def __init__(self):
            self.data = 0

    instance = None
    #---- Constructor creates an instance
    def __init__(self):
        if not SingletonExampleNested.instance:
            SingletonExampleNested.instance = SingletonExampleNested.__SingletonExampleNested()

    def __getattr__(self, name):
        return getattr(self.instance, name)

    #---- Get/Set
    def setdata(self, value):
        SingletonExampleNested.instance.data = value

    def getdata(self):
        return SingletonExampleNested.instance.data;



#--------------------------------------------------------------
#---- MAIN
#--------------------------------------------------------------

def main():
    #---- Let's try metaclass approach
    sc1 = SingletonExample()
    sc1.method1("test1")
    sc2 = SingletonExample()

    print(sc2.method2())


    scn1 = SingletonExampleNested()
    scn1.setdata("test2")
    scn2 = SingletonExampleNested()

    print(scn2.getdata())



#--------------------------------------------------------------

if __name__ == "__main__":
    main()