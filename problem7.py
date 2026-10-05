class Mobile:
    def __init__(self,initial_battery=20):
        self.__battery=initial_battery if initial_battery > 0 else 20

    def charge(self,percent):
        if percent>0:
            self.__battery+=percent
            return f"{self.__battery}"
        else:
            return "Enter valid charging number"
        
    def use(self,minutes):
        if 200 >= minutes >= 1:
            self.__battery-=0.5*minutes
            return f"{self.__battery}"
        else:
            return "Use for limited time"
    
    def display_battery(self):
        return f"{self.__battery}"

m1=Mobile(50)
print(m1.charge(20))
print(m1.use(23))
print(m1.display_battery())
