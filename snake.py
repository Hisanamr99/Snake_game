from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT =0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for position in STARTING_POSITION:
            self.new_add(position)

    def new_add(self, position):
        new_snake = Turtle(shape="square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(position)
        self.segments.append(new_snake)

    def extend(self):
        self.new_add(self.segments[-1].position())


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x_position = self.segments[seg_num - 1].xcor()
            new_y_position = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x_position, new_y_position)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        #pass

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        #pass

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        #pass

