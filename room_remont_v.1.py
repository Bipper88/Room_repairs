class WinDoor:
     def __init__(self, x, y, name="unk"):
       self.x = x
       self.y = y
       self.name = name
       self.square = x * y 

     def __repr__(self):
       return f'{self.name} {self.x}x{self.y}'


class Room:

    def __init__(self, x, y, z):
        self.square = 2 * z * (x + y)
        self.wd = []

    def addWD(self, w, h, name='unk'):
        self.wd.append(WinDoor(w, h, name))
        
    def workSurface(self):
        new_square = self.square
        for i in self.wd:
            new_square -= i.square
        return new_square



#Выполнение кода


r1 = Room(4, 3, 2.5) 
print(r1.square)            #расчет площади комнаты



r1.addWD(1.5, 1.5, 'big_win')   #расчет площади окна
r1.addWD(1, 2, 'door_1')        #расчет площади двери

print(r1.wd)                    #вывод заданных параметров окна и двери
print(r1.workSurface())         #вывод площади комнаты за вычетом окна и двери
