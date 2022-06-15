import copy
import random
# Consider using the modules imported above.

class Hat:

  def __init__(self, **balls):
    self.contents = [k for k,v in balls.items() for i in range(v)]
    self.contents_copy = self.contents

  def draw(self, tries):
    if tries > len(self.contents):
      return self.contents
      
    removed = []
    for _ in range(tries):
      ball = random.choice(self.contents)
      self.contents.remove(ball)
      removed.append(ball)
    return removed


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  m = 0
  expected_balls_copy = copy.deepcopy(expected_balls)
  for i in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    expected_balls_copy = copy.deepcopy(expected_balls)

    result = hat_copy.draw(num_balls_drawn)
    for b in result:
      if b in expected_balls_copy:
        expected_balls_copy[b] = expected_balls_copy.get(b) - 1

    if all([x<=0 for x in expected_balls_copy.values()]):
      m += 1

  return m/num_experiments
    