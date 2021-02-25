import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **balls):
        self.contents = self.create_balls_list(balls)

    def get_contents(self):
        return self.contents

    def create_balls_list(self, dict):
        result = []
        for ball_type, ball_count in dict.items():
            for _ in range(ball_count):
                result.append(ball_type)
        return result

    def draw(self, num_of_balls):
        if num_of_balls > len(self.get_contents()):
            self.get_contents()

        drawn_balls = []
        for _ in range(num_of_balls):
            random_index = random.randint(0, len(self.get_contents()) - 1)
            drawn_balls.append(self.contents.pop(random_index))
        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass