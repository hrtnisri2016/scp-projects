import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = [item for color, num_balls in kwargs.items() for item in [color]*num_balls]
    
    def draw(self, num_balls_drawn):
        if num_balls_drawn > len(self.contents): 
            return self.contents
        else:
            balls_drawn = []
            for n in range(0, num_balls_drawn):
                drawn = random.choices(self.contents)[0]
                balls_drawn.append(drawn)
                self.contents.remove(drawn)
            return balls_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    hat_original = copy.deepcopy(hat)
    balls_color = list(expected_balls.keys())
    count = 0
  
    for n in range(0, num_experiments):
        balls_drawn = hat.draw(num_balls_drawn)
        check = [balls_drawn.count(color) >= expected_balls[color] for color in balls_color]
        if not False in check: count += 1
        hat = copy.deepcopy(hat_original)
    
    return count / num_experiments