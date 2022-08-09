# Fill in the following methods for the class 'Clock'

class Clock:
    def __init__(self, hour, minutes):
        self.minutes = minutes
        self.hour = hour

    # Print the time
    def __str__(self):
        if self.minutes < 10:
            time = str(self.hour) + ":0" + str(self.minutes)
        else:
            time = str(self.hour) + ":" + str(self.minutes)
        return time

    # Add time
    # Don't return anything
    def __add__(self, minutes):
        self.minutes += minutes
        if self.minutes // 60 > 0:
            self.hour += self.minutes // 60
            self.minutes = self.minutes - ((self.minutes // 60) * 60)
            if self.hour > 23:
                self.hour -= 24
            elif self.hour < 0:
                self.hour += 24

    # Subtract time
    # Don't return anything
    def __sub__(self, minutes):
        self.minutes -= minutes
        if self.minutes < 0:
            self.minutes = self.minutes * -1
            self.hour -= (self.minutes // 60) + 1
            self.minutes = self.minutes - ((self.minutes // 60) * 60)
            if self.hour > 23:
                self.hour -= 24
            elif self.hour < 0:
                self.hour += 24

    # Are two times equal?
    def __eq__(self, other):
        return self.hour == other.hour and self.minutes == other.minutes

    # Are two times not equal?
    def __ne__(self, other):
        return not (self.hour == other.hour and self.minutes == other.minutes)


# You should be able to run these
clock1 = Clock(23, 5)
print(clock1)  # 23:05
clock2 = Clock(12, 45)
print(clock2)  # 12:45
clock3 = Clock(12, 45)
print(clock3)  # 12:45

print(clock1 == clock2)  # False
print(clock1 != clock2)  # True
print(clock2 == clock3)  # True

print("testing addition")
clock1 + 60
print(clock1)  # 00:05
print(clock1 == Clock(0, 5))  # True

print("testing subtraction")
clock1 - 100
print(clock1)  # 22:25
