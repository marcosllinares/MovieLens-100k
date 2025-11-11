# Instrucciones para Descargar Datasets

## Script de Descarga Automática

Si has clonado este repositorio y los datasets no están presentes, usa el script de descarga automática:

```bash
python3 download_datasets.py
```
## Opciones Disponibles

El script te ofrecerá tres opciones:

1. **Solo MovieLens 100k** (~5 MB)
   - ✅ Recomendado para empezar
   - ✅ Descarga rápida (< 1 minuto)
   - ✅ Ideal para pruebas y aprendizaje

2. **Solo MovieLens 32M** (~800 MB)
   - ⚠️ Descarga grande
   - ⚠️ Puede tardar 5-15 minutos según tu conexión
   - ✅ Más datos para resultados robustos

3. **Ambos datasets** (~805 MB)
   - ⚠️ Descarga grande
   - ⚠️ Puede tardar 5-20 minutos
   - ✅ Permite comparar resultados entre datasets

## Estructura Esperada

Después de la descarga, deberías tener:

```
MovieLens-100k/
├── ml-100k/
│   ├── u.data
│   ├── u.item
│   ├── u.user
│   └── ...
└── ml-32m/
    ├── ratings.csv
    ├── movies.csv
    ├── tags.csv
    └── ...
```
