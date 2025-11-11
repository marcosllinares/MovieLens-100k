#!/usr/bin/env python3
"""
Script para descargar y descomprimir los datasets de MovieLens
Descarga automáticamente ml-100k y ml-32m desde los servidores de GroupLens
"""

import os
import urllib.request
import zipfile
import sys
from pathlib import Path


# URLs de descarga de los datasets
DATASETS = {
    '100k': {
        'url': 'https://files.grouplens.org/datasets/movielens/ml-100k.zip',
        'zip_file': 'ml-100k.zip',
        'extract_dir': 'ml-100k',
        'size': '~5 MB'
    },
    '32m': {
        'url': 'https://files.grouplens.org/datasets/movielens/ml-32m.zip',
        'zip_file': 'ml-32m.zip',
        'extract_dir': 'ml-32m',
        'size': '~800 MB'
    }
}


def download_file(url, destination, description):
    """
    Descarga un archivo con barra de progreso
    
    Args:
        url: URL del archivo a descargar
        destination: Ruta donde guardar el archivo
        description: Descripción del archivo
    """
    print(f"\nDescargando {description}...")
    print(f"URL: {url}")
    print(f"Destino: {destination}")
    
    def report_progress(block_num, block_size, total_size):
        downloaded = block_num * block_size
        if total_size > 0:
            percent = min(downloaded * 100 / total_size, 100)
            downloaded_mb = downloaded / (1024 * 1024)
            total_mb = total_size / (1024 * 1024)
            bar_length = 50
            filled = int(bar_length * percent / 100)
            bar = '█' * filled + '░' * (bar_length - filled)
            print(f'\r[{bar}] {percent:.1f}% ({downloaded_mb:.1f}/{total_mb:.1f} MB)', end='')
        else:
            downloaded_mb = downloaded / (1024 * 1024)
            print(f'\rDescargado: {downloaded_mb:.1f} MB', end='')
    
    try:
        urllib.request.urlretrieve(url, destination, reporthook=report_progress)
        print('\n✓ Descarga completada')
        return True
    except Exception as e:
        print(f'\n✗ Error en la descarga: {e}')
        return False


def extract_zip(zip_path, extract_to='.'):
    """
    Extrae un archivo ZIP
    
    Args:
        zip_path: Ruta del archivo ZIP
        extract_to: Directorio donde extraer
    """
    print(f"Extrayendo {zip_path}...")
    
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            # Obtener lista de archivos
            file_list = zip_ref.namelist()
            total_files = len(file_list)
            
            print(f"Extrayendo {total_files} archivos...")
            
            for i, file in enumerate(file_list, 1):
                zip_ref.extract(file, extract_to)
                if i % 10 == 0 or i == total_files:
                    percent = (i * 100) / total_files
                    print(f'\rProgreso: {percent:.1f}% ({i}/{total_files} archivos)', end='')
            
            print('\n✓ Extracción completada')
            return True
    except Exception as e:
        print(f'\n✗ Error en la extracción: {e}')
        return False


def download_dataset(dataset_key, keep_zip=False):
    """
    Descarga y extrae un dataset específico
    
    Args:
        dataset_key: Clave del dataset ('100k' o '32m')
        keep_zip: Si True, conserva el archivo ZIP después de extraer
    """
    dataset = DATASETS[dataset_key]
    
    print(f"\n{'='*70}")
    print(f"Dataset: MovieLens {dataset_key.upper()}")
    print(f"Tamaño aproximado: {dataset['size']}")
    print(f"{'='*70}")
    
    zip_file = dataset['zip_file']
    extract_dir = dataset['extract_dir']
    
    # Verificar si ya existe el directorio extraído
    if os.path.exists(extract_dir):
        print(f"\n⚠ El directorio {extract_dir}/ ya existe")
        response = input("¿Deseas descargarlo de nuevo? (s/N): ").strip().lower()
        if response not in ['s', 'si', 'sí', 'yes', 'y']:
            print("✓ Omitiendo descarga")
            return True
        else:
            print(f"Eliminando directorio existente...")
            import shutil
            shutil.rmtree(extract_dir)
    
    # Descargar el archivo ZIP
    if not download_file(dataset['url'], zip_file, f"MovieLens {dataset_key}"):
        return False
    
    # Extraer el archivo ZIP
    if not extract_zip(zip_file):
        return False
    
    # Eliminar el archivo ZIP después de extraer (si no se desea conservar)
    if not keep_zip:
        try:
            os.remove(zip_file)
            print(f"✓ Archivo {zip_file} eliminado")
        except Exception as e:
            print(f"⚠ No se pudo eliminar {zip_file}: {e}")
    else:
        print(f"✓ Archivo {zip_file} conservado")
    
    print(f"✓ Dataset {dataset_key} listo en {extract_dir}/")
    return True


def verify_dataset(dataset_key):
    """
    Verifica que el dataset esté correctamente descargado
    
    Args:
        dataset_key: Clave del dataset ('100k' o '32m')
    """
    dataset = DATASETS[dataset_key]
    extract_dir = dataset['extract_dir']
    
    if dataset_key == '100k':
        # Verificar archivos principales de ml-100k
        required_files = [
            os.path.join(extract_dir, 'u.data'),
            os.path.join(extract_dir, 'u.item'),
            os.path.join(extract_dir, 'u.user'),
        ]
    else:  # 32m
        # Verificar archivos principales de ml-32m
        required_files = [
            os.path.join(extract_dir, 'ratings.csv'),
            os.path.join(extract_dir, 'movies.csv'),
        ]
    
    missing = [f for f in required_files if not os.path.exists(f)]
    
    if missing:
        print(f"\n⚠ Archivos faltantes en {dataset_key}:")
        for f in missing:
            print(f"  - {f}")
        return False
    
    print(f"✓ Dataset {dataset_key} verificado correctamente")
    return True


def main():
    """
    Función principal
    """
    print("\n" + "="*70)
    print(" DESCARGADOR DE DATASETS MOVIELENS")
    print(" Sistema de Recomendación de Películas")
    print("="*70)
    
    print("\nEste script descargará los datasets de MovieLens necesarios:")
    print("  1. MovieLens 100k  (~5 MB)")
    print("  2. MovieLens 32M   (~800 MB)")
    
    print("\n⚠ ADVERTENCIA: El dataset 32M es muy grande y puede tardar varios minutos")
    print("   en descargarse dependiendo de tu conexión a Internet.")
    
    print("\n¿Qué datasets deseas descargar?")
    print("  1. Solo MovieLens 100k (recomendado para empezar)")
    print("  2. Solo MovieLens 32M")
    print("  3. Ambos datasets")
    print("  4. Salir")
    
    choice = input("\nSelecciona una opción (1-4): ").strip()
    
    datasets_to_download = []
    
    if choice == '1':
        datasets_to_download = ['100k']
    elif choice == '2':
        datasets_to_download = ['32m']
    elif choice == '3':
        datasets_to_download = ['100k', '32m']
    elif choice == '4':
        print("\n✓ Saliendo...")
        return
    else:
        print("\n✗ Opción inválida")
        return
    
    # Preguntar si desea conservar los archivos ZIP
    print("\n¿Deseas conservar los archivos ZIP después de extraerlos?")
    keep_response = input("Conservar ZIPs (s/N): ").strip().lower()
    keep_zip = keep_response in ['s', 'si', 'sí', 'yes', 'y']
    
    if keep_zip:
        print("✓ Los archivos ZIP se conservarán")
    else:
        print("✓ Los archivos ZIP se eliminarán después de extraer")
    
    # Descargar los datasets seleccionados
    success_count = 0
    for dataset_key in datasets_to_download:
        if download_dataset(dataset_key, keep_zip):
            if verify_dataset(dataset_key):
                success_count += 1
    
    # Resumen final
    print("\n" + "="*70)
    print(" RESUMEN")
    print("="*70)
    
    if success_count == len(datasets_to_download):
        print(f"\n✓ ¡Todos los datasets descargados exitosamente! ({success_count}/{len(datasets_to_download)})")
        print("\nAhora puedes ejecutar:")
        print("  python quick_test.py      # Prueba rápida")
        print("  python recommender.py     # Evaluación completa")
    else:
        print(f"\n⚠ Se descargaron {success_count} de {len(datasets_to_download)} datasets")
        print("  Algunos datasets no se descargaron correctamente")
    
    print("\n" + "="*70 + "\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n✗ Descarga interrumpida por el usuario")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Error inesperado: {e}")
        sys.exit(1)
