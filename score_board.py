from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.starting_score = 0
        self.goto(0, 270)
        self.penup()
        self.hideturtle()
        self.pencolor("white")
        self.write(f"Score = {self.starting_score} ", move = False, align= "center", font= ("Courier", 15,"normal"))
        
    def new_score(self):
        self.starting_score += 1
        self.clear()
        self.write(f"Score = {self.starting_score} ", move = False, align= "center", font= ("Courier", 15,"normal"))
        
        
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over.", move = False, align= "center", font= ("Courier", 15,"normal"))
        