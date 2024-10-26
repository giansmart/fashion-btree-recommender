import pandas as pd
from BThree import BThree
from memory_profiler import profile
import time

fp = open('BusquedaInsertar/memory_profiler.log', 'a+')
@profile(stream=fp)
def bthree():
    product_df = pd.read_csv('product_df.csv')

    btree = BThree()

    # Assuming 'id' is the product_id and 'feature_vector' is your data vector
    for index, row in product_df.iterrows():
        feature_vector = row.drop('id').values
        btree.insert(row['id'], feature_vector)
        if index < 1:
            print(row['id'], feature_vector)

    target_product_id = 1634  # 1163  # 37935

    # Seleccionar un producto como base de recomendación
    target_vector = product_df[product_df['id'] == target_product_id].values[0][1:]
    print(target_vector.shape)

    # Obtener productos más similares
    recommended_products = btree.search_similar(target_vector, k=8)
    print(recommended_products)

    # Mostrar IDs de los productos recomendados
    recommended_product_ids = [product[1] for product in recommended_products]
    print("Productos recomendados:", recommended_product_ids)

if __name__ == '__main__':
    bthree()