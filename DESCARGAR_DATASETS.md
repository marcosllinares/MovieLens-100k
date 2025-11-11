# Instrucciones para Descargar Datasets

## 📥 Script de Descarga Automática

Si has clonado este repositorio y los datasets no están presentes, usa el script de descarga automática:

```bash
python download_datasets.py
```

## 📋 Opciones Disponibles

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

## ⚡ Descarga Manual (Alternativa)

Si prefieres descargar manualmente:

### MovieLens 100k
```bash
wget https://files.grouplens.org/datasets/movielens/ml-100k.zip
unzip ml-100k.zip
```

### MovieLens 32M
```bash
wget https://files.grouplens.org/datasets/movielens/ml-32m.zip
unzip ml-32m.zip
```

## 📊 Estructura Esperada

Después de la descarga, deberías tener:

```
Prueba-100k/
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

## 🔍 Verificación

Para verificar que los datasets se descargaron correctamente:

```bash
# Verificar ml-100k
ls -lh ml-100k/u.data

# Verificar ml-32m
ls -lh ml-32m/ratings.csv
```

## ❓ Problemas Comunes

### "Error al descargar"
- Verifica tu conexión a Internet
- Los servidores de GroupLens pueden estar temporalmente no disponibles
- Intenta de nuevo más tarde o descarga manualmente

### "Archivo corrupto"
- El script eliminará el archivo y puedes intentar de nuevo
- Asegúrate de tener suficiente espacio en disco

### "Sin espacio en disco"
- ml-100k necesita ~10 MB
- ml-32m necesita ~2 GB (incluido el archivo ZIP temporal)

## 📚 Más Información

- **Fuente oficial**: https://grouplens.org/datasets/movielens/
- **Documentación del proyecto**: Ver `README.md`
- **Guía de uso**: Ver `GUIA_USO.md`
