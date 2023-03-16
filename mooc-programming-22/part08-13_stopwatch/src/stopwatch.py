class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    def __str__(self):
        if self.minutes<10 and self.seconds<10:
            return "0"+f"{self.minutes}"+":0"+f"{self.seconds}"
        elif self.minutes>10 and self.seconds<10:
            return f"{self.minutes}"+":0"+f"{self.seconds}"
        elif self.minutes<10 and self.seconds>10:
            return "0"+f"{self.minutes}:{self.seconds}"
        else:
            return f"{self.minutes}:{self.seconds}"
    
    def tick(self):
        if self.seconds==59:
            self.seconds = 0
            
            if self.minutes==59:
                self.minutes = 0
            else:
                self.minutes += 1
        else:
            self.seconds += 1
        
if __name__ == "__main__":
    watch = Stopwatch()

    for i in range(3600):
        print(watch)
        watch.tick()