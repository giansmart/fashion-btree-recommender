# **Sistema de Recomendación de Productos con BTree**

Este proyecto es un sistema de recomendación de productos utilizando **filtrado por contenido** y **árboles B** como estructura de datos. Se basa en el **Fashion Product Images Dataset** de Kaggle, el cual contiene información detallada sobre productos de moda.

- Dataset: [Fashion Product Images Dataset](https://www.kaggle.com/datasets/paramaggarwal/fashion-product-images-dataset/data)

## **Descripción del Proyecto**

El objetivo principal del proyecto es construir un sistema de recomendación que sugiera productos similares basados en las características de los productos, utilizando **filtrado por contenido**. Para almacenar y buscar eficientemente los productos, se utilizan **árboles B**.

### **Características del Proyecto**
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
df = pd.read_csv('ruta_al_dataset/styles.csv', nrows=1000)  # Cargar una muestra del dataset

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
├── src/                  # Código fuente del proyecto
├── requeriments.txt      # Dependencias del proyecto
├── README.md             # Este archivo
└── recommender.ipynb        # Jupyter Notebook con pruebas y análisis
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
