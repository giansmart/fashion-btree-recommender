from sortedcontainers import SortedList
import numpy as np

class BThree:
  def __init__(self):
    self.tree = SortedList()

  def insert(self, product_id, feature_vector):
    feature_vector = tuple(feature_vector)
    # print((feature_vector, product_id))
    self.tree.add((feature_vector, product_id))

  def search_similar(self, target_vector, k=5):
    # Buscar los productos más cercanos usando la distancia euclidiana
    distances = [(self.euclidean_distance(target_vector, np.array(product[0])), product[1])
                for product in self.tree]
    distances.sort(key=lambda x: x[0]) # Ordenamos por la distancia más corta
    return distances[:k] # Retornar los k productos más similares

  @staticmethod
  def euclidean_distance(v1, v2):
    return sum((a - b) ** 2 for a, b in zip(v1, v2)) ** 0.5

btree = BThree()
