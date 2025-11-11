"""
Script para visualizar resultados de forma tabular mejorada
Muestra estadísticas detalladas de los algoritmos evaluados
"""

import pandas as pd
import os
from config import OUTPUT_DIR


def display_detailed_results(dataset_name):
    """
    Muestra resultados detallados de un dataset específico
    
    Args:
        dataset_name: '100k' o '32m'
    """
    file_path = os.path.join(OUTPUT_DIR, f'resultados_{dataset_name}.csv')
    
    if not os.path.exists(file_path):
        print(f"✗ No se encontró el archivo: {file_path}")
        print(f"  Ejecuta 'python recommender.py' con DATASET='{dataset_name}' en config.py")
        return
    
    df = pd.read_csv(file_path)
    
    # Filtrar errores si existen
    if 'Error' in df.columns:
        df_success = df[df['Error'].isna()].copy()
        df_errors = df[df['Error'].notna()].copy()
        
        if len(df_errors) > 0:
            print(f"\n⚠ Algoritmos con errores: {len(df_errors)}")
            for _, row in df_errors.iterrows():
                print(f"  - {row['Algorithm']}: {row['Error']}")
            print()
    else:
        df_success = df.copy()
    
    if len(df_success) == 0:
        print("✗ No hay resultados exitosos para mostrar")
        return
    
    print("\n" + "="*100)
    print(f" RESULTADOS DETALLADOS - MovieLens {dataset_name}")
    print("="*100 + "\n")
    
    # Ordenar por RMSE
    df_success = df_success.sort_values('RMSE_mean')
    
    # Tabla principal
    print("MÉTRICAS DE PREDICCIÓN")
    print("-" * 100)
    print(f"{'Rank':<6} {'Algoritmo':<18} {'RMSE':<20} {'MAE':<20} {'Params':<30}")
    print("-" * 100)
    
    for rank, (_, row) in enumerate(df_success.iterrows(), 1):
        rmse_str = f"{row['RMSE_mean']:.4f} ±{row['RMSE_std']:.4f}"
        mae_str = f"{row['MAE_mean']:.4f} ±{row['MAE_std']:.4f}"
        params = row.get('Parameters', 'N/A')
        if isinstance(params, str) and len(params) > 28:
            params = params[:25] + "..."
        
        medal = ""
        if rank == 1:
            medal = "🥇"
        elif rank == 2:
            medal = "🥈"
        elif rank == 3:
            medal = "🥉"
            
        print(f"{rank:<3} {medal:<3} {row['Algorithm']:<18} {rmse_str:<20} {mae_str:<20} {params:<30}")
    
    print("\n" + "-" * 100)
    
    # Estadísticas de tiempo
    print("\nTIEMPOS DE EJECUCIÓN")
    print("-" * 100)
    print(f"{'Algoritmo':<18} {'Tiempo Fit':<15} {'Tiempo Test':<15} {'Tiempo Total':<15}")
    print("-" * 100)
    
    # Ordenar por tiempo total
    df_by_time = df_success.sort_values('Total_time')
    
    for _, row in df_by_time.iterrows():
        fit_time = f"{row['Fit_time_mean']:.2f}s"
        test_time = f"{row['Test_time_mean']:.2f}s"
        total_time = f"{row['Total_time']:.2f}s"
        
        print(f"{row['Algorithm']:<18} {fit_time:<15} {test_time:<15} {total_time:<15}")
    
    # Resumen estadístico
    print("\n" + "="*100)
    print("RESUMEN ESTADÍSTICO")
    print("="*100)
    
    best_rmse = df_success.iloc[0]
    best_mae = df_success.sort_values('MAE_mean').iloc[0]
    fastest = df_by_time.iloc[0]
    slowest = df_by_time.iloc[-1]
    
    print(f"\n🏆 Mejor RMSE:    {best_rmse['Algorithm']} ({best_rmse['RMSE_mean']:.4f})")
    print(f"🏆 Mejor MAE:     {best_mae['Algorithm']} ({best_mae['MAE_mean']:.4f})")
    print(f"⚡ Más rápido:    {fastest['Algorithm']} ({fastest['Total_time']:.2f}s)")
    print(f"🐌 Más lento:     {slowest['Algorithm']} ({slowest['Total_time']:.2f}s)")
    
    print(f"\n📊 Estadísticas generales:")
    print(f"   - RMSE promedio: {df_success['RMSE_mean'].mean():.4f}")
    print(f"   - MAE promedio:  {df_success['MAE_mean'].mean():.4f}")
    print(f"   - Tiempo total:  {df_success['Total_time'].sum():.2f}s ({df_success['Total_time'].sum()/60:.2f} min)")
    print(f"   - Algoritmos evaluados: {len(df_success)}")
    print(f"   - Validación cruzada: {df_success['CV_folds'].iloc[0]} folds")
    
    print("\n" + "="*100 + "\n")


def main():
    """
    Función principal para mostrar resultados
    """
    print("\n" + "="*100)
    print(" VISUALIZACIÓN DE RESULTADOS - Sistema de Recomendación MovieLens")
    print("="*100)
    
    # Buscar datasets disponibles
    available = []
    
    if os.path.exists(os.path.join(OUTPUT_DIR, 'resultados_100k.csv')):
        available.append('100k')
    
    if os.path.exists(os.path.join(OUTPUT_DIR, 'resultados_32m.csv')):
        available.append('32m')
    
    if not available:
        print("\n✗ No se encontraron archivos de resultados")
        print("  Ejecuta primero 'python recommender.py' para generar resultados\n")
        return
    
    print(f"\nDatasets disponibles: {', '.join(available)}\n")
    
    # Mostrar resultados de cada dataset
    for dataset in available:
        display_detailed_results(dataset)


if __name__ == "__main__":
    main()
