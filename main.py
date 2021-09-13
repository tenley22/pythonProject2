
class Rocket:

    def __init__(self, x_loc, y_loc, height=200):
        self.height = height
        self.x_loc = x_loc
        self.y_loc = y_loc
        self.rocket_velo = 10

    def move_up(self):
        self.y_loc -= self.rocket_velo


rocket1 = Rocket(100, 400)
#rocket2 = Rocket( )

# rocket1 = instance of the Rocket class, then you can find attributes (ex. height) or run methods (ex. rocket_sound)


print(rocket1.x_loc)
#print(rocket2.x_loc)

for i in range(10):
    print(rocket1.move_up())
    print(rocket1.y_loc)
    print()

enemy_rockets=[]
for i in range(10):
    rocket = Rocket(100,400)
    enemy_rockets.append(rocket)
# can also do enemy_rockets = [Rocket(100,400) for i in range(10)] USING list comprehension
for rocket in enemy_rockets:
    print(rocket)

