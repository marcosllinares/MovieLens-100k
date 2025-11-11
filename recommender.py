"""
Sistema de Recomendación de Películas usando Surprise
Prueba todos los algoritmos de Surprise en datasets de MovieLens

Autores: Marcos Llinares Montes, Ángel De Lorenzo Jerez
"""

import os
import time
import pandas as pd
from datetime import datetime
from surprise import (
    Dataset, Reader,
    NormalPredictor, BaselineOnly,
    KNNBasic, KNNWithMeans, KNNWithZScore, KNNBaseline,
    SVD, SVDpp, NMF,
    SlopeOne, CoClustering
)
from surprise.model_selection import cross_validate
import config


class MovieLensRecommender:
    """
    Clase principal para entrenar y evaluar algoritmos de recomendación
    en datasets de MovieLens
    """
    
    def __init__(self):
        """Inicializa el sistema de recomendación"""
        self.dataset_name = config.DATASET
        self.data = None
        self.results = []
        
        # Diccionario con todos los algoritmos disponibles
        self.algorithms = {
            'NormalPredictor': NormalPredictor,
            'BaselineOnly': BaselineOnly,
            'KNNBasic': KNNBasic,
            'KNNWithMeans': KNNWithMeans,
            'KNNWithZScore': KNNWithZScore,
            'KNNBaseline': KNNBaseline,
            'SVD': SVD,
            'SVDpp': SVDpp,
            'NMF': NMF,
            'SlopeOne': SlopeOne,
            'CoClustering': CoClustering
        }
        
    def load_data(self):
        """
        Carga el dataset especificado en la configuración
        """
        print(f"\n{'='*60}")
        print(f"Cargando dataset: MovieLens {self.dataset_name}")
        print(f"{'='*60}\n")
        
        if self.dataset_name == '100k':
            self._load_100k()
        elif self.dataset_name == '32m':
            self._load_32m()
        else:
            raise ValueError(f"Dataset '{self.dataset_name}' no reconocido. Use '100k' o '32m'")
            
        print(f"✓ Dataset cargado exitosamente")
        print(f"  - Número de ratings: {len(self.data.raw_ratings)}")
        print()
        
    def _load_100k(self):
        """Carga el dataset MovieLens 100k"""
        # El formato de ml-100k es: user_id item_id rating timestamp (separado por tabs)
        file_path = config.DATASET_PATHS['100k']['full']
        
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"No se encuentra el archivo: {file_path}")
        
        # Definir el formato del Reader
        reader = Reader(line_format='user item rating timestamp', sep='\t', rating_scale=(1, 5))
        
        # Cargar el dataset desde archivo
        self.data = Dataset.load_from_file(file_path, reader=reader)
        
    def _load_32m(self):
        """Carga el dataset MovieLens 32m"""
        file_path = config.DATASET_PATHS['32m']['ratings']
        
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"No se encuentra el archivo: {file_path}")
        
        # Cargar el CSV
        df = pd.read_csv(file_path)
        
        # El formato de ml-32m es: userId, movieId, rating, timestamp
        reader = Reader(rating_scale=(0.5, 5.0))
        
        # Cargar desde el DataFrame
        self.data = Dataset.load_from_df(df[['userId', 'movieId', 'rating']], reader)
        
    def get_algorithms_to_run(self):
        """
        Retorna la lista de algoritmos a ejecutar según la configuración
        """
        if config.RUN_ALL_ALGORITHMS:
            return list(self.algorithms.keys())
        else:
            return config.SELECTED_ALGORITHMS
            
    def evaluate_algorithm(self, algo_name):
        """
        Evalúa un algoritmo específico usando validación cruzada
        
        Args:
            algo_name: Nombre del algoritmo a evaluar
            
        Returns:
            dict: Diccionario con los resultados de la evaluación
        """
        print(f"\n{'-'*60}")
        print(f"Evaluando: {algo_name}")
        print(f"{'-'*60}")
        
        # Obtener la clase del algoritmo
        algo_class = self.algorithms[algo_name]
        
        # Obtener los parámetros del algoritmo
        params = config.ALGORITHM_PARAMS.get(algo_name, {})
        
        # Instanciar el algoritmo con sus parámetros
        algo = algo_class(**params)
        
        # Medir tiempo de ejecución
        start_time = time.time()
        
        try:
            # Realizar validación cruzada
            cv_results = cross_validate(
                algo,
                self.data,
                measures=['RMSE', 'MAE'],
                cv=config.CV_FOLDS,
                verbose=config.VERBOSE
            )
            
            execution_time = time.time() - start_time
            
            # Importar numpy para calcular medias y desviaciones estándar
            import numpy as np
            
            # Calcular métricas promedio
            result = {
                'Algorithm': algo_name,
                'Dataset': self.dataset_name,
                'RMSE_mean': np.mean(cv_results['test_rmse']),
                'RMSE_std': np.std(cv_results['test_rmse']),
                'MAE_mean': np.mean(cv_results['test_mae']),
                'MAE_std': np.std(cv_results['test_mae']),
                'Fit_time_mean': np.mean(cv_results['fit_time']),
                'Test_time_mean': np.mean(cv_results['test_time']),
                'Total_time': execution_time,
                'CV_folds': config.CV_FOLDS,
                'Timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            
            # Agregar información de parámetros
            if params:
                result['Parameters'] = str(params)
            else:
                result['Parameters'] = 'Default'
                
            print(f"\n✓ Evaluación completada")
            print(f"  RMSE: {result['RMSE_mean']:.4f} (±{result['RMSE_std']:.4f})")
            print(f"  MAE:  {result['MAE_mean']:.4f} (±{result['MAE_std']:.4f})")
            print(f"  Tiempo total: {execution_time:.2f}s")
            
            return result
            
        except Exception as e:
            print(f"\n✗ Error al evaluar {algo_name}: {str(e)}")
            return {
                'Algorithm': algo_name,
                'Dataset': self.dataset_name,
                'Error': str(e),
                'Timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
    
    def run_all_evaluations(self):
        """
        Ejecuta la evaluación de todos los algoritmos seleccionados
        """
        algorithms_to_run = self.get_algorithms_to_run()
        
        print(f"\n{'='*60}")
        print(f"INICIO DE EVALUACIÓN")
        print(f"{'='*60}")
        print(f"Dataset: MovieLens {self.dataset_name}")
        print(f"Algoritmos a evaluar: {len(algorithms_to_run)}")
        print(f"Validación cruzada: {config.CV_FOLDS} folds")
        print(f"{'='*60}\n")
        
        total_start_time = time.time()
        
        for i, algo_name in enumerate(algorithms_to_run, 1):
            print(f"\n[{i}/{len(algorithms_to_run)}] Procesando {algo_name}...")
            result = self.evaluate_algorithm(algo_name)
            self.results.append(result)
            
        total_time = time.time() - total_start_time
        
        print(f"\n{'='*60}")
        print(f"EVALUACIÓN COMPLETADA")
        print(f"{'='*60}")
        print(f"Tiempo total: {total_time:.2f}s ({total_time/60:.2f} minutos)")
        print(f"Algoritmos evaluados: {len(self.results)}")
        print(f"{'='*60}\n")
        
    def save_results(self):
        """
        Guarda los resultados en un archivo CSV
        """
        # Crear directorio de salida si no existe
        if not os.path.exists(config.OUTPUT_DIR):
            os.makedirs(config.OUTPUT_DIR)
            
        # Crear DataFrame con los resultados
        df_results = pd.DataFrame(self.results)
        
        # Guardar en CSV
        output_path = os.path.join(config.OUTPUT_DIR, config.RESULTS_FILE)
        df_results.to_csv(output_path, index=False)
        
        print(f"✓ Resultados guardados en: {output_path}")
        
    def display_summary(self):
        """
        Muestra un resumen de los resultados
        """
        if not self.results:
            print("No hay resultados para mostrar")
            return
            
        df = pd.DataFrame(self.results)
        
        # Filtrar solo resultados exitosos (sin errores)
        if 'Error' in df.columns:
            df_success = df[df['Error'].isna()].copy()
        else:
            df_success = df.copy()
        
        if len(df_success) == 0:
            print("\n✗ No hay resultados exitosos para mostrar")
            print("Todos los algoritmos fallaron durante la evaluación")
            
            # Mostrar errores
            if 'Error' in df.columns:
                print("\nErrores encontrados:")
                for _, row in df[df['Error'].notna()].iterrows():
                    print(f"  - {row['Algorithm']}: {row['Error']}")
            return
            
        print(f"\n{'='*80}")
        print(f"RESUMEN DE RESULTADOS - MovieLens {self.dataset_name}")
        print(f"{'='*80}\n")
        
        # Ordenar por RMSE
        df_success = df_success.sort_values('RMSE_mean')
        
        print(f"{'Algoritmo':<20} {'RMSE':<15} {'MAE':<15} {'Tiempo (s)':<12}")
        print(f"{'-'*80}")
        
        for _, row in df_success.iterrows():
            rmse_str = f"{row['RMSE_mean']:.4f} ±{row['RMSE_std']:.4f}"
            mae_str = f"{row['MAE_mean']:.4f} ±{row['MAE_std']:.4f}"
            time_str = f"{row['Total_time']:.2f}"
            
            print(f"{row['Algorithm']:<20} {rmse_str:<15} {mae_str:<15} {time_str:<12}")
            
        print(f"\n{'='*80}")
        print(f"Mejor algoritmo (por RMSE): {df_success.iloc[0]['Algorithm']}")
        print(f"RMSE: {df_success.iloc[0]['RMSE_mean']:.4f}")
        print(f"{'='*80}\n")


def main():
    """
    Función principal
    """
    print("\n" + "="*60)
    print(" Sistema de Recomendación de Películas - MovieLens")
    print(" Evaluación de Algoritmos con Surprise")
    print("="*60)
    
    # Crear instancia del recomendador
    recommender = MovieLensRecommender()
    
    # Cargar datos
    recommender.load_data()
    
    # Ejecutar evaluaciones
    recommender.run_all_evaluations()
    
    # Mostrar resumen
    recommender.display_summary()
    
    # Guardar resultados
    recommender.save_results()
    
    print("\n¡Proceso completado!")


if __name__ == "__main__":
    main()
