# -*- coding: utf-8 -*-
#capturamos las capas en un grupo layers
#como queremos todas las capas, no sólo las activas, usamos iface

layers = iface.legendInterface().layers()

#ahora hacemos un for para recorrer las capas y activar rios
for layer in layers:
    print layer.name()
    if 'rios' in layer.name():
        #activamos la capa
        qgis.utils.iface.setActiveLayer(layer)
        print "La capa activa es %s"%(layer.name())
#como no va a salir activa en laTOC comrpobamos como se llama
capa_activa = qgis.utils.iface.activeLayer()
capa_activa.name()

    