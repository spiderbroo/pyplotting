from random import choice
import matplotlib.pyplot as plt

class RandomWalk():

    def __init__(self, num_points=200):
        self.num_points = num_points

        self.x_values=[0]
        self.y_values=[0]
    

    def fill_walk(self):
        x_step_counting = 0
        y_step_counting = 0
        while len(self.x_values) < self.num_points:
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice ([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            x_step_counting += int(x_step)
            y_step_counting += int(y_step)

            if x_step == 0 and y_step == 0 or x_step_counting > 50 or x_step_counting < -50 or y_step_counting > 50 or y_step_counting < -50:
                continue
            
            print(x_step_counting, y_step_counting)
            
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
        

while True:
    rw = RandomWalk()
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Greens, edgecolor='none', s=15)
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break




