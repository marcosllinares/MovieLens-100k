"""
Script de utilidad para limpiar resultados antiguos
Útil cuando quieres empezar con evaluaciones frescas
"""

import os
import shutil
from config import OUTPUT_DIR


def clean_results():
    """
    Limpia el directorio de resultados
    """
    print("\n" + "="*60)
    print(" LIMPIAR RESULTADOS")
    print("="*60 + "\n")
    
    if not os.path.exists(OUTPUT_DIR):
        print(f"✓ El directorio {OUTPUT_DIR}/ no existe o ya está vacío")
        return
    
    # Listar archivos en el directorio
    files = [f for f in os.listdir(OUTPUT_DIR) if f.endswith('.csv')]
    
    if not files:
        print("✓ No hay archivos de resultados para limpiar")
        return
    
    print(f"Se encontraron {len(files)} archivos de resultados:")
    for f in files:
        file_path = os.path.join(OUTPUT_DIR, f)
        file_size = os.path.getsize(file_path)
        print(f"  - {f} ({file_size} bytes)")
    
    print()
    response = input("¿Deseas eliminar estos archivos? (s/N): ").strip().lower()
    
    if response == 's' or response == 'si' or response == 'sí':
        for f in files:
            file_path = os.path.join(OUTPUT_DIR, f)
            os.remove(file_path)
            print(f"✓ Eliminado: {f}")
        
        print(f"\n✓ Se eliminaron {len(files)} archivos")
        print(f"  El directorio {OUTPUT_DIR}/ está limpio\n")
    else:
        print("\n✗ Operación cancelada. No se eliminó ningún archivo\n")


def backup_results():
    """
    Crea una copia de seguridad de los resultados actuales
    """
    print("\n" + "="*60)
    print(" BACKUP DE RESULTADOS")
    print("="*60 + "\n")
    
    if not os.path.exists(OUTPUT_DIR):
        print("✗ No hay resultados para respaldar")
        return
    
    files = [f for f in os.listdir(OUTPUT_DIR) if f.endswith('.csv')]
    
    if not files:
        print("✗ No hay archivos de resultados para respaldar")
        return
    
    # Crear directorio de backup
    backup_dir = f"{OUTPUT_DIR}_backup"
    counter = 1
    while os.path.exists(backup_dir):
        backup_dir = f"{OUTPUT_DIR}_backup_{counter}"
        counter += 1
    
    os.makedirs(backup_dir)
    
    print(f"Creando backup en: {backup_dir}/")
    
    for f in files:
        src = os.path.join(OUTPUT_DIR, f)
        dst = os.path.join(backup_dir, f)
        shutil.copy2(src, dst)
        print(f"  ✓ Copiado: {f}")
    
    print(f"\n✓ Backup completado: {len(files)} archivos respaldados\n")


def show_results_info():
    """
    Muestra información sobre los resultados actuales
    """
    print("\n" + "="*60)
    print(" INFORMACIÓN DE RESULTADOS")
    print("="*60 + "\n")
    
    if not os.path.exists(OUTPUT_DIR):
        print("✗ No existe el directorio de resultados")
        return
    
    files = [f for f in os.listdir(OUTPUT_DIR) if f.endswith('.csv')]
    
    if not files:
        print("✗ No hay archivos de resultados")
        return
    
    print(f"Archivos en {OUTPUT_DIR}/:\n")
    
    import pandas as pd
    from datetime import datetime
    
    for f in files:
        file_path = os.path.join(OUTPUT_DIR, f)
        file_size = os.path.getsize(file_path) / 1024  # KB
        
        # Leer el CSV para obtener información
        df = pd.read_csv(file_path)
        
        print(f"📄 {f}")
        print(f"   Tamaño: {file_size:.2f} KB")
        print(f"   Registros: {len(df)}")
        
        if 'Timestamp' in df.columns and len(df) > 0:
            last_timestamp = df['Timestamp'].iloc[-1]
            print(f"   Última ejecución: {last_timestamp}")
        
        if 'Algorithm' in df.columns:
            algorithms = df['Algorithm'].unique()
            print(f"   Algoritmos: {len(algorithms)}")
        
        print()
    
    print("="*60 + "\n")


def main():
    """
    Menú principal
    """
    while True:
        print("\n" + "="*60)
        print(" UTILIDADES DE GESTIÓN DE RESULTADOS")
        print("="*60)
        print("\n1. Ver información de resultados")
        print("2. Crear backup de resultados")
        print("3. Limpiar resultados")
        print("4. Salir")
        print()
        
        choice = input("Selecciona una opción (1-4): ").strip()
        
        if choice == '1':
            show_results_info()
        elif choice == '2':
            backup_results()
        elif choice == '3':
            clean_results()
        elif choice == '4':
            print("\n✓ Saliendo...\n")
            break
        else:
            print("\n✗ Opción inválida. Intenta de nuevo.\n")


if __name__ == "__main__":
    main()
