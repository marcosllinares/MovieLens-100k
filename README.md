# Sistema de Recomendación de Películas - MovieLens

Sistema generalizado para evaluar todos los algoritmos de Surprise en datasets de MovieLens (100k y 32M).

**Autores:** Marcos Llinares Montes, Ángel De Lorenzo Jerez

## 📋 Descripción

Este proyecto implementa un sistema completo de evaluación de algoritmos de recomendación de películas utilizando la librería Surprise. Permite probar 11 algoritmos diferentes en dos datasets de MovieLens:

- **MovieLens 100k**: 100,000 ratings de 943 usuarios sobre 1,682 películas
- **MovieLens 32M**: 32 millones de ratings de 200,948 usuarios sobre 87,585 películas

## 🧠 Algoritmos Implementados

El sistema evalúa los siguientes algoritmos de Surprise:

1. **NormalPredictor** - Predicciones aleatorias (baseline)
2. **BaselineOnly** - Modelo de línea base con sesgos de usuario/ítem
3. **KNNBasic** - Filtrado colaborativo básico basado en vecinos
4. **KNNWithMeans** - KNN con normalización por media del usuario
5. **KNNWithZScore** - KNN con normalización Z-score
6. **KNNBaseline** - KNN con corrección de sesgos
7. **SVD** - Factorización matricial (Singular Value Decomposition)
8. **SVDpp** - SVD con retroalimentación implícita
9. **NMF** - Factorización matricial no negativa
10. **SlopeOne** - Algoritmo basado en diferencias entre ítems
11. **CoClustering** - Agrupamiento simultáneo de usuarios e ítems

## 📁 Estructura del Proyecto

```
Prueba-100k/
├── config.py              # Archivo de configuración
├── recommender.py         # Script principal
├── quick_test.py          # Script de prueba rápida
├── view_results.py        # Visualización detallada de resultados
├── compare_results.py     # Comparar resultados entre datasets
├── README.md             # Este archivo
├── requirements.txt      # Dependencias del proyecto
├── ml-100k/              # Dataset MovieLens 100k
│   ├── u.data            # Todos los ratings
│   ├── u.item            # Información de películas
│   └── ...
├── ml-32m/               # Dataset MovieLens 32M
│   ├── ratings.csv       # Todos los ratings
│   ├── movies.csv        # Información de películas
│   └── ...
└── resultados/           # Directorio de salida (se crea automáticamente)
    ├── resultados_100k.csv
    ├── resultados_32m.csv
    └── comparacion_datasets.csv
```

## 🚀 Instalación

### Requisitos Previos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### 1. Clonar el Repositorio

```bash
git clone https://github.com/marcosllinares/MovieLens-100k.git
cd MovieLens-100k
```

### 2. Descargar los Datasets

Los datasets no están incluidos en el repositorio. Usa el script de descarga automática:

```bash
python download_datasets.py
```

El script te permitirá elegir:
- Solo MovieLens 100k (~5 MB) - Recomendado para empezar
- Solo MovieLens 32M (~800 MB)
- Ambos datasets

**Nota:** El dataset 32M es muy grande y puede tardar varios minutos en descargarse.

### 3. Instalar Dependencias

```bash
pip install -r requirements.txt
```

O manualmente:

```bash
pip install pandas numpy scikit-surprise
```

## ⚙️ Configuración

Edita el archivo `config.py` para personalizar la ejecución:

### Seleccionar Dataset

```python
# Cambiar entre '100k' o '32m'
DATASET = '100k'  # Para el dataset pequeño (rápido)
DATASET = '32m'   # Para el dataset grande (más lento)
```

### Seleccionar Algoritmos

Para ejecutar **todos** los algoritmos:

```python
RUN_ALL_ALGORITHMS = True
```

Para ejecutar solo algoritmos específicos:

```python
RUN_ALL_ALGORITHMS = False
SELECTED_ALGORITHMS = [
    'NormalPredictor',
    'BaselineOnly',
    'SVD',
    'KNNBasic'
]
```

### Ajustar Validación Cruzada

```python
CV_FOLDS = 5  # Número de folds para cross-validation
```

### Configurar Parámetros de Algoritmos

Los parámetros de cada algoritmo se pueden ajustar en `ALGORITHM_PARAMS`:

```python
ALGORITHM_PARAMS = {
    'SVD': {
        'n_factors': 100,
        'n_epochs': 20,
        'lr_all': 0.005,
        'reg_all': 0.02
    },
    # ... otros algoritmos
}
```

## 🏃 Ejecución

### Prueba Rápida (Recomendado para Empezar)

Para hacer una prueba rápida del sistema con solo 3 algoritmos:

```bash
python quick_test.py
```

Esto ejecutará NormalPredictor, BaselineOnly y SVD en el dataset 100k con 3-fold CV.

### Ejecutar el Sistema Completo

```bash
python recommender.py
```

Esto ejecutará todos los algoritmos configurados según `config.py`.

### Visualizar Resultados Detallados

Para ver un análisis detallado de los resultados con estadísticas y rankings:

```bash
python view_results.py
```

Mostrará tablas formateadas con métricas, tiempos y rankings de los algoritmos.

### Comparar Resultados entre Datasets

Después de ejecutar el sistema con ambos datasets (100k y 32M), puedes comparar los resultados:

```bash
python compare_results.py
```

Esto generará un análisis comparativo y guardará `comparacion_datasets.csv`.

### Ejemplo de Salida

```
============================================================
 Sistema de Recomendación de Películas - MovieLens
 Evaluación de Algoritmos con Surprise
============================================================

============================================================
Cargando dataset: MovieLens 100k
============================================================

✓ Dataset cargado exitosamente
  - Número de ratings: 100000

============================================================
INICIO DE EVALUACIÓN
============================================================
Dataset: MovieLens 100k
Algoritmos a evaluar: 11
Validación cruzada: 5 folds
============================================================

[1/11] Procesando NormalPredictor...
------------------------------------------------------------
Evaluando: NormalPredictor
------------------------------------------------------------
...
```

## 📊 Resultados

Los resultados se guardan automáticamente en el directorio `resultados/`:

- `resultados_100k.csv` - Resultados para MovieLens 100k
- `resultados_32m.csv` - Resultados para MovieLens 32M

### Formato del CSV

Cada archivo contiene las siguientes columnas:

- **Algorithm**: Nombre del algoritmo
- **Dataset**: Dataset utilizado (100k o 32m)
- **RMSE_mean**: Error cuadrático medio promedio
- **RMSE_std**: Desviación estándar del RMSE
- **MAE_mean**: Error absoluto medio promedio
- **MAE_std**: Desviación estándar del MAE
- **Fit_time_mean**: Tiempo promedio de entrenamiento
- **Test_time_mean**: Tiempo promedio de prueba
- **Total_time**: Tiempo total de ejecución
- **CV_folds**: Número de folds utilizados
- **Parameters**: Parámetros del algoritmo
- **Timestamp**: Fecha y hora de la evaluación

### Resumen en Consola

Al finalizar, se muestra un resumen ordenado por RMSE:

```
================================================================================
RESUMEN DE RESULTADOS - MovieLens 100k
================================================================================

Algoritmo            RMSE            MAE             Tiempo (s)  
--------------------------------------------------------------------------------
SVD                  0.9340 ±0.0082  0.7351 ±0.0065  15.23       
SVDpp                0.9345 ±0.0079  0.7356 ±0.0063  45.67       
KNNBaseline          0.9425 ±0.0091  0.7425 ±0.0071  8.45        
...

================================================================================
Mejor algoritmo (por RMSE): SVD
RMSE: 0.9340
================================================================================
```

## ⏱️ Tiempo de Ejecución Estimado

- **MovieLens 100k**: ~5-15 minutos (todos los algoritmos)
- **MovieLens 32M**: ~2-8 horas (dependiendo del hardware)

💡 **Recomendación**: Comienza con el dataset 100k para probar el sistema, y luego usa el 32M si necesitas resultados más robustos.

## 🔧 Personalización Avanzada

### Modificar Métricas de Similitud (KNN)

```python
ALGORITHM_PARAMS = {
    'KNNBasic': {
        'k': 40,
        'sim_options': {
            'name': 'pearson',  # Opciones: cosine, msd, pearson
            'user_based': False  # True = user-based, False = item-based
        }
    }
}
```

### Ajustar Verbosidad

```python
VERBOSE = True   # Muestra detalles durante la ejecución
VERBOSE = False  # Solo muestra resultados finales
```

### El dataset 32M es muy lento

Esto es normal debido al tamaño. Puedes:
1. Reducir el número de folds: `CV_FOLDS = 3`
2. Seleccionar solo algunos algoritmos: `RUN_ALL_ALGORITHMS = False`
3. Ajustar parámetros para que los algoritmos sean más rápidos (menos épocas, menos factores)
