# Q4. Define a Time class with hour, minute and second, a parameterized constructor, displayTime() in HH:MM:SS format, and addTime() to add two Time objects.
class Time:
    def __init__(self, hour, minute, second):
        total_seconds = hour * 3600 + minute * 60 + second
        self.hour = (total_seconds // 3600) % 24
        self.minute = (total_seconds % 3600) // 60
        self.second = total_seconds % 60

    def displayTime(self):
        print(f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}")

    def addTime(self, other):
        total = (
            self.hour * 3600 + self.minute * 60 + self.second
            + other.hour * 3600 + other.minute * 60 + other.second
        )
        return Time(0, 0, total)

t1 = Time(4, 10, 48)
t2 = Time(2, 15, 38)
print("First time:", end=" ")
t1.displayTime()
print("Second time:", end=" ")
t2.displayTime()
result = t1.addTime(t2)
print("Resultant time:", end=" ")
result.displayTime()
