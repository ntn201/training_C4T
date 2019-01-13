class Timer:
    def __init__(self,hours,minutes,seconds):
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours
    def __str__(self):
        time = str(self.hours) + "h " + str(self.minutes) + "m " + str(self.seconds) + "s"
        return time
    def tick(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
        if self.minutes == 60:
            self.minutes = 0
            self.hours += 1
    def reset(self):
        self.seconds = 0
        self.minutes = 0
        self.hours = 0
