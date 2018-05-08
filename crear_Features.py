# -*- coding: utf-8 -*-
#CAPTURAMOS COMO LAYER LA CAPA ACTIVA PARA EDITARLA
layer = qgis.utils.iface.mapCanvas().currentLayer()
#PARA EMPEZAR A EDITAR LA CAPA HACEMOS:
layer.startEditing()
#CREAMOS UN FEATURE
feat = QgsFeature()
#APORTAMOS LA GEOMETRIA AL FEATURE A TRAVES DE UN QGSPOINT
feat.setGeometry(QgsGeometry.fromPoint(QgsPoint(-92,37)))
#APORTAMOS LOS ATRIBUROS DE LA LISTA AL FEATURE
feat.setAttributes(["MiCiudad","Estados Unidos"])
#INTRODUCIMOS EL FEATURE DENTRO DE LA CAPA A TRAVES DEL DATA PROVIDER
layer.dataProvider().addFeatures( [ feat ] )
#CERRAMOS LA EDICION GUARDANDO CAMBIOS
layer.commitChanges()