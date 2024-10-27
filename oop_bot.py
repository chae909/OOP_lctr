import datetime

class Robot:
    def __init__(self, name="bot", color="grey"):
        self.name = name
        self.color = color
        self.made_year = datetime.date.today().year

    def say_hello(self):
        print(f"Hello!My name is {self.name}.", end=" ")
        print(f"I was born in {self.made_year}")

    def change_name(self, name):
        self.name = name

    def how_old(self):
        return datetime.date.today().year - self.made_year

if __name__ == "__main__":
    robots = [Robot(), Robot("Sambot", "blue")]
    robots[0].change_name("Kbot")

    for r in robots:
        r.say_hello()