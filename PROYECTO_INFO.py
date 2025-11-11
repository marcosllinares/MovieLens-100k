"""
=============================================================================
SISTEMA DE RECOMENDACIÓN DE PELÍCULAS - MovieLens
=============================================================================

Autores: Marcos Llinares Montes, Ángel De Lorenzo Jerez
Universidad de La Laguna - Sistemas Inteligentes

=============================================================================
DESCRIPCIÓN DEL PROYECTO
=============================================================================

Este sistema evalúa 11 algoritmos de recomendación de la librería Surprise
en dos datasets de MovieLens:
  - MovieLens 100k: 100,000 ratings
  - MovieLens 32M:  32,000,000 ratings

Algoritmos implementados:
  1. NormalPredictor      - Predicciones aleatorias (baseline)
  2. BaselineOnly         - Modelo con sesgos usuario/ítem
  3. KNNBasic            - K-vecinos básico
  4. KNNWithMeans        - K-vecinos con normalización por media
  5. KNNWithZScore       - K-vecinos con normalización Z-score
  6. KNNBaseline         - K-vecinos con corrección de sesgos
  7. SVD                 - Factorización matricial
  8. SVDpp               - SVD con retroalimentación implícita
  9. NMF                 - Factorización matricial no negativa
  10. SlopeOne           - Basado en diferencias entre ítems
  11. CoClustering       - Agrupamiento de usuarios e ítems

=============================================================================
ARCHIVOS PRINCIPALES
=============================================================================

download_datasets.py   - Descargador automático de datasets (¡EMPIEZA AQUÍ!)
config.py              - Configuración del sistema (EDITAR AQUÍ)
recommender.py         - Script principal de evaluación
quick_test.py          - Prueba rápida (3 algoritmos)
view_results.py        - Visualización detallada de resultados
compare_results.py     - Comparación entre datasets
config_examples.py     - Ejemplos de configuración
utils.py               - Utilidades de gestión de resultados

README.md              - Documentación completa
GUIA_USO.md           - Guía rápida de uso
requirements.txt      - Dependencias del proyecto

=============================================================================
INICIO RÁPIDO
=============================================================================

0. Descargar datasets (PRIMERA VEZ):
   $ python download_datasets.py

1. Instalar dependencias:
   $ pip install -r requirements.txt

2. Prueba rápida (10 segundos):
   $ python quick_test.py

3. Evaluación completa en 100k (editar config.py primero):
   $ python recommender.py

4. Ver resultados:
   $ python view_results.py

5. Ver ejemplos de configuración:
   $ python config_examples.py

=============================================================================
CONFIGURACIÓN (config.py)
=============================================================================

CAMBIAR DATASET:
  DATASET = '100k'  # o '32m'

EJECUTAR TODOS LOS ALGORITMOS:
  RUN_ALL_ALGORITHMS = True

EJECUTAR ALGORITMOS ESPECÍFICOS:
  RUN_ALL_ALGORITHMS = False
  SELECTED_ALGORITHMS = ['SVD', 'KNNBasic', 'BaselineOnly']

AJUSTAR VALIDACIÓN CRUZADA:
  CV_FOLDS = 5  # Más folds = más preciso pero más lento

AJUSTAR PARÁMETROS:
  ALGORITHM_PARAMS = {
      'SVD': {
          'n_factors': 100,
          'n_epochs': 20,
      }
  }

=============================================================================
RESULTADOS
=============================================================================

Los resultados se guardan en:
  - resultados/resultados_100k.csv
  - resultados/resultados_32m.csv
  - resultados/comparacion_datasets.csv (después de compare_results.py)

Métricas principales:
  - RMSE (Root Mean Squared Error): Menor es mejor
  - MAE (Mean Absolute Error): Menor es mejor
  - Tiempos de ejecución

=============================================================================
FLUJO DE TRABAJO RECOMENDADO
=============================================================================

PASO 1: PRUEBA INICIAL
  $ python quick_test.py
  → Verifica que el sistema funciona (10 segundos)

PASO 2: EVALUACIÓN EN 100K
  Editar config.py:
    DATASET = '100k'
    RUN_ALL_ALGORITHMS = True
    CV_FOLDS = 5

  $ python recommender.py
  → Evalúa todos los algoritmos (~15 minutos)

PASO 3: ANALIZAR RESULTADOS
  $ python view_results.py
  → Muestra ranking y estadísticas

PASO 4 (OPCIONAL): EVALUACIÓN EN 32M
  Editar config.py:
    DATASET = '32m'
    RUN_ALL_ALGORITHMS = True
    CV_FOLDS = 5

  $ python recommender.py
  → Evalúa en dataset grande (2-8 horas)

PASO 5 (OPCIONAL): COMPARAR
  $ python compare_results.py
  → Compara resultados entre datasets

=============================================================================
CONSEJOS Y RECOMENDACIONES
=============================================================================

✓ Empieza siempre con quick_test.py
✓ Usa el dataset 100k para experimentar
✓ Reduce CV_FOLDS a 3 si necesitas velocidad
✓ Reduce n_epochs y n_factors para algoritmos más rápidos
✓ El dataset 32M requiere MUCHO tiempo (planifica con anticipación)
✓ SVD y BaselineOnly son buenos puntos de partida
✓ KNN algorithms son más lentos pero muy interpretables

=============================================================================
TIEMPO ESTIMADO DE EJECUCIÓN
=============================================================================

Dataset 100k:
  - quick_test.py:         ~10 segundos
  - 1 algoritmo (5-fold):  ~1-2 minutos
  - Todos (5-fold):        ~15-20 minutos

Dataset 32M:
  - 1 algoritmo (5-fold):  ~20-60 minutos
  - Todos (5-fold):        ~4-8 horas
  - Reducir a 3-fold ayuda, pero sigue siendo lento

=============================================================================
SOLUCIÓN DE PROBLEMAS
=============================================================================

"FileNotFoundError: u.data or ratings.csv"
  → Verifica que los datasets estén descomprimidos en ml-100k/ y ml-32m/

"ModuleNotFoundError: No module named 'surprise'"
  → Ejecuta: pip install scikit-surprise

"numpy.core.multiarray failed to import"
  → Ejecuta: pip install "numpy<2"

"El dataset 32M es muy lento"
  → Reduce CV_FOLDS a 3
  → Selecciona menos algoritmos
  → Reduce parámetros (n_epochs, n_factors)

"No se encuentran los resultados"
  → Los archivos CSV se crean en el directorio resultados/
  → Verifica que recommender.py se ejecutó correctamente

=============================================================================
ESTRUCTURA DE SALIDA (CSV)
=============================================================================

Columnas en resultados_*.csv:
  - Algorithm:       Nombre del algoritmo
  - Dataset:         '100k' o '32m'
  - RMSE_mean:       RMSE promedio
  - RMSE_std:        Desviación estándar del RMSE
  - MAE_mean:        MAE promedio
  - MAE_std:         Desviación estándar del MAE
  - Fit_time_mean:   Tiempo promedio de entrenamiento
  - Test_time_mean:  Tiempo promedio de prueba
  - Total_time:      Tiempo total de ejecución
  - CV_folds:        Número de folds usados
  - Timestamp:       Fecha y hora de ejecución
  - Parameters:      Parámetros usados

=============================================================================
DOCUMENTACIÓN ADICIONAL
=============================================================================

README.md          - Documentación completa y detallada
GUIA_USO.md        - Guía rápida de referencia
config_examples.py - 10 ejemplos de configuración

Librería Surprise: https://surpriselib.com/
MovieLens:         https://grouplens.org/datasets/movielens/

=============================================================================
CONTACTO
=============================================================================

Marcos Llinares Montes
Ángel De Lorenzo Jerez

Universidad de La Laguna
Sistemas Inteligentes

=============================================================================
"""

if __name__ == "__main__":
    print(__doc__)
