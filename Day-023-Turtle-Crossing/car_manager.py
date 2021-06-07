from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

NUMBER_OF_CARS = 10
Y_LOWER = -240
Y_UPPER = 280
X_LEFT = -350
X_RIGHT = 350

class CarManager():
    def __init__(self):
        #super().__init__()
        self.car_list = []
        self.create_starting_cars()
        self.cars_on_screen = NUMBER_OF_CARS
        print(self.car_list)


    def create_starting_cars(self):
        for i in range(NUMBER_OF_CARS):
            car = self.create_car()
            print(car)
            self.car_list.append(car)

    def create_car(self):
        car = Turtle()
        car.penup()
        car.shape("square")
        car.turtlesize(stretch_wid=1, stretch_len=2)
        car.color(random.choice(COLORS))
        x = random.randint(X_LEFT, X_RIGHT)
        y = random.randint(Y_LOWER, Y_UPPER)
        car.goto((x, y))
        car.setheading(180)
        return car

    def create_car_far_field(self):
        car = Turtle()
        car.penup()
        car.shape("square")
        car.turtlesize(stretch_wid=1, stretch_len=2)
        car.color(random.choice(COLORS))
        x = X_RIGHT
        y = random.randint(Y_LOWER, Y_UPPER)
        car.goto((x, y))
        car.setheading(180)
        return car

    def move_cars(self):
        for car in self.car_list:
            car.forward(MOVE_INCREMENT)


    def check_cars_on_screen(self):
        self.cars_on_screen = 0

        for i in range(len(self.car_list)):

            if (self.car_list[i].xcor() > X_LEFT) and (self.car_list[i].xcor() < X_RIGHT):
                self.cars_on_screen += 1
            else:
                self.car_list.pop(i)
                self.car_list.append(self.create_car_far_field())


    # def create_cars(self):
    #     for i in range(NUMBER_OF_CARS):
    #         car = Turtle()
    #         car.penup()
    #         car.shape("square")
    #         car.turtlesize(stretch_wid=1, stretch_len=2)
    #         car.color(random.choice(COLORS))
    #         x = random.randint(X_LEFT, X_RIGHT)
    #         y = random.randint(Y_LOWER, Y_UPPER)
    #         car.goto((x,y))
    #         self.cars.append(car)

