import numpy as np
from tqdm import tqdm


def get_cities_from_txt(file_name) -> list:
    """
    Returns a list of cities from a text file
    """
    cities = []
    with open(file_name, "r") as f:
        for line in f:
            cities.append(line.strip())

    return cities


def get_city_dist(city_A, city_B) -> float:
    """
    Returns the distance between two cities using https://www.distance24.org/api.xhtml API
    """
    import requests
    import json
    url = "https://www.distance24.org/route.json"
    params = {
        "stops": city_A + "|" + city_B,
        "mode": "car"
    }

    try:
        response = requests.get(url, params=params)
    except:
        return -1
    data = json.loads(response.text)

    return data["distances"][0]


def get_city_dist_matrix(cities) -> np.array:
    """
    Returns the distance matrix of all cities
    """
    import time

    dist_matrix = np.zeros((len(cities), len(cities)))
    for i in tqdm(range(len(cities))):
        for j in tqdm(range(len(cities))):
            dist_matrix[i][j] = get_city_dist(cities[i], cities[j])
            time.sleep(1)

    return dist_matrix


def create_and_save_dist_matrix():
    import pickle as pkl
    cities = get_cities_from_txt("cities.txt")
    dist_matrix = get_city_dist_matrix(cities)

    with open('dist_matrix.pkl', 'wb') as f:
        pkl.dump(dist_matrix, f)


if __name__ == "__main__":
    create_and_save_dist_matrix()
