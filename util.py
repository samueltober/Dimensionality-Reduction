import numpy as np


def get_city_continent_dict():
    """Load the cities and their corresponding continents from the file"""
    city_continent_dict = {}
    with open('cities.txt', 'r') as f:
        for line in f:
            city, continent = line.split(' - ')
            city_continent_dict[city] = continent.strip()

    return city_continent_dict


def plot_coords(coords: np.ndarray, city_continent_dict: dict):
    """Plots the 2d coordinates in coords and colors the points according to their
       corresponding continent"""
    import matplotlib.pyplot as plt
    from matplotlib.patches import Circle

    fig, ax = plt.subplots()
    ax.set_xlim(-0.3, 0.3)
    ax.set_ylim(-0.3, 0.3)
    fig.set_size_inches(20, 10)
    #ax.set_aspect('equal')
    ax.set_title('MDS coordinates')

    i = 0

    for city, continent in city_continent_dict.items():
        if continent == 'Europe':
            color = 'blue'
        elif continent == 'Asia':
            color = 'green'
        elif continent == 'North America':
            color = 'orange'
        elif continent == 'Latin America':
            color = 'red'
        elif continent == 'Africa':
            color = 'brown'

        circle = Circle(coords[i], 0.01, color=color)
        ax.add_patch(circle)
        ax.annotate(city, coords[i], color=color)
        i += 1

    plt.show()
