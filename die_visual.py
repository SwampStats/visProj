# Die program
import pygal
from die import Die

    # Create a D6.
die = Die()
   #make some rolls, and store resuls in a list.

results = []
results= [die.roll() for roll_num in range(1000)]

    # Analyze the results.
frequencies = []
frequencies = [results.count(value) for value in range(1, die.num_sides + 1)]

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
#hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_labels=[x for x in range(1,6)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
