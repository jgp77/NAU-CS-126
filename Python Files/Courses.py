# I'm assuming that time will be given like 12:30 is 1230 or 1:30 is 1330
# I am also assuming the first class will always return False, as it is the only
# class so far.

class Courses():
    start_times =[]
    end_times= []
    def __init__(self, class_name, credit, start_time, end_time):
        self.credits=credit
        self.class_name=class_name
        self.start_time=start_time
        self.end_time=end_time
    def compare_time(self):
        for start in Courses.start_times:
            for end in Courses.end_times:
                if (start <= int(self.start_time)) or (end >= int(self.end_time)) or (int(self.start_time) <= end):
                    return True
        else:
            Courses.start_times.append(int(self.start_time))
            Courses.end_times.append(int(self.end_time))
            return False
        
cs125= Courses('CS125',4,'1200','1400')
cs126=Courses('CS126',4,'1110','1225')
cs136=Courses('CS136',5,'1015','1500')
print(cs126.compare_time())
print(cs125.compare_time())
print(cs136.compare_time())
