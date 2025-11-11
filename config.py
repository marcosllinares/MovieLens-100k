"""
Configuración para el sistema de recomendación de películas
Permite seleccionar el dataset a utilizar y otros parámetros
"""

# ===== CONFIGURACIÓN DEL DATASET =====
# Opciones: '100k' o '32m'
DATASET = '100k'  # Cambiar a '32m' para usar el dataset más grande

# ===== RUTAS DE LOS DATASETS =====
DATASET_PATHS = {
    '100k': {
        'base': 'ml-100k/u1.base',
        'test': 'ml-100k/u1.test',
        'full': 'ml-100k/u.data',  # Archivo con todos los datos
    },
    '32m': {
        'ratings': 'ml-32m/ratings.csv',
    }
}

# ===== CONFIGURACIÓN DE LA EVALUACIÓN =====
# Número de folds para validación cruzada
CV_FOLDS = 5

# Métricas a calcular
METRICS = ['RMSE', 'MAE']

# ===== CONFIGURACIÓN DE LOS ALGORITMOS =====
# Si True, se ejecutan todos los algoritmos
# Si False, se ejecutan solo los especificados en SELECTED_ALGORITHMS
RUN_ALL_ALGORITHMS = True

# Lista de algoritmos a ejecutar (solo si RUN_ALL_ALGORITHMS = False)
SELECTED_ALGORITHMS = [
    'NormalPredictor',
    'BaselineOnly',
    'SVD',
]

# ===== CONFIGURACIÓN DE SALIDA =====
# Directorio donde guardar los resultados
OUTPUT_DIR = 'resultados'

# Nombre del archivo de resultados
RESULTS_FILE = f'resultados_{DATASET}.csv'

# Mostrar detalles durante la ejecución
VERBOSE = True

# ===== PARÁMETROS DE LOS ALGORITMOS =====
# Aquí se pueden ajustar los hiperparámetros de cada algoritmo
ALGORITHM_PARAMS = {
    'KNNBasic': {
        'k': 40,
        'min_k': 1,
        'sim_options': {
            'name': 'cosine',
            'user_based': True
        }
    },
    'KNNWithMeans': {
        'k': 40,
        'min_k': 1,
        'sim_options': {
            'name': 'cosine',
            'user_based': True
        }
    },
    'KNNWithZScore': {
        'k': 40,
        'min_k': 1,
        'sim_options': {
            'name': 'cosine',
            'user_based': True
        }
    },
    'KNNBaseline': {
        'k': 40,
        'min_k': 1,
        'sim_options': {
            'name': 'cosine',
            'user_based': True
        }
    },
    'SVD': {
        'n_factors': 100,
        'n_epochs': 20,
        'lr_all': 0.005,
        'reg_all': 0.02
    },
    'SVDpp': {
        'n_factors': 20,
        'n_epochs': 20,
        'lr_all': 0.007,
        'reg_all': 0.02
    },
    'NMF': {
        'n_factors': 15,
        'n_epochs': 50
    },
    'SlopeOne': {},
    'CoClustering': {
        'n_cltr_u': 3,
        'n_cltr_i': 3,
        'n_epochs': 20
    },
    'BaselineOnly': {
        'bsl_options': {
            'method': 'als',
            'n_epochs': 10
        }
    },
    'NormalPredictor': {}
}
