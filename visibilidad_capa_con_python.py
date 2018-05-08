# -*- coding: utf-8 -*-
#capturamos las capas en un grupo layers
#como queremos todas las capas, no sólo las activas, usamos iface
layers = iface.legendInterface().layers()
#capturamos el iface
legend = iface.legendInterface()

#lista de capas visibles
visibles=['vias', 'carreteras', 'rios', 'marco' , 'urbano']
#lista no visibles
no_visibles = ['zona_estudio', 'ciudades']

#ahora hacemos un for para recorrer las capas 
for layer in layers:
    print layer.name()
    #buscamos nuestras capas y lcambiamos la visibilidad
    if layer.name() in visibles and legend.isLayerVisible(layer) is False:
        #damos visibilidad a la capa
        legend.setLayerVisible(layer, True)
    if layer.name() in no_visibles and legend.isLayerVisible(layer) is True:
        legend.setLayerVisible(layer, False)
        


    