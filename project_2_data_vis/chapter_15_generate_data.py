import matplotlib.pyplot as plt

# 15-1 Cubes
# 15-2 Colored Cubes (apply colormap)

x_maxes = [5, 5000]
for index, x_max in enumerate(x_maxes):
    x_data = range(1, x_max + 1)
    y_data = [x**3 for x in x_data]

    # Create figure in loop that will be shown in separate window after loop
    # figure index starts at 1
    plt.figure(index + 1)

    plt.scatter(x_data, y_data, c=y_data, cmap=plt.cm.Blues)
    
    plt.title("Cubic Numbers")
    plt.xlabel("Value")
    plt.ylabel("Cube of Value")
    plt.axis([0, x_data[-1], 0, y_data[-1]])

plt.show()