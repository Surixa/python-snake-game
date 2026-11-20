from turtle import Turtle
starting_postion = [(0,0), (-20,0), (-40,0)]
move_distance = 20
up = 90
down = 270
left = 180
right = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
    
     
        
    def create_snake(self):
        for position in starting_postion:
            self.add_segment(position)
            
    def add_segment(self,position):
        turtle = Turtle(shape= "square")
        turtle.color("white")
        turtle.penup()  
        turtle.goto(position)
        self.segments.append(turtle)
        
        
    def extend(self):
        self.add_segment(self.segments[-1].position())    
        
    def move(self):
        for seg_num in range(len(self.segments) -1, 0 , -1):
            new_xcoor = self.segments[seg_num - 1].xcor()
            new_ycoor = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_xcoor, new_ycoor)
        self.segments[0].forward(move_distance)
    def up(self):
        if self.segments[0].heading() != down:
                self.segments[0].setheading(up)   
        
    def down(self):
        if self.segments[0].heading() != up:
            self.segments[0].setheading(down)
            
    def left(self):
        if self.segments[0].heading() != right:
            self.segments[0].setheading(left)
            
    def right(self):
        if self.segments[0].heading() != left:
            self.segments[0].setheading(right)