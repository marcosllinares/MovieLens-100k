# Guía Rápida de Uso

## 📋 Resumen del Sistema

Este proyecto evalúa 11 algoritmos de recomendación de Surprise en datasets de MovieLens.

## 🚀 Inicio Rápido

### 0. Primera vez - Descargar datasets
```bash
python download_datasets.py
```
Selecciona los datasets que necesites (recomendado: empezar con 100k)

### 1. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 2. Prueba rápida (3 algoritmos, ~10 segundos)
```bash
python quick_test.py
```

### 3. Evaluación completa en 100k (~15 minutos)
Edita `config.py`:
```python
DATASET = '100k'
RUN_ALL_ALGORITHMS = True
```

Ejecuta:
```bash
python recommender.py
```

### 4. Ver resultados detallados
```bash
python view_results.py
```

## 📊 Scripts Disponibles

| Script | Descripción | Tiempo estimado |
|--------|-------------|-----------------|
| `download_datasets.py` | Descarga automática de datasets | 1-10 min (según dataset y conexión) |
| `quick_test.py` | Prueba rápida (3 algoritmos) | ~10 segundos |
| `recommender.py` | Evaluación completa configurable | 5-15 min (100k) / 2-8 horas (32M) |
| `view_results.py` | Visualización detallada de resultados | Instantáneo |
| `compare_results.py` | Comparación entre datasets | Instantáneo |
| `utils.py` | Gestión de resultados (backup, limpieza) | Instantáneo |

## ⚙️ Configuración Principal (config.py)

### Cambiar Dataset
```python
DATASET = '100k'  # o '32m'
```

### Seleccionar Algoritmos Específicos
```python
RUN_ALL_ALGORITHMS = False
SELECTED_ALGORITHMS = ['SVD', 'KNNBasic', 'BaselineOnly']
```

### Ajustar Validación Cruzada
```python
CV_FOLDS = 5  # Menos folds = más rápido, menos preciso
```

### Ajustar Parámetros de Algoritmo
```python
ALGORITHM_PARAMS = {
    'SVD': {
        'n_factors': 50,    # Menos factores = más rápido
        'n_epochs': 10,     # Menos épocas = más rápido
    }
}
```

## 📈 Interpretar Resultados

Los resultados se guardan en `resultados/resultados_{DATASET}.csv` con estas columnas:

- **RMSE_mean / MAE_mean**: Menor es mejor (precisión de predicción)
- **RMSE_std / MAE_std**: Menor es mejor (consistencia)
- **Fit_time_mean**: Tiempo de entrenamiento
- **Total_time**: Tiempo total de evaluación

### Mejores Algoritmos Generalmente:
1. **SVD** / **SVDpp** - Balance entre precisión y velocidad
2. **KNNBaseline** - Buena precisión, más lento
3. **BaselineOnly** - Rápido, baseline robusto

## 🔍 Ejemplos de Uso

### Ejemplo 1: Evaluar solo KNN en 100k
```python
# config.py
DATASET = '100k'
RUN_ALL_ALGORITHMS = False
SELECTED_ALGORITHMS = ['KNNBasic', 'KNNWithMeans', 'KNNWithZScore', 'KNNBaseline']
```

### Ejemplo 2: Evaluación rápida con menos folds
```python
# config.py
DATASET = '100k'
CV_FOLDS = 3  # Menos folds = más rápido
RUN_ALL_ALGORITHMS = True
```

### Ejemplo 3: Comparar 100k vs 32M
1. Ejecuta con `DATASET = '100k'`
2. Ejecuta con `DATASET = '32m'`
3. Ejecuta `python compare_results.py`

## ⚠️ Consideraciones

### Dataset 100k
- ✅ Rápido (5-15 minutos para todos los algoritmos)
- ✅ Ideal para prototipar y aprender
- ⚠️ Menos representativo que datasets grandes

### Dataset 32M
- ⚠️ Muy lento (2-8 horas según hardware)
- ✅ Más representativo de casos reales
- ✅ Mejores estimaciones de rendimiento

### Recomendaciones:
1. Empieza siempre con `quick_test.py`
2. Prueba con 100k antes de usar 32M
3. Ajusta `CV_FOLDS` si necesitas velocidad
4. Reduce parámetros (n_factors, n_epochs) para mayor velocidad

## 📝 Flujo de Trabajo Típico

```bash
# 1. Prueba rápida del sistema
python quick_test.py

# 2. Evaluación completa en 100k
# Editar config.py: DATASET = '100k'
python recommender.py

# 3. Ver resultados
python view_results.py

# 4. (Opcional) Evaluación en 32M
# Editar config.py: DATASET = '32m'
python recommender.py

# 5. (Opcional) Comparar datasets
python compare_results.py
```

## 🆘 Solución de Problemas

**Error: "FileNotFoundError"**
- Verifica que los datasets estén descomprimidos en `ml-100k/` y `ml-32m/`

**Error: "ModuleNotFoundError: surprise"**
- Ejecuta: `pip install scikit-surprise`

**El 32M es muy lento**
- Reduce `CV_FOLDS` a 3
- Reduce `n_epochs` en los parámetros de algoritmos
- Selecciona solo algunos algoritmos con `RUN_ALL_ALGORITHMS = False`

**Numpy compatibility error**
- Ejecuta: `pip install "numpy<2"`

## 📚 Más Información

Ver `README.md` para documentación completa.
