import pandas as pd
from BThree2 import BTreeCustom
from memory_profiler import profile


fp = open('memory_profiler.log', 'a+')
@profile(stream=fp)
def bthree():
    # Leer el dataframe de productos y instanciar el árbol B
    product_df = pd.read_csv('product_df.csv')
    btree = BTreeCustom(local_btree=True, degree=4)

    ###########################################################
    # Insertar productos en el Arbol B
    ###########################################################
    for index, row in product_df.iterrows():
        feature_vector = row.drop('id').values
        btree.insert(row['id'], feature_vector)

    ###########################################################
    # Buscar productos similares
    ###########################################################
    # Seleccionar un producto de referencia
    target_product_id = 1634
    # Obtener el vector de características del producto de referencia
    target_vector = product_df[product_df['id'] == target_product_id].values[0][1:]
    # Buscar productos similares al producto de referencia
    recommended_products = btree.search_similar(target_vector, k=8)
    # Mostrar IDs de los productos recomendados
    recommended_product_ids = [product[1] for product in recommended_products]
    return btree, target_product_id, recommended_product_ids

if __name__ == '__main__':
    bthree()