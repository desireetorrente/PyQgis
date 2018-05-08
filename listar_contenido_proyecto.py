# -*- coding: utf-8 -*-
#capturamos las capas en un grupo layers
#como queremos todas las capas, no sólo las activas, usamos iface
#si solo queremos la info de las capas activas usamos mapCanvas
#claters=qgs.utils.iface.mapCanvas().layers()
layers = iface.legendInterface().layers()

#ahora hacemos un for para recorrer las capas y sacar su nombre
for layer in layers:
    print layer.name()
