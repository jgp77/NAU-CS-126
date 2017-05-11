import time
class StopWatch:
    num_watches=0
    def __init__(self, p_color):
        self.colore=p_color
        self.start_time=0
        self.stop_time=0
        StopWatch.num_watches+=1

    def start(self):
        print(p_colore)
        self.start_time=time.time()

    def stop(self):
        self.stop_time=time.time()

    def __atr__(self):
        return str(self.stop_time - self.start_time)
