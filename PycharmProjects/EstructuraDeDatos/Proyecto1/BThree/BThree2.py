from sortedcontainers import SortedList
import numpy as np
from srcBthree.btree import BTree

##############################################################################
# Eleccion de dos tipos de arboles uno local y otro con la libreria SortedList.
# 1. BTree local -> BTreeCustom(local_btree=True, degree=4)
# 2. SortedList -> BTreeCustom()
##############################################################################
class BTreeCustom:
  def __init__(self, local_btree=False, degree=4):
    self.local_btree = local_btree
    self.tree = BTree(degree=degree) if local_btree else SortedList()

  def insert(self, product_id, feature_vector):
    feature_vector = tuple(feature_vector)
    if self.local_btree:
      self.tree.insert(feature_vector, product_id)
    else:
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

btree = BTreeCustom(local_btree=True, degree=4)
#btree = BTreeCustom()
