#!/usr/bin/env bash
# exit on error
set -o errexit

# Cambiar al directorio 'arquictectura'
cd arquictectura

# Instalar dependencias con pip
pip install -r requirements.txt

# Recopilar archivos estáticos
python manage.py collectstatic --noinput

# Migrar la base de datos
python manage.py migrate

# Volver al directorio original (opcional)

# Resto del script...
