#!/usr/bin/env python
import os
import sys

# Configurar paths correctamente
project_root = r"c:\gym_django\gym_django\gym_dangoo (1)\gym_djangoo (1)\gym_django"
gym_root = os.path.join(project_root, 'gym')

sys.path.insert(0, project_root)
sys.path.insert(0, gym_root)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gym.settings')

import django
django.setup()

from productos.models import Categoria, Producto

# Diccionario de mapeo inteligente para categorías
CATEGORIA_MAP = {
    'suplementos': 'Suplementos',
    'suplemento': 'Suplementos',
    'vitaminas': 'Vitaminas',
    'vitamina': 'Vitaminas',
    'creatina': 'Creatinas',
    'creatinas': 'Creatinas',
    'proteina': 'Proteínas',
    'proteinas': 'Proteínas',
    'whey': 'Proteínas',
    'aminoacidos': 'Aminoácidos',
    'aminoácidos': 'Aminoácidos',
    'amino': 'Aminoácidos',
    'bcaas': 'Aminoácidos',
    'bcaa': 'Aminoácidos',
    'glutamina': 'Aminoácidos',
    'anabolicos': 'Anabólicos',
    'anabólicos': 'Anabólicos',
    'esteroides': 'Anabólicos',
    'testosterona': 'Anabólicos',
    'pre entreno': 'Pre-entreno',
    'pre-entrenamiento': 'Pre-entreno',
    'preentreno': 'Pre-entreno',
    'quemadores': 'Quemadores',
    'quemador': 'Quemadores',
    'fat burner': 'Quemadores',
    'termogenico': 'Quemadores',
    'termogénico': 'Quemadores',
    'maquinaria': 'Maquinaria',
    'equipo': 'Equipamiento',
    'equipamiento': 'Equipamiento',
    'accesorios': 'Accesorios',
    'guantes': 'Accesorios',
    'cinturones': 'Accesorios',
    'muñequeras': 'Accesorios',
    'rodilleras': 'Accesorios',
    'pesas': 'Pesas',
    'mancuernas': 'Pesas',
    'barras': 'Barras',
    'discos': 'Discos',
    'bebidas': 'Bebidas',
    'energia': 'Bebidas Energéticas',
    'energeticas': 'Bebidas Energéticas',
    'recuperacion': 'Recuperación',
    'recuperación': 'Recuperación',
    'salud': 'Salud',
    'general': 'General',
    'otros': 'Otros',
}

def normalizar_categoria(categoria_str):
    if not categoria_str:
        return 'Otros'
    norm = categoria_str.strip().lower()
    if norm in CATEGORIA_MAP:
        return CATEGORIA_MAP[norm]
    return norm.title()

def limpiar_categorias_duplicadas():
    """
    Limpia duplicados existentes en la base de datos.
    """
    categorias = Categoria.objects.all()
    grupos = {}

    for cat in categorias:
        # Aplicar normalización completa
        nuevo_nombre = normalizar_categoria(cat.nombre)
        
        if nuevo_nombre not in grupos:
            grupos[nuevo_nombre] = cat.id
        else:
            # Ya existe una categoría con este nombre normalizado
            categoria_principal_id = grupos[nuevo_nombre]
            # Reasignar productos a la categoría principal
            Producto.objects.filter(categoria=cat).update(categoria_id=categoria_principal_id)
            # Eliminar el duplicado
            cat.delete()
            print(f"Eliminada duplicada: {cat.nombre} (mantenida: {nuevo_nombre})")

    # Ahora actualizar nombres de categorías que cambien
    for nuevo_nombre, cat_id in grupos.items():
        cat = Categoria.objects.get(id=cat_id)
        if cat.nombre != nuevo_nombre:
            cat.nombre = nuevo_nombre
            cat.save()
            print(f"Normalizada: {cat.nombre}")

    print(f"✅ Categorías limpias y normalizadas: {len(grupos)}")

if __name__ == '__main__':
    limpiar_categorias_duplicadas()