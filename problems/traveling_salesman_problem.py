__author__ = 're9ulus'

import numpy as np
import math
import matplotlib.pyplot as plt


class City:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other):
        math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


class TravelinSalesmanProblem:

    def __init__(self):
        self.cities = []

    def add_city(self, city):
        self.cities.append(city)

    def distance_btw_cities(self, city_index_1, city_index_2):
        city_1 = self.cities[city_index_1]
        city_2 = self.cities[city_index_2]
        return city_1.distance_to(city_2)

    def path_distance(self, path):
        '''Compute distance of the path
        '''
        distance = 0
        for index in path[1:]:
            step_distance = self.distance_btw_cities(path[index-1], path[index])
            distance += step_distance
        return distance

    def check_path(self, path):
        '''Check that every city is visited only once
        '''
        if len(list(set(path))) != len(self.cities):
            return False
        return True

    def cities_coords(self):
        x_coords = [city.x for city in self.cities]
        y_coords = [city.y for city in self.cities]
        return x_coords, y_coords

    def __plot_cities(self):
        x_coords, y_coords = self.cities_coords()
        plt.plot(x_coords, y_coords, 'ro')

    def __plot_path(self, path):
        x_coords, y_coords = [], []
        for i in path:
            x_coords.append(self.cities[i].x)
            y_coords.append(self.cities[i].y)
        plt.plot(x_coords, y_coords)

    def __plot_axis(self):
        delta = 10
        x_coords, y_coords = self.cities_coords()
        min_x, max_x = min(x_coords), max(x_coords)
        min_y, max_y = min(y_coords), max(y_coords)
        plt.axis([min_x - delta, max_x + delta, min_y - delta, max_y + delta])

    def plot_cities(self):
        self.__plot_cities()
        self.__plot_axis()
        plt.show()

    def plot_path(self, path):
        self.__plot_cities()
        self.__plot_path(path)
        self.__plot_axis()
        plt.show()

    def generate_random_cities(self, n):
        raise "ERROR: Unimplemented"


if __name__ == '__main__':
    tsp = TravelinSalesmanProblem()
    tsp.add_city(City(30, 30))
    tsp.add_city(City(50, 20))
    tsp.add_city(City(20, 60))
    tsp.add_city(City(80, 40))
    tsp.plot_cities()
    path = [2, 1, 0, 3]
    tsp.plot_path(path)