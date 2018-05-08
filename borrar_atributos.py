# -*- coding: utf-8 -*-
from PyQt4.QtCore import QVariant
#CAPTURAMOS COMO LAYER LA CAPA ACTIVA
layer= qgis.utils.iface.mapCanvas().currentLayer()
#ACCEDEMOS AL DATAPROVIDER Y BORRA LOS CAMPOS DE LA LISTA
layer.dataProvider().deleteAttributes([0,1])
#ACTUALIZAMOS LA CAPA
layer.updateFields()