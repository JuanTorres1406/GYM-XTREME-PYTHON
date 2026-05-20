# TODO - Arreglo carga masiva productos

✅ [DONE] Fix categorias ForeignKey en csv_import.py  
✅ [DONE] Script fix_carga_productos.py creado  

🔄 **PENDIENTE: Fix imágenes carga WEB**
- Leer gym/gym/csv_import.py completo (ya pegado por usuario)
- Editar `importar_productos_desde_csv()` para:
  * Leer columna 'imagen' del CSV
  * Copiar archivos desde gym/csv_datos/*.jpg → media/productos/
  * Asignar ImageField correctamente
- Test: Subir CSV web → verificar productos + imágenes en admin

**Próximo paso:** Editar csv_import.py con diff preciso
