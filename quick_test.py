"""
Script de ejemplo rápido para probar el sistema
Ejecuta solo 3 algoritmos en el dataset 100k para verificación rápida
"""

import os
import sys

# Modificar temporalmente la configuración
import config
config.DATASET = '100k'
config.RUN_ALL_ALGORITHMS = False
config.SELECTED_ALGORITHMS = ['NormalPredictor', 'BaselineOnly', 'SVD']
config.CV_FOLDS = 3  # Menos folds para mayor velocidad
config.VERBOSE = False  # Menos output

# Importar y ejecutar el sistema
from recommender import MovieLensRecommender

def main():
    print("\n" + "="*60)
    print(" PRUEBA RÁPIDA DEL SISTEMA")
    print(" 3 algoritmos | 3-fold CV | Dataset 100k")
    print("="*60)
    
    recommender = MovieLensRecommender()
    recommender.load_data()
    recommender.run_all_evaluations()
    recommender.display_summary()
    recommender.save_results()
    
    print("\n✓ Prueba completada exitosamente!")
    print("  Ahora puedes modificar config.py para ejecutar todos los algoritmos")

if __name__ == "__main__":
    main()
