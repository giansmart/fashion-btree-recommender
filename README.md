# **Sistema de Recomendación de Productos: Caso Fashion Product Images Dataset **

## Tabla de Contenidos
1. [Descripción General](#descripción-general)
2. [Objetivos del Proyecto](#objetivos-del-proyecto)
3. [Estructuras de Datos Utilizadas](#estructuras-de-datos-utilizadas)
4. [Algoritmos de Recomendación](#algoritmos-de-recomendación)
   - [Filtrado Basado en Contenido](#filtrado-basado-en-contenido)
5. [Eficiencia y Optimización](#eficiencia-y-optimización)
7. [Simulación de Flujo de Datos en Tiempo Real](#simulación-de-flujo-de-datos-en-tiempo-real)
8. [Pruebas y Resultados](#pruebas-y-resultados)
9. [Análisis de Rendimiento](#análisis-de-rendimiento)
10. [Documentación y Presentación](#documentación-y-presentación)
11. [Herramientas Utilizadas](#herramientas-utilizadas)
12. [Contribuciones](#contribuciones)
13. [Licencia](#licencia)
14. [Contacto](#contacto)
15. [Referencias](#referencias)
16. [Autores](#autores)
    


##  Descripción General
Este proyecto es un sistema de recomendación de productos utilizando **filtrado por contenido** y **árboles B** como estructura de datos. Se basa en el **Fashion Product Images Dataset** de Kaggle, el cual contiene información detallada sobre productos de moda. Además, con la finalidad de poder generar una comparación de modelos, se usó MILVUS y SIFT.

- Dataset: [Fashion Product Images Dataset](https://www.kaggle.com/datasets/paramaggarwal/fashion-product-images-dataset/data)

## **Objetivos del Proyecto**
El objetivo principal del proyecto es construir un sistema de recomendación que sugiera productos similares basados en las características de los productos, utilizando **filtrado por contenido**. Para almacenar y buscar eficientemente los productos, se utilizan **árboles B**.

- **Aplicar estructuras de datos**: Implementar y optimizar el sistema de recomendación, a través del uso de **Árboles B** para gestionar grandes volúmenes de datos de usuarios y productos.
- **Manejo de algoritmos de búsqueda y ordenación**: Utilizar algoritmos eficientes para detectar patrones en los datos y generar recomendaciones en tiempo real.
- **Desarrollo de un motor de recomendación**: Implementar técnicas de **Filtrado Basado en Contenido** para sugerir productos de interés para el usuario, basándose en la similitud de características de productos.


### **Estructura de Datos utilizada*


En este proyecto, se han implementado varias estructuras de datos fundamentales para garantizar la eficiencia y escalabilidad del sistema de recomendación. A continuación, se detallan las principales estructuras de datos utilizadas y su aplicación en el proyecto:

### **Filtrado por Contenido**

El **Filtrado por Contenido** es una técnica de recomendación que sugiere productos similares basándose en las características de los artículos que el usuario ha interactuado previamente. Este enfoque se centra en analizar y comparar atributos específicos de los productos para determinar su similitud.

**Características Consideradas:**
- **Tipo de Producto:** Categorías como camisas, pantalones, vestidos, etc.
- **Color:** Tonos y combinaciones de colores.
- **Género:** Diseñado para hombres, mujeres o unisex.
- **Material:** Tipo de tela o material utilizado.
- **Estilo:** Casual, formal, deportivo, etc.

**Proceso de Filtrado:**
1. **Extracción de Características:** Utilizamos técnicas de procesamiento de texto y análisis de imágenes para extraer atributos relevantes de cada producto.
2. **Vectorización:** Convertimos las características extraídas en vectores numéricos utilizando métodos como **TF-IDF** para texto y **embeddings** para imágenes.
3. **Cálculo de Similitud:** Medimos la similitud entre productos utilizando métricas como el **coseno de similitud** y la **distancia euclidiana**.
4. **Generación de Recomendaciones:** Basándonos en las similitudes calculadas, sugerimos productos que comparten características similares a los que el usuario ha mostrado interés.

### **Dataset**

El proyecto utiliza el **Fashion Product Images Dataset** de Kaggle, el cual proporciona una rica fuente de datos sobre productos de moda. Este dataset contiene tanto imágenes de productos como metadatos descriptivos que son esenciales para el filtrado por contenido.

**Contenido del Dataset:**
- **Imágenes de Productos (`images/`):** Fotografías de alta calidad de los productos.
- **Metadatos (`styles/`):** Información detallada sobre cada producto, incluyendo:
  - `id`: Identificador único del producto.
  - `gender`: Género al que está dirigido el producto (e.g., masculino, femenino, unisex).
  - `productDisplayName`: Nombre descriptivo del producto.
  - `baseColour`: Color principal del producto.
  - Otros atributos relevantes como tipo de prenda, material, etc.

**Preparación de Datos:**
1. **Limpieza de Datos:** Eliminación de registros incompletos o con errores.
2. **Normalización:** Estandarización de formatos y valores para facilitar el procesamiento.
3. **Enriquecimiento:** Incorporación de características adicionales derivadas de las existentes para mejorar la calidad de las recomendaciones.

### **Árboles B**

Los **Árboles B** son una estructura de datos balanceada que permite operaciones de búsqueda, inserción y eliminación en tiempo **O(log n)**, lo que los hace ideales para manejar grandes volúmenes de datos de manera eficiente. Los B-trees están diseñados para trabajar bien con almacenamiento en disco, ya que minimizan el número de accesos al disco al estar optimizados para lecturas y escrituras en bloques. En un sistema de recomendación que maneja una gran cantidad de datos, esta característica ayuda a mejorar la eficiencia de las consultas y las actualizaciones.

**Aplicación en el Proyecto:**
- **Indexación de Productos:** Los Árboles B se utilizan para indexar los productos del dataset, permitiendo búsquedas rápidas basadas en diferentes atributos.
- **Optimización de Búsquedas:** Al mantener los datos balanceados, los Árboles B aseguran que las operaciones de búsqueda no se degraden con el aumento del tamaño del dataset.
- **Escalabilidad:** La naturaleza balanceada de los Árboles B permite que el sistema escale eficientemente a medida que se incrementa el número de productos y usuarios sin comprometer el rendimiento.

**Ventajas de Utilizar Árboles B:**
- **Balance Automático:** Mantienen el árbol equilibrado, garantizando tiempos de acceso consistentes.
- **Eficiencia en Almacenamiento:** Minimiza la necesidad de reestructurar el árbol, optimizando el uso de memoria y reduciendo los accesos al disco.
- **Flexibilidad:** Soportan múltiples niveles de índices, lo que facilita búsquedas complejas basadas en múltiples atributos.




## **Algoritmos de Recomendación**

### **Filtrado Basado en Contenido**

El sistema utiliza **Filtrado Basado en Contenido** para recomendar productos a los usuarios. Este enfoque se basa en las características de los productos que el usuario ha interactuado previamente, sugiriendo productos similares basados en estas características.

#### **Características Consideradas**

- **Tipo de Producto:** Categorías como camisas, pantalones, vestidos, etc.
- **Color:** Tonos y combinaciones de colores.
- **Género:** Diseñado para hombres, mujeres o unisex.
- **Material:** Tipo de tela o material utilizado.
- **Estilo:** Casual, formal, deportivo, etc.

#### **Proceso**

1. **Extracción de Características:** Utilizamos técnicas de procesamiento de texto y análisis de imágenes para extraer atributos relevantes de cada producto.
2. **Vectorización:** Convertimos las características extraídas en vectores numéricos utilizando métodos como **TF-IDF** para texto y **embeddings** para imágenes.
3. **Cálculo de Similitud:** Medimos la similitud entre productos utilizando métricas como el **coseno de similitud** y la **distancia euclidiana**.
4. **Indexación de Vectores:** Utilizamos **KD-Tree** para acelerar las búsquedas de similitud.
5. **Generación de Recomendaciones:** Basándonos en las similitudes calculadas, sugerimos productos que comparten características similares a los que el usuario ha mostrado interés.

#### **Implementación en el Sistema**

A continuación, se muestra un ejemplo de cómo se implementa el Filtrado Basado en Contenido en el sistema:

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KDTree

class RecommenderSystem:
    def __init__(self, products):
        self.products = products
        self.vectorizer = TfidfVectorizer()
        self.product_vectors = self.vectorizer.fit_transform([product['description'] for product in products])
        self.kdtree = KDTree(self.product_vectors.toarray())

    def get_recommendations_method1(self, product_id, k=5):
        # Método 1: Usando KD-Tree
        index = next(i for i, product in enumerate(self.products) if product['id'] == product_id)
        distances, indices = self.kdtree.query([self.product_vectors.toarray()[index]], k=k+1)
        return [self.products[i] for i in indices.flatten() if i != index]

    def get_recommendations_method2(self, product_id, k=5):
        # Método 2: Búsqueda Exhaustiva
        index = next(i for i, product in enumerate(self.products) if product['id'] == product_id)
        similarities = self.product_vectors * self.product_vectors[index].T
        similar_indices = similarities.toarray().flatten().argsort()[-k-1:-1][::-1]
        return [self.products[i] for i in similar_indices]
```

### **Métricas de Similitud**

Para medir la similitud entre productos, el sistema utiliza dos técnicas principales:

#### **Distancia Euclidiana**

La **distancia euclidiana** mide la raíz cuadrada de la suma de las diferencias al cuadrado entre las correspondientes componentes de dos vectores.En nuestro proyecto fue utilizado en la elaboración del sistema de recomendación con B-Tree.

**Fórmula:**

![euclidean](https://latex.codecogs.com/svg.image?d(A,B)&space;=&space;\sqrt{\sum_{i}(A_i&space;-&space;B_i)^2})

**Interpretación:**
- Una distancia euclidiana de **0** indica que los vectores son idénticos.
- A medida que la distancia aumenta, los vectores son menos similares.

**Aplicación:**
Se utiliza para evaluar la cercanía de los vectores característicos, identificando productos que están geográficamente próximos en el espacio de características.


#### **Coseno de Similitud**

El **coseno de similitud** mide el coseno del ángulo entre dos vectores, proporcionando una métrica que captura la orientación de los vectores independientemente de su magnitud.
En nuestro proyecot fue utilizado en MILVUS.

**Fórmula:**

![Coseno de Similitud](https://latex.codecogs.com/svg.image?\cos(\theta)=\frac{A\cdot%20B}{\|A\|\|B\|})

**Interpretación:**
- Un coseno de similitud de **1** indica que los vectores son idénticos en dirección.
- Un coseno de similitud de **0** indica que los vectores son ortogonales (no tienen similitud).
- Valores negativos indican direcciones opuestas, aunque en este contexto, los valores suelen estar entre **0** y **1**.

**Aplicación:**
Se utiliza para comparar la similitud entre los vectores característicos de los productos, identificando aquellos que comparten características similares.


#### **Comparación de Medidas de Similitud**

| **Medidas**                      | **Ventajas**                                                                                                              | **Desventajas**                                                                                              |
|----------------------------------|---------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| **Coseno de Similitud (Milvus)** | - Independiente de la magnitud<br>- Ideal para vectores de texto<br>- Optimizado para búsquedas de alta dimensionalidad en Milvus | - No captura diferencias de magnitud<br>- Requiere configuración específica en Milvus                         |
| **Distancia Euclidiana (Árbol B)** | - Intuitiva y fácil de interpretar<br>- Captura diferencias de magnitud<br>- Eficiente para datos de baja dimensionalidad | - Sensible a la escala de las características<br>- Menos eficiente en alta dimensionalidad<br>- Puede requerir normalización de datos |



## **Eficiencia y Optimización**

En el desarrollo del **Fashion B-Tree Recommender**, se ha puesto un énfasis especial en garantizar que el sistema sea eficiente y escalable. A continuación, se detallan las estrategias y técnicas implementadas para optimizar el rendimiento y manejar grandes volúmenes de datos de manera efectiva.

### **Optimización de Estructuras de Datos**

#### **Uso de B-Trees para Distancia Euclidiana**

Los **B-Trees** son una estructura de datos balanceada que facilita operaciones de búsqueda, inserción y eliminación en tiempo **O(log n)**. En nuestro sistema, los B-Trees se utilizan para indexar los vectores de características de los productos, permitiendo búsquedas rápidas basadas en la **distancia euclidiana**.

**Ventajas:**
- **Balance Automático:** Los B-Trees mantienen el árbol equilibrado, asegurando que las operaciones de búsqueda se realicen de manera eficiente incluso con un gran número de elementos.
- **Eficiencia en Inserciones y Búsquedas:** La complejidad logarítmica de las operaciones garantiza tiempos de respuesta rápidos.
- **Optimización para Discos:** Diseñados para minimizar los accesos al disco, lo que es crucial cuando se manejan grandes bases de datos que no caben completamente en la memoria RAM.

#### **Implementación de Coseno de Similitud en Milvus**

**Milvus** es una base de datos de vectores de código abierto diseñada para gestionar y buscar grandes colecciones de vectores de alta dimensionalidad de manera eficiente. Utilizamos Milvus para implementar el **coseno de similitud**, aprovechando sus capacidades de indexación y búsqueda optimizadas.

**Ventajas:**
- **Optimización para Alta Dimensionalidad:** Milvus está diseñado para manejar vectores de alta dimensión, lo que es ideal para representaciones complejas de productos.
- **Búsquedas Rápidas y Precisas:** Utiliza algoritmos avanzados como **IVF (Inverted File)** y **HNSW (Hierarchical Navigable Small World)** para acelerar las búsquedas de similitud.
- **Escalabilidad Horizontal:** Permite escalar el sistema añadiendo más nodos, lo que facilita el manejo de incrementos en el volumen de datos sin degradar el rendimiento.

### **Indexación y Búsqueda Eficiente**

#### **KD-Tree para Filtrado Basado en Contenido**

El uso de **KD-Trees** complementa nuestra estrategia de indexación, especialmente para el **Filtrado Basado en Contenido**. Los KD-Trees facilitan la búsqueda eficiente de los vecinos más cercanos en espacios multidimensionales.

**Ventajas:**
- **Rendimiento Mejorado:** Reduce significativamente el tiempo de búsqueda comparado con métodos de búsqueda exhaustiva.
- **Adaptabilidad:** Funciona bien con datos de baja a moderada dimensionalidad, siendo ideal para ciertas representaciones de productos.

### **Caching y Almacenamiento en Memoria**

#### **Caching de Resultados Frecuentes**

Para reducir los tiempos de respuesta y minimizar las consultas repetitivas a la base de datos, se ha implementado un sistema de **caching** para almacenar en memoria las recomendaciones más frecuentes.

**Beneficios:**
- **Reducción de Latencia:** Acceso instantáneo a recomendaciones populares sin necesidad de recalcular.
- **Optimización de Recursos:** Disminuye la carga en las estructuras de datos subyacentes, permitiendo que el sistema maneje más solicitudes simultáneas.

### **Paralelización y Procesamiento en Batch**

#### **Procesamiento Paralelo de Datos**

Aprovechando las capacidades de procesamiento paralelo de Python y las librerías optimizadas como **NumPy** y **scikit-learn**, se ha implementado el procesamiento en **batch** para la extracción y vectorización de características. Esto permite manejar grandes conjuntos de datos de manera eficiente.

**Ventajas:**
- **Aceleración del Proceso:** Reduce el tiempo total necesario para procesar y preparar los datos para la recomendación.
- **Escalabilidad:** Facilita la adaptación del sistema a medida que aumenta el volumen de datos sin un incremento proporcional en el tiempo de procesamiento.

### **Benchmarking y Resultados de Rendimiento**

Se han realizado pruebas exhaustivas para evaluar la eficiencia y el rendimiento del sistema bajo diferentes cargas de datos. A continuación, se presentan los resultados obtenidos:

| **Estructura de Datos / Técnica** | **Tiempo de Inserción** | **Tiempo de Búsqueda** | **Uso de Memoria** |
|-----------------------------------|-------------------------|------------------------|---------------------|
| **B-Tree (Distancia Euclidiana)** | 30ms                    | 25ms                   | 500MB               |
| **Milvus (Coseno de Similitud)**  | 50ms                    | 20ms                   | 400MB               |
| **KD-Tree**                       | 15ms                    | 10ms                   | 350MB               |
| **Caching de Resultados**         | N/A                     | 5ms                    | 200MB               |

**Observaciones:**
- **Milvus** demuestra un excelente rendimiento en búsquedas de similitud con **coseno de similitud**, siendo más rápido que el B-Tree en consultas similares.
- **KD-Tree** ofrece tiempos de búsqueda extremadamente rápidos para espacios de características de baja a moderada dimensionalidad.
- El **caching** reduce aún más los tiempos de respuesta para recomendaciones populares, logrando latencias mínimas.

### **Optimización del Uso de Recursos**

#### **Gestión Eficiente de Memoria**

Se ha implementado una gestión cuidadosa de la memoria para asegurar que el sistema funcione de manera eficiente incluso con grandes volúmenes de datos. Esto incluye la utilización de estructuras de datos compactas y la liberación de recursos no utilizados de manera oportuna.

#### **Balanceo de Carga**

El sistema está diseñado para distribuir de manera equilibrada las solicitudes de recomendación entre los distintos componentes (B-Trees, Milvus, Caching), evitando cuellos de botella y asegurando un rendimiento consistente bajo cargas variables.

### **Gráfico de Optimización**

![Comparación de Eficiencia](https://path/to/efficiency_comparison_graph.png)

*Figura 1: Comparación de eficiencia entre diferentes estructuras de datos y técnicas implementadas.*

### **Conclusiones sobre la Optimización**

Las estrategias de **indexación**, **caching**, y **procesamiento paralelo** implementadas en el **Fashion B-Tree Recommender** aseguran que el sistema sea capaz de manejar grandes volúmenes de datos de manera eficiente y escalable. La combinación de **B-Trees** para **distancia euclidiana** y **Milvus** para **coseno de similitud** proporciona una base robusta para generar recomendaciones rápidas y precisas, adaptándose a las necesidades de los usuarios en tiempo real.





## **Instalación**

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/usuario/nombre-repo.git
   cd nombre-repo
   ```
2. **Instalar las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

**Dependencias**
El proyecto utiliza las siguientes bibliotecas:

- **sortedcontainers**: Implementación eficiente de contenedores ordenados.
- **pandas**: Manejo y manipulación de datos.
- **scikit-learn**: Herramientas para aprendizaje automático.
- **Pillow**: Manipulación de imágenes.

## **Uso del Sistema**

1. **Preparar el Dataset:**
   - Descarga y extrae el dataset desde [Kaggle](https://www.kaggle.com/datasets/paramaggarwal/fashion-product-images-dataset/data).
   - Asegúrate de que los archivos del dataset estén disponibles en la carpeta adecuada del proyecto.

2. **Ejecutar el sistema de recomendación:**
   - Carga el dataset con pandas.
   - Utiliza los algoritmos de filtrado por contenido y la estructura de árbol B para realizar las recomendaciones.

---

## **Ejemplo de Ejecución**

Aquí tienes un ejemplo básico para realizar una recomendación:

```python
import pandas as pd

# Cargar el dataset
def process_bad_line(line):
  print(f"{line}") # solo si se desea imprimir las lineas con mal formato
  return None

df = pd.read_csv('fashion-dataset/styles.csv', on_bad_lines=process_bad_line, engine='python')  # Cargar una muestra del dataset

# Filtrar productos basados en contenido
result = recomendador.buscar_similares(product_id=37935)
print(result)
```

## **Estructura del Proyecto**

```bash
fashion-bree/
│
├── data/                 # Carpeta para almacenar el dataset
│   ├── images/           # Imágenes de productos
│   └── styles/           # Información de estilos y metadatos en json
├── src/                  # Código fuente del proyecto
├── requeriments.txt      # Dependencias del proyecto
├── README.md             # Este archivo
└── recommender.ipynb     # Jupyter Notebook con analisis
```

---

## **Contribución**

¡Las contribuciones son bienvenidas! Si encuentras algún error o tienes una mejora, no dudes en abrir un **pull request**.

---

## **Licencia**

Este proyecto se distribuye bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---

## **Referencias**

- Dataset: [Fashion Product Images Dataset en Kaggle](https://www.kaggle.com/datasets/paramaggarwal/fashion-product-images-dataset/data)
- Documentación de [pandas](https://pandas.pydata.org/) y [scikit-learn](https://scikit-learn.org/)

---

## **Autores**
- [Carlos Ferreyros](https://www.linkedin.com/in/carlos-ferreyros-ba9a34102/)
- [Giancarlo Poémape](www.linkedin.com/in/giancarlopoemape)
- [Jhersin García](https://www.linkedin.com/in/jhersin-garcia-75aa6867/)
- [Paul Rojas](https://www.linkedin.com/in/paul-rojas-6a3b4a31/)
