import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Make a randomw walk, and plot the points.
rw = RandomWalk()
rw.fill_walk()
plt.figure(figsize=(20, 12))
#plt.scatter(rw.x_values, rw.y_values, s=1)
#now try with plot
plt.plot(rw.x_values, rw.y_values, linewidth=1)

plt.show()

