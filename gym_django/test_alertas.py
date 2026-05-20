import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gym.settings')

import django
django.setup()

from productos.models import AlertaLote
resultado = AlertaLote.generar_alertas_automaticas()
print('Alertas creadas:', resultado[0])
print('Alertas actualizadas:', resultado[1])
print('Alertas desactivadas:', resultado[2])