# TODO - Mejora Términos y Condiciones GymXtreme

## ✅ PLAN APROBADO
- [x] Plan detallado creado y aprobado por usuario
- [x] TODO.md creado

## 📋 PASOS DE IMPLEMENTACIÓN (7 total)

### 1. **Modelos** (usuarios/models.py)
- [x] Agregar `acepto_terminos` a Suscripcion
- [x] Agregar `acepto_terminos` a Venta

### 2. **Template principal** (confirmar_compra.html)
- [x] Modal profesional con términos completos
- [x] Checkbox obligatorio validado JS
- [x] Campo hidden para POST

### 3. **Backend Vistas** (usuarios/views.py)
- [x] confirmar_compra(): pasa términos
- [x] procesar_pago(): valida checkbox + guarda BD

### 4. **Migración**
- [ ] `makemigrations usuarios`
- [ ] `migrate`

### 5. **Template secundario** (pago_carrito.html)
- [ ] Mejora mínima para consistencia

### 6. **Testing**
- [ ] Probar /comprar/201/ completo
- [ ] Verificar BD guarda acepto_terminos=True

### 7. **Finalización**
- [ ] Update TODO.md ✅
- [ ] attempt_completion

**Estado actual: 3/7 completados (43%)**
**Próximo paso: Ejecutar migraciones**

