"""
Script para comparar resultados entre diferentes datasets
Útil para analizar el comportamiento de algoritmos en 100k vs 32M
"""

import pandas as pd
import os
from config import OUTPUT_DIR


def compare_results():
    """
    Compara los resultados de diferentes datasets si están disponibles
    """
    print("\n" + "="*80)
    print(" COMPARACIÓN DE RESULTADOS ENTRE DATASETS")
    print("="*80 + "\n")
    
    # Buscar archivos de resultados
    results_files = {}
    
    if os.path.exists(os.path.join(OUTPUT_DIR, 'resultados_100k.csv')):
        results_files['100k'] = pd.read_csv(os.path.join(OUTPUT_DIR, 'resultados_100k.csv'))
        print(f"✓ Encontrados resultados para MovieLens 100k")
        
    if os.path.exists(os.path.join(OUTPUT_DIR, 'resultados_32m.csv')):
        results_files['32m'] = pd.read_csv(os.path.join(OUTPUT_DIR, 'resultados_32m.csv'))
        print(f"✓ Encontrados resultados para MovieLens 32M")
    
    if len(results_files) == 0:
        print("✗ No se encontraron archivos de resultados")
        print("  Ejecuta primero 'python recommender.py' para generar resultados")
        return
    
    if len(results_files) == 1:
        dataset = list(results_files.keys())[0]
        print(f"\n⚠ Solo hay resultados para un dataset ({dataset})")
        print("  Para comparar, ejecuta el sistema con ambos datasets\n")
        
        # Mostrar solo los resultados disponibles
        df = results_files[dataset]
        if 'Error' in df.columns:
            df = df[df['Error'].isna()]
        
        if len(df) > 0:
            df_sorted = df.sort_values('RMSE_mean')
            print(f"\nResultados para MovieLens {dataset}:")
            print(f"\n{'Algoritmo':<20} {'RMSE':<15} {'MAE':<15}")
            print("-" * 50)
            
            for _, row in df_sorted.iterrows():
                print(f"{row['Algorithm']:<20} {row['RMSE_mean']:.4f}       {row['MAE_mean']:.4f}")
        return
    
    # Comparar resultados
    print(f"\n{'='*80}")
    print("COMPARACIÓN DE ALGORITMOS")
    print(f"{'='*80}\n")
    
    # Obtener algoritmos comunes
    algos_100k = set(results_files['100k']['Algorithm'])
    algos_32m = set(results_files['32m']['Algorithm'])
    common_algos = algos_100k.intersection(algos_32m)
    
    print(f"Algoritmos en común: {len(common_algos)}")
    print(f"Solo en 100k: {len(algos_100k - algos_32m)}")
    print(f"Solo en 32M: {len(algos_32m - algos_100k)}\n")
    
    # Crear tabla de comparación
    comparison_data = []
    
    for algo in sorted(common_algos):
        row_100k = results_files['100k'][results_files['100k']['Algorithm'] == algo].iloc[0]
        row_32m = results_files['32m'][results_files['32m']['Algorithm'] == algo].iloc[0]
        
        comparison_data.append({
            'Algorithm': algo,
            'RMSE_100k': row_100k['RMSE_mean'],
            'RMSE_32m': row_32m['RMSE_mean'],
            'RMSE_diff': row_32m['RMSE_mean'] - row_100k['RMSE_mean'],
            'MAE_100k': row_100k['MAE_mean'],
            'MAE_32m': row_32m['MAE_mean'],
            'MAE_diff': row_32m['MAE_mean'] - row_100k['MAE_mean'],
            'Time_100k': row_100k['Total_time'],
            'Time_32m': row_32m['Total_time']
        })
    
    df_comparison = pd.DataFrame(comparison_data)
    df_comparison = df_comparison.sort_values('RMSE_100k')
    
    # Mostrar tabla
    print(f"\n{'Algoritmo':<18} {'RMSE (100k)':<12} {'RMSE (32M)':<12} {'Diferencia':<12}")
    print("-" * 80)
    
    for _, row in df_comparison.iterrows():
        diff_symbol = "↓" if row['RMSE_diff'] < 0 else "↑"
        print(f"{row['Algorithm']:<18} {row['RMSE_100k']:<12.4f} {row['RMSE_32m']:<12.4f} "
              f"{diff_symbol} {abs(row['RMSE_diff']):<11.4f}")
    
    print(f"\n{'='*80}")
    
    # Encontrar mejor algoritmo para cada dataset
    best_100k = df_comparison.loc[df_comparison['RMSE_100k'].idxmin()]
    best_32m = df_comparison.loc[df_comparison['RMSE_32m'].idxmin()]
    
    print(f"\nMejor algoritmo en 100k: {best_100k['Algorithm']} (RMSE: {best_100k['RMSE_100k']:.4f})")
    print(f"Mejor algoritmo en 32M: {best_32m['Algorithm']} (RMSE: {best_32m['RMSE_32m']:.4f})")
    
    # Guardar comparación
    comparison_file = os.path.join(OUTPUT_DIR, 'comparacion_datasets.csv')
    df_comparison.to_csv(comparison_file, index=False)
    print(f"\n✓ Comparación guardada en: {comparison_file}")
    
    print(f"\n{'='*80}\n")


if __name__ == "__main__":
    compare_results()
