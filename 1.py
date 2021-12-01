import numpy
from utils import get_todays_input

# Task 1
def task1(data):
    diffs = data - numpy.roll(data, 1)
    return numpy.sum(diffs > 0)


todays_input = get_todays_input(1)

print(task1(todays_input))

# Task 2
result = numpy.empty(todays_input.shape[0] - 2)
result[0::3] = todays_input[0::3][:-1] + todays_input[1::3][:-1] + todays_input[2::3]
result[1::3] = todays_input[1::3][:-1] + todays_input[2::3] + todays_input[3::3]
result[2::3] = todays_input[2::3] + todays_input[3::3] + todays_input[4::3]
print(task1(result))
