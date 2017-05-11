class MutantTracker:
    count= 0
    def __init__(self,num):
        self.count=num
        MutantTracker.count +=1

    def reset_count(self, cls):
        cls.count=0
class Automobile:
    def is_mobile(self):
        return True

class SportsCar(Automobile):
    def __init__(self, top_speed):
        self.top_speed=top_speed
    def is_sports_car(self):
        if self.top_speed > 176:
            return True
        else:
            return 'Not quite'

class Porsche(SportsCar):
    pass
