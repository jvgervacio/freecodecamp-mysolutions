import copy
import random
# Consider using the modules imported above.

class Hat:
    
    def __init__(self, **balls):
        self.contents = []
        for ball in balls:
            for content in range(balls.get(ball)):
                self.contents.append(ball)

    def draw(self,number_of_balls):
        draw_result = None
        if number_of_balls >= self.get_totaln():
             draw_result = copy.deepcopy(self.contents)
             self.contents.clear()
             return draw_result
        else:
            draw_result = random.sample(self.contents,number_of_balls)
            for ball in draw_result:
                self.contents.remove(ball)
                        
            return draw_result
    def get_dict(self):
        return {ball:self.contents.count(ball) for ball in self.contents}
    
    def get_totaln(self):
        return len(self.contents)

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected_result = 0
    for experiment in range(num_experiments):
        test_hat = copy.deepcopy(hat)
        draw_sample = test_hat.draw(num_balls_drawn)
        draw_sample = {ball: draw_sample.count(ball) for ball in draw_sample}
        
        result = True
        for ball in expected_balls:
            if ball not in draw_sample or draw_sample[ball] < expected_balls[ball]:         
                result = False
                break
        if result:
             expected_result += 1
            
    return expected_result/num_experiments
