import pandas as pd
from BThree import BThree
from memory_profiler import profile
import time

fp = open('BusquedaInsertar/memory_profiler.log', 'a+')
@profile(stream=fp)
def insert_bthree():
    product_df = pd.read_csv('product_df.csv')

    btree = BThree()

    # Assuming 'id' is the product_id and 'feature_vector' is your data vector
    for index, row in product_df.iterrows():
        feature_vector = row.drop('id').values
        btree.insert(row['id'], feature_vector)
        if index < 1:
            print(row['id'], feature_vector)

if __name__ == '__main__':
    insert_bthree()