# 🎬 Sistema de Recomendación de Películas - MovieLens

## ✅ Proyecto Completado

**Autores:** Marcos Llinares Montes, Ángel De Lorenzo Jerez  
**Asignatura:** Sistemas Inteligentes  
**Universidad:** Universidad de La Laguna

---

## 📦 Contenido del Proyecto

### Archivos Principales

| Archivo | Descripción | Uso |
|---------|-------------|-----|
| `config.py` | ⚙️ Configuración del sistema | Editar para cambiar dataset y algoritmos |
| `recommender.py` | 🚀 Script principal | `python recommender.py` |
| `quick_test.py` | ⚡ Prueba rápida | `python quick_test.py` |
| `view_results.py` | 📊 Visualización de resultados | `python view_results.py` |
| `compare_results.py` | 🔍 Comparación entre datasets | `python compare_results.py` |
| `utils.py` | 🛠️ Utilidades de gestión | `python utils.py` |

### Documentación

| Archivo | Contenido |
|---------|-----------|
| `README.md` | 📖 Documentación completa del proyecto |
| `GUIA_USO.md` | 📋 Guía rápida de referencia |
| `PROYECTO_INFO.py` | ℹ️ Información del proyecto |
| `config_examples.py` | 📝 10 ejemplos de configuración |
| `requirements.txt` | 📦 Dependencias Python |

---

## 🎯 Características Implementadas

### ✅ Algoritmos (11 implementados)

1. ✅ **NormalPredictor** - Baseline aleatorio
2. ✅ **BaselineOnly** - Modelo con sesgos
3. ✅ **KNNBasic** - K-vecinos básico
4. ✅ **KNNWithMeans** - K-vecinos con medias
5. ✅ **KNNWithZScore** - K-vecinos con Z-score
6. ✅ **KNNBaseline** - K-vecinos con baseline
7. ✅ **SVD** - Factorización matricial
8. ✅ **SVDpp** - SVD con retroalimentación implícita
9. ✅ **NMF** - Factorización no negativa
10. ✅ **SlopeOne** - Basado en diferencias
11. ✅ **CoClustering** - Agrupamiento

### ✅ Datasets Soportados

- ✅ **MovieLens 100k** (100,000 ratings)
- ✅ **MovieLens 32M** (32,000,000 ratings)

### ✅ Funcionalidades

- ✅ Configuración flexible por archivo `config.py`
- ✅ Selección de dataset (100k o 32M)
- ✅ Ejecución de todos los algoritmos o selección específica
- ✅ Validación cruzada configurable
- ✅ Ajuste de hiperparámetros por algoritmo
- ✅ Cálculo de métricas (RMSE, MAE)
- ✅ Medición de tiempos de ejecución
- ✅ Exportación de resultados a CSV
- ✅ Visualización detallada de resultados
- ✅ Comparación entre datasets
- ✅ Prueba rápida del sistema
- ✅ Ejemplos de configuración
- ✅ Utilidades de gestión de resultados
- ✅ Descarga automática de datasets

---

## 🚀 Inicio Rápido

### 1. Clonar y Preparar (Una sola vez)

```bash
# Clonar el repositorio
git clone https://github.com/marcosllinares/MovieLens-100k.git
cd MovieLens-100k

# Descargar datasets
python download_datasets.py

# Instalar dependencias
pip install -r requirements.txt
```

### 2. Prueba Rápida (10 segundos)

```bash
python quick_test.py
```

### 3. Evaluación Completa

**Opción A: Dataset 100k (Recomendado, ~15 minutos)**

Editar `config.py`:
```python
DATASET = '100k'
RUN_ALL_ALGORITHMS = True
```

Ejecutar:
```bash
python recommender.py
```

**Opción B: Dataset 32M (Avanzado, 2-8 horas)**

Editar `config.py`:
```python
DATASET = '32m'
RUN_ALL_ALGORITHMS = True
```

Ejecutar:
```bash
python recommender.py
```

### 4. Ver Resultados

```bash
python view_results.py
```

---

## 📊 Ejemplo de Resultados

Después de ejecutar `quick_test.py`:

```
================================================================================
RESUMEN DE RESULTADOS - MovieLens 100k
================================================================================

Algoritmo            RMSE            MAE             Tiempo (s)  
--------------------------------------------------------------------------------
SVD                  0.9446 ±0.0046  0.7455 ±0.0050  5.40        
BaselineOnly         0.9469 ±0.0046  0.7510 ±0.0040  2.70        
NormalPredictor      1.5228 ±0.0014  1.2233 ±0.0013  1.87        

================================================================================
Mejor algoritmo (por RMSE): SVD
RMSE: 0.9446
================================================================================
```

---

## 🎓 Casos de Uso

### Caso 1: Comparar variantes de KNN

```python
# En config.py:
DATASET = '100k'
RUN_ALL_ALGORITHMS = False
SELECTED_ALGORITHMS = ['KNNBasic', 'KNNWithMeans', 'KNNWithZScore', 'KNNBaseline']
```

### Caso 2: Optimizar SVD

```python
# En config.py:
DATASET = '100k'
RUN_ALL_ALGORITHMS = False
SELECTED_ALGORITHMS = ['SVD']
ALGORITHM_PARAMS = {
    'SVD': {
        'n_factors': 150,
        'n_epochs': 30,
        'lr_all': 0.005,
        'reg_all': 0.02
    }
}
```

### Caso 3: Comparar 100k vs 32M

```bash
# Paso 1: Evaluar 100k
# Editar config.py: DATASET = '100k'
python recommender.py

# Paso 2: Evaluar 32M
# Editar config.py: DATASET = '32m'
python recommender.py

# Paso 3: Comparar
python compare_results.py
```

---

## 📁 Estructura de Archivos de Salida

```
resultados/
├── resultados_100k.csv      # Resultados de MovieLens 100k
├── resultados_32m.csv       # Resultados de MovieLens 32M
└── comparacion_datasets.csv # Comparación entre datasets
```

### Formato de CSV

Cada archivo contiene:
- **Algorithm**: Nombre del algoritmo
- **RMSE_mean**: Error cuadrático medio promedio
- **MAE_mean**: Error absoluto medio promedio
- **Total_time**: Tiempo total de ejecución
- **Parameters**: Parámetros utilizados
- **Timestamp**: Fecha y hora de ejecución

---

## 🎯 Scripts de Ayuda

### Ver ejemplos de configuración
```bash
python config_examples.py
```

### Ver información del proyecto
```bash
python PROYECTO_INFO.py
```

### Gestionar resultados
```bash
python utils.py
```
- Ver información de resultados
- Crear backups
- Limpiar resultados antiguos

---

## ⏱️ Tiempos de Ejecución Estimados

| Tarea | Dataset | Tiempo |
|-------|---------|--------|
| Prueba rápida (3 algoritmos) | 100k | ~10 segundos |
| 1 algoritmo (5-fold CV) | 100k | ~1-2 minutos |
| Todos los algoritmos (5-fold CV) | 100k | ~15-20 minutos |
| 1 algoritmo (5-fold CV) | 32M | ~20-60 minutos |
| Todos los algoritmos (5-fold CV) | 32M | ~4-8 horas |

---

## 💡 Consejos

1. ✅ **Empieza con `quick_test.py`** para verificar que todo funciona
2. ✅ **Usa el dataset 100k** para experimentar y aprender
3. ✅ **Reduce CV_FOLDS a 3** si necesitas resultados más rápidos
4. ⚠️ **El dataset 32M requiere mucho tiempo** - planifica con anticipación
5. ✅ **SVD suele ser el mejor** balance entre precisión y velocidad
6. ✅ **Consulta `config_examples.py`** para configuraciones predefinidas

---

## 🔧 Tecnologías Utilizadas

- **Python 3.12**
- **scikit-surprise 1.1.1** - Librería de sistemas de recomendación
- **pandas** - Manejo de datos y resultados
- **numpy < 2.0** - Operaciones numéricas

---

## 📚 Referencias

- **Surprise Documentation**: https://surpriselib.com/
- **MovieLens Datasets**: https://grouplens.org/datasets/movielens/
- **Paper de referencia**: Harper & Konstan (2015) - The MovieLens Datasets

---

## ✅ Estado del Proyecto

| Componente | Estado |
|------------|--------|
| Implementación de algoritmos | ✅ Completo (11/11) |
| Soporte para datasets | ✅ Completo (2/2) |
| Sistema de configuración | ✅ Completo |
| Evaluación y métricas | ✅ Completo |
| Exportación de resultados | ✅ Completo |
| Visualización | ✅ Completo |
| Comparación entre datasets | ✅ Completo |
| Documentación | ✅ Completo |
| Pruebas | ✅ Verificado |

---

## 🎉 Proyecto Listo para Usar

El sistema está completamente funcional y documentado. Puedes:

1. ✅ Ejecutar evaluaciones en ambos datasets
2. ✅ Comparar diferentes algoritmos
3. ✅ Ajustar hiperparámetros
4. ✅ Exportar y analizar resultados
5. ✅ Crear configuraciones personalizadas

**¡Todo está listo para tu trabajo de Sistemas Inteligentes!**

---

**Última actualización:** 11 de Noviembre de 2025  
**Versión:** 1.0  
**Repositorio:** MovieLens-100k
