"""
This is a factory design pattern
It uses the abc module for abstract classes
"""
import abc


#--------------------------------------------------------------
#----- Device interfaces, and concrete device classes
#--------------------------------------------------------------

class DeviceInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def method1(self):
        pass

    @abc.abstractmethod
    def method2(self, parameter):
        pass

#--------------------------------------------------------------

class DeviceA(DeviceInterface):

    def method1(self):
        print("Called method1 on deviceA")

    def method2(self, parameter):
        print("Called method2 on deviceA")

class DeviceB(DeviceInterface):

    def method1(self):
        print("Called method1 on deviceB")

    def method2(self, parameter):
        print("Called method2 on deviceB")

#--------------------------------------------------------------
#----- Factory
#--------------------------------------------------------------

class Factory():

    def createdevice (devicetype):

        if devicetype == 1: return DeviceA()
        if devicetype == 2: return DeviceB()

#--------------------------------------------------------------
#---- MAIN
#--------------------------------------------------------------

def main():
    device = Factory.createdevice(1)
    device.method1()
    device = Factory.createdevice(2)
    device.method2(1)

#--------------------------------------------------------------

if __name__ == "__main__":
    main()