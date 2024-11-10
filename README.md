# **Sistema de Recomendación de Productos: Caso Fashion Product Images Dataset **

## Tabla de Contenidos
1. [Descripción General](#descripción-general)
2. [Objetivos del Proyecto](#objetivos-del-proyecto)
3. [Estructuras de Datos Utilizadas](#estructuras-de-datos-utilizadas)
4. [Algoritmos de Recomendación](#algoritmos-de-recomendación)
   - [Filtrado Basado en Contenido](#filtrado-basado-en-contenido)
5. [Eficiencia y Optimización](#eficiencia-y-optimización)
6. [Similitud de Usuarios y Productos](#similitud-de-usuarios-y-productos)
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

- **Filtrado por Contenido:** Se basa en la similitud de características como el tipo de producto, color, género, etc.
- **Dataset:** Contiene imágenes y metadatos como `id`, `gender`, `productDisplayName` y `baseColour`.
- **Árboles B:** Se utilizan para optimizar las búsquedas rápidas de productos dentro del dataset.

---

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
