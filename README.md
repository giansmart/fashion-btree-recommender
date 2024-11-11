# Sistema de Recomendación de Productos: Caso Fashion Product Images Dataset 

## Tabla de Contenidos
1. [Descripción General](#descripción-general)
2. [Objetivos del Proyecto](#objetivos-del-proyecto)
3. [Estructuras de Datos Utilizadas](#estructuras-de-datos-utilizadas)
4. [Algoritmos de Recomendación](#algoritmos-de-recomendación)
5. [Eficiencia y Optimización](#eficiencia-y-optimización)
6. [Pruebas y Resultados](#pruebas-y-resultados)
7. [Herramientas Utilizadas](#herramientas-utilizadas)
8. [Estructura del proyecto](#estructura-del-proyecto)
9. [Contribución](#contribuciones)
10. [Licencia](#licencia)
11. [Referencias](#referencias)
12. [Autores](#autores)
    


##  Descripción General
Este proyecto es un sistema de recomendación de productos utilizando **filtrado por contenido** y **árboles B** como estructura de datos. Se basa en el **Fashion Product Images Dataset** de Kaggle, el cual contiene información detallada sobre productos de moda. Además, con la finalidad de poder generar una comparación de modelos, se usó MILVUS y SIFT.

- Dataset: [Fashion Product Images Dataset](https://www.kaggle.com/datasets/paramaggarwal/fashion-product-images-dataset/data)

## **Objetivos del Proyecto**
El objetivo principal del proyecto es construir un sistema de recomendación que sugiera productos similares basados en las características de los productos, utilizando **filtrado por contenido**. Para almacenar y buscar eficientemente los productos, se utilizan **árboles B**.

- **Aplicar estructuras de datos**: Implementar y optimizar el sistema de recomendación, a través del uso de **Árboles B** para gestionar grandes volúmenes de datos de usuarios y productos.
- **Manejo de algoritmos de búsqueda y ordenación**: Utilizar algoritmos eficientes para detectar patrones en los datos y generar recomendaciones en tiempo real.
- **Desarrollo de un motor de recomendación**: Implementar técnicas de **Filtrado Basado en Contenido** para sugerir productos de interés para el usuario, basándose en la similitud de características de productos.


### **Estructura de Datos utilizada**


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
4. **Indexación de Vectores:** Utilizamos **-Tree** para acelerar las búsquedas de similitud.
5. **Generación de Recomendaciones:** Basándonos en las similitudes calculadas, sugerimos productos que comparten características similares a los que el usuario ha mostrado interés.


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


### **Comparación de Métricas de Similitud**

| **Métricas**                      | **Ventajas**                                                                                                              | **Desventajas**                                                                                              |
|----------------------------------|---------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| **Coseno de Similitud (Milvus)** | - **Independiente de la magnitud:** La similitud se basa en la orientación de los vectores, no en su tamaño.<br>- **Ideal para vectores de texto:** Funciona bien con datos textuales representados en espacios vectoriales.<br>- **Optimizado para búsquedas de alta dimensionalidad en Milvus:** Milvus está diseñado para manejar eficientemente grandes volúmenes de datos de alta dimensión. | - **No captura diferencias de magnitud:** No considera la magnitud de los vectores, lo que puede ser una limitación en ciertos contextos.<br>- **Requiere configuración específica en Milvus:** Necesita ajustes y optimizaciones particulares para aprovechar al máximo las capacidades de Milvus.                         |
| **Distancia Euclidiana (B-Tree)**| - **Intuitiva y fácil de interpretar:** La distancia euclidiana es una medida directa y comprensible de la similitud.<br>- **Captura diferencias de magnitud:** Considera tanto la dirección como la magnitud de los vectores, proporcionando una medida más completa de la similitud.<br>- **Eficiente para datos de baja dimensionalidad:** Funciona bien cuando el número de características es relativamente pequeño. | - **Sensible a la escala de las características:** Las diferencias en la escala de los datos pueden afectar significativamente la medida de similitud.<br>- **Menos eficiente en alta dimensionalidad:** Su rendimiento puede degradarse cuando se trabaja con datos de muchas dimensiones.<br>- **Puede requerir normalización de datos:** Para mitigar la sensibilidad a la escala, a menudo es necesario normalizar los datos antes de calcular la distancia euclidiana. |




## **Eficiencia y Optimización**

En el desarrollo del **Fashion Recommender**, se ha priorizado la eficiencia y optimización del sistema para manejar grandes volúmenes de datos de manera efectiva. A continuación, se describen las estrategias implementadas y las técnicas utilizadas para asegurar un rendimiento óptimo.


### **Gráfico de Optimización**

![Búsqueda por Inserción en B-Tree](https://github.com/giansmart/fashion-btree-recommender/blob/main/PycharmProjects/EstructuraDeDatos/Proyecto1/BThree/BusquedaInsertar/my_func.png?raw=true)

*Figura 1: Curva de Uso de Memoria según el tiempo en Inserción con B-Tree*


![Búsqueda por Inserción en B-Tree](https://github.com/giansmart/fashion-btree-recommender/blob/main/PycharmProjects/EstructuraDeDatos/Proyecto1/BThree/Insertar/my_func.png?raw=true)

*Figura 2: Curva de Uso de Memoria según el tiempo en Búsqueda con B-Tree*

### Análisis de Uso de Memoria en B-tree

Este documento proporciona un análisis comparativo del uso de memoria al insertar datos en un B-tree, basado en los registros de memoria capturados durante las pruebas de inserción y búsqueda en Python.


#### Cuadro Comparativo de Uso de Memoria

```markdown
| **Archivo**               | **Memoria Inicial** | **Memoria Máx. Uso** | **Incremento Memoria (inserción)** | **Observaciones**                                   |
|---------------------------|---------------------|----------------------|-------------------------------------|-----------------------------------------------------|
| **InsertBthree.py (1)**  | 93.0 MiB            | 639.1 MiB            | 334.0 MiB                          | Incremento constante en la línea 16 durante la inserción. |
| **InsertBthree.py (2)**  | 92.7 MiB            | 639.4 MiB            | 260.5 MiB                          | Uso de memoria menor en la línea 16 comparado con el primero. |
| **InsertBthree.py (3)**  | 92.8 MiB            | 639.2 MiB            | 260.4 MiB                          | Similar al segundo, con leve variación.               |
| **BusquedaInsertBthree.py (1)** | 102.5 MiB       | 655.4 MiB            | 346.6 MiB                          | Uso de memoria notablemente más alto en búsqueda y inserción. |
| **BusquedaInsertBthree.py (2)** | 92.8 MiB        | 645.5 MiB            | 345.2 MiB                          | Incremento en la línea 16 y proceso de búsqueda posterior. |
```

#### Observaciones Generales
- **Incrementos de Memoria en la Inserción**: La memoria aumenta considerablemente en la línea 16 en todos los casos, variando entre 260.4 MiB y 346.6 MiB.
- **Diferencias en Búsqueda vs. Inserción**: El archivo de búsqueda muestra un uso de memoria inicial más alto (102.5 MiB) y un incremento más alto durante la inserción.
- **Consistencia en el Proceso**: Aunque el uso de memoria en los archivos de inserción es similar, hay diferencias en los incrementos detallados en la línea 16, mostrando una variabilidad en la carga de memoria.

#### Conclusión
Este análisis permite visualizar cómo varía el uso de memoria durante el proceso de inserción y búsqueda en el B-tree. Identificar estas diferencias es crucial para la optimización y mejora de la gestión de memoria en aplicaciones de estructuras de datos complejas.



### **Conclusiones sobre la Optimización**

Las estrategias de **indexación** y **procesamiento eficiente** implementadas en el **Fashion B-Tree Recommender** aseguran que el sistema sea capaz de manejar grandes volúmenes de datos de manera eficiente y escalable. La combinación de **B-Trees** para **distancia euclidiana** y **Milvus** para **coseno de similitud** proporciona una base robusta para generar recomendaciones rápidas y precisas, adaptándose a las necesidades de los usuarios en tiempo real.

**Observaciones:**
- **Milvus** demuestra un excelente rendimiento en búsquedas de similitud con **coseno de similitud**, siendo más rápido en consultas similares que el B-Tree.
- **B-Trees** ofrecen tiempos de búsqueda rápidos para espacios de características de baja a moderada dimensionalidad.
- La combinación de **B-Trees** y **Milvus** permite un equilibrio entre eficiencia en inserciones y rapidez en búsquedas.


### **Optimización del Uso de Recursos**

#### **Gestión Eficiente de Memoria**

Se ha implementado una gestión cuidadosa de la memoria para asegurar que el sistema funcione de manera eficiente incluso con grandes volúmenes de datos. Esto incluye la utilización de estructuras de datos compactas y la liberación de recursos no utilizados de manera oportuna.

#### **Balanceo de Carga**

El sistema está diseñado para distribuir de manera equilibrada las solicitudes de recomendación entre los distintos componentes (**B-Trees** y **Milvus**), evitando cuellos de botella y asegurando un rendimiento consistente bajo cargas variables.



## **Pruebas y resultados**





## **Herramientas a utilizar**

### **Instalación**

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/usuario/nombre-repo.git
   cd nombre-repo
   ```
2. **Instalar las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

###**Dependencias**
El proyecto utiliza las siguientes bibliotecas:

- **sortedcontainers**: Implementación eficiente de contenedores ordenados.
- **pandas**: Manejo y manipulación de datos.
- **scikit-learn**: Herramientas para aprendizaje automático.
- **Pillow**: Manipulación de imágenes.

### **Uso del Sistema**

1. **Preparar el Dataset:**
   - Descarga y extrae el dataset desde [Kaggle](https://www.kaggle.com/datasets/paramaggarwal/fashion-product-images-dataset/data).
   - Asegúrate de que los archivos del dataset estén disponibles en la carpeta adecuada del proyecto.

2. **Ejecutar el sistema de recomendación:**
   - Carga el dataset con pandas.
   - Utiliza los algoritmos de filtrado por contenido y la estructura de árbol B para realizar las recomendaciones.


### **Ejemplo de Ejecución**

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
