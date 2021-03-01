import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **balls):
        self.contents = create_list(balls)

    def get_contents(self):
        return self.contents

    def draw(self, num_of_balls):
        if num_of_balls > len(self.get_contents()):
            return self.get_contents()

        drawn_balls = []

        for _ in range(num_of_balls):
            random_ball = random.choice(self.get_contents())
            drawn_balls.append(random_ball)
            self.contents.pop(self.contents.index(random_ball))

        return drawn_balls


def create_list(dictionary):
    result = []
    for key, val in dictionary.items():
        for _ in range(val):
            result.append(key)
    return result


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    match_count = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn = hat_copy.draw(num_balls_drawn)

        # Convert drawn balls list to dictionary
        drawn_dict = dict.fromkeys(drawn, 0)
        for ball in drawn:
            drawn_dict[ball] += 1

        # Create dictionary of balls and ball_count
        matches = {ball: ball_count for (ball, ball_count) in drawn_dict.items()
                   if ball in expected_balls and ball_count >= expected_balls[ball]}

        # If matches is equal to the expected dictionary size, increment match_count
        if len(matches) == len(expected_balls):
            match_count += 1

    return match_count / num_experiments
