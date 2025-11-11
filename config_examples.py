"""
Ejemplos de configuraciones para diferentes casos de uso
Copia la configuración deseada en config.py
"""

# ============================================================================
# EJEMPLO 1: PRUEBA RÁPIDA CON DATASET 100K
# Tiempo estimado: ~10 minutos
# ============================================================================
EXAMPLE_1_QUICK_100K = {
    'DATASET': '100k',
    'RUN_ALL_ALGORITHMS': True,
    'CV_FOLDS': 3,
    'VERBOSE': False
}

# ============================================================================
# EJEMPLO 2: EVALUACIÓN COMPLETA Y PRECISA EN 100K
# Tiempo estimado: ~20 minutos
# ============================================================================
EXAMPLE_2_COMPLETE_100K = {
    'DATASET': '100k',
    'RUN_ALL_ALGORITHMS': True,
    'CV_FOLDS': 5,
    'VERBOSE': True
}

# ============================================================================
# EJEMPLO 3: SOLO ALGORITMOS KNN EN 100K
# Tiempo estimado: ~5 minutos
# Para comparar diferentes variantes de KNN
# ============================================================================
EXAMPLE_3_KNN_ONLY = {
    'DATASET': '100k',
    'RUN_ALL_ALGORITHMS': False,
    'SELECTED_ALGORITHMS': [
        'KNNBasic',
        'KNNWithMeans',
        'KNNWithZScore',
        'KNNBaseline'
    ],
    'CV_FOLDS': 5
}

# ============================================================================
# EJEMPLO 4: SOLO FACTORIZACIÓN MATRICIAL EN 100K
# Tiempo estimado: ~10 minutos
# Para comparar SVD, SVDpp y NMF
# ============================================================================
EXAMPLE_4_MATRIX_FACTORIZATION = {
    'DATASET': '100k',
    'RUN_ALL_ALGORITHMS': False,
    'SELECTED_ALGORITHMS': [
        'SVD',
        'SVDpp',
        'NMF'
    ],
    'CV_FOLDS': 5
}

# ============================================================================
# EJEMPLO 5: EVALUACIÓN RÁPIDA EN 32M
# Tiempo estimado: ~1-2 horas
# Solo algoritmos más eficientes
# ============================================================================
EXAMPLE_5_QUICK_32M = {
    'DATASET': '32m',
    'RUN_ALL_ALGORITHMS': False,
    'SELECTED_ALGORITHMS': [
        'BaselineOnly',
        'SVD',
        'NMF',
        'SlopeOne'
    ],
    'CV_FOLDS': 3,
    'VERBOSE': False
}

# ============================================================================
# EJEMPLO 6: EVALUACIÓN COMPLETA EN 32M
# Tiempo estimado: ~4-8 horas
# ADVERTENCIA: Requiere mucho tiempo de cómputo
# ============================================================================
EXAMPLE_6_COMPLETE_32M = {
    'DATASET': '32m',
    'RUN_ALL_ALGORITHMS': True,
    'CV_FOLDS': 5,
    'VERBOSE': True
}

# ============================================================================
# EJEMPLO 7: OPTIMIZACIÓN DE SVD EN 100K
# Tiempo estimado: ~30 segundos por configuración
# Para encontrar mejores hiperparámetros
# ============================================================================
EXAMPLE_7_SVD_TUNING = {
    'DATASET': '100k',
    'RUN_ALL_ALGORITHMS': False,
    'SELECTED_ALGORITHMS': ['SVD'],
    'CV_FOLDS': 3,
    'ALGORITHM_PARAMS': {
        'SVD': {
            'n_factors': 150,      # Probar con diferentes valores
            'n_epochs': 30,        # Más épocas = mejor ajuste
            'lr_all': 0.005,       # Tasa de aprendizaje
            'reg_all': 0.02        # Regularización
        }
    }
}

# ============================================================================
# EJEMPLO 8: COMPARACIÓN ITEM-BASED VS USER-BASED
# Tiempo estimado: ~8 minutos
# Para ver diferencias entre enfoques KNN
# ============================================================================
EXAMPLE_8_ITEM_VS_USER = {
    'DATASET': '100k',
    'RUN_ALL_ALGORITHMS': False,
    'SELECTED_ALGORITHMS': ['KNNBasic'],
    'CV_FOLDS': 5,
    'ALGORITHM_PARAMS': {
        'KNNBasic': {
            'k': 40,
            'sim_options': {
                'name': 'cosine',
                'user_based': False  # Cambiar a True para user-based
            }
        }
    }
}

# ============================================================================
# EJEMPLO 9: BASELINE COMPARISON
# Tiempo estimado: ~2 minutos
# Solo baselines y un algoritmo simple
# ============================================================================
EXAMPLE_9_BASELINE = {
    'DATASET': '100k',
    'RUN_ALL_ALGORITHMS': False,
    'SELECTED_ALGORITHMS': [
        'NormalPredictor',
        'BaselineOnly',
        'SVD'
    ],
    'CV_FOLDS': 3
}

# ============================================================================
# EJEMPLO 10: ALGORITMOS RÁPIDOS PARA PRODUCCIÓN
# Tiempo estimado: ~5 minutos
# Algoritmos con buen balance velocidad/precisión
# ============================================================================
EXAMPLE_10_PRODUCTION_READY = {
    'DATASET': '100k',
    'RUN_ALL_ALGORITHMS': False,
    'SELECTED_ALGORITHMS': [
        'BaselineOnly',
        'SVD',
        'SlopeOne',
        'CoClustering'
    ],
    'CV_FOLDS': 5,
    'ALGORITHM_PARAMS': {
        'SVD': {
            'n_factors': 50,       # Menos factores = más rápido
            'n_epochs': 15         # Balance precisión/velocidad
        }
    }
}


# ============================================================================
# INSTRUCCIONES DE USO
# ============================================================================
"""
Para usar una de estas configuraciones:

1. Copia el diccionario de ejemplo que quieras usar
2. Abre config.py
3. Actualiza los valores según el ejemplo

Por ejemplo, para usar EXAMPLE_1_QUICK_100K:

# En config.py:
DATASET = '100k'
RUN_ALL_ALGORITHMS = True
CV_FOLDS = 3
VERBOSE = False

Luego ejecuta:
    python recommender.py
"""


def print_examples():
    """Imprime todos los ejemplos disponibles"""
    examples = [
        ("PRUEBA RÁPIDA 100K", EXAMPLE_1_QUICK_100K, "~10 min"),
        ("EVALUACIÓN COMPLETA 100K", EXAMPLE_2_COMPLETE_100K, "~20 min"),
        ("SOLO KNN", EXAMPLE_3_KNN_ONLY, "~5 min"),
        ("FACTORIZACIÓN MATRICIAL", EXAMPLE_4_MATRIX_FACTORIZATION, "~10 min"),
        ("RÁPIDA 32M", EXAMPLE_5_QUICK_32M, "~1-2 horas"),
        ("COMPLETA 32M", EXAMPLE_6_COMPLETE_32M, "~4-8 horas"),
        ("OPTIMIZACIÓN SVD", EXAMPLE_7_SVD_TUNING, "~30 seg"),
        ("ITEM-BASED VS USER-BASED", EXAMPLE_8_ITEM_VS_USER, "~8 min"),
        ("BASELINE COMPARISON", EXAMPLE_9_BASELINE, "~2 min"),
        ("ALGORITMOS PRODUCCIÓN", EXAMPLE_10_PRODUCTION_READY, "~5 min"),
    ]
    
    print("\n" + "="*80)
    print(" EJEMPLOS DE CONFIGURACIÓN DISPONIBLES")
    print("="*80 + "\n")
    
    for i, (name, config, time) in enumerate(examples, 1):
        print(f"{i:2d}. {name:<30} Tiempo: {time}")
        print(f"    Dataset: {config['DATASET']}")
        if not config['RUN_ALL_ALGORITHMS']:
            algos = config.get('SELECTED_ALGORITHMS', [])
            print(f"    Algoritmos: {', '.join(algos[:3])}", end="")
            if len(algos) > 3:
                print(f" (+{len(algos)-3} más)")
            else:
                print()
        else:
            print(f"    Algoritmos: Todos (11)")
        print()
    
    print("="*80)
    print("\nVer detalles en config_examples.py")
    print("="*80 + "\n")


if __name__ == "__main__":
    print_examples()
