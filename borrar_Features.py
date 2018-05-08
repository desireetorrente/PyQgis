# -*- coding: utf-8 -*-
#CREAMOS UNA CAPA EN MEMORIA Y LA PREPARAMOS PARA EDITAR 
layer=qgis.utils.iface.mapCanvas().currentLayer()
layer.startEditing()
#CREAMOS UNA LISTA CON LAS CIUDADES QUE QUEREMOS ELIMINAR
ListaBorra = ["Topeka","Tulsa","Tupelo"]
#ACCEDEMOS A LA LISTA DE FEATURES Y LAS RECORREMOS
for feature in layer.getFeatures():
    #comparamos el nombre del feature con el de nuestra lista
    if feature['NAME'] in ListaBorra:
        #borra el feature que coincide
        layer.deleteFeature(feature.id())
#CIERRA EDICION GUARDANDO CAMBIOS
layer.commitChanges()