#!/usr/bin/env python
"""
Script automático para arreglar la carga masiva de productos.
Ejecuta: cd "c:/gym_django/gym_dangoo (1)/gym_djangoo (1)/gym_django" && python ../../fix_carga_productos.py
"""

import os
import sys
import django
from pathlib import Path

# Configurar Django para ejecución desde gym_dangoo (1)/gym_djangoo (1)/gym_django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gym.settings')
django.setup()

# Añadir directorio padre si necesario
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))

from productos.models import Categoria, Producto
from django.db import transaction

def fix_productos():
    print("🔧 Arreglando carga de productos...")
    
    # 1. Crear todas las categorias del CSV
    categorias_csv = [
        'Suplementos', 'Vitaminas', 'Proteinas', 'Creatinas', 'Accesorios'
    ]
    creadas = []
    for nombre in categorias_csv:
        obj, created = Categoria.objects.get_or_create(nombre=nombre.strip())
        if created:
            creadas.append(nombre)
    
    print(f"✅ Categorias creadas/nombre: {len(creadas)} nuevas")
    
    # 2. Limpiar productos duplicados/rotos si existen
    eliminados = Producto.objects.filter(categoria__isnull=True).delete()[0]
    print(f"🗑️  Productos rotos eliminados: {eliminados}")
    
    print("🎉 Listo! Ahora ejecuta: python manage.py cargar_datos --todo")
    print("   Verifica con: python manage.py shell 'from productos.models import Producto; print(Producto.objects.count())'")

if __name__ == "__main__":
    fix_productos()

