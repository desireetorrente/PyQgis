# -*- coding: utf-8 -*-
#accedemos a la capa activa
layer=qgis.utils.iface.mapCanvas().currentLayer()

#comprobamos geometría
if layer.wkbType()==QGis.WKBPoint:
    print 'La capa activa es de tipo punto'
    tipo = ' Point?'
    print tipo
 
elif layer.wkbType()==QGis.WKBLineString:
    print 'La capa activa es de tipo linea'
    tipo = ' LineString?'
    print tipo

elif layer.wkbType()==QGis.WKBPolygon:
    print ' La capa activa es de tipo poligono'
    tipo = 'Polygon?'
    print tipo

else:
    print 'La capa activa tiene otro formato'
 
#obtenemos el CRS
#como ya hemos accedido a la capa activa al pricipio,
#accedemos directamente al dataProvaider
layer_dp=layer.dataProvider()
#METODO crs() SOBRE EL DATA PROVIDER
layer_crs=layer_dp.crs()
#TRANSFORMA EL CRS EN UN STRING
layer_crs_str=layer_crs.authid()
print layer_crs_str
#OBTIENE EL NUM DEL IDENTIFICADOR EPGS
layer_EPSG_int=int (layer_crs_str[5:])
print layer_EPSG_int

#creamos la capa en memoria con las mismas características
capaDestino = QgsVectorLayer(tipo+ 'crs=epsg:'+str(layer_EPSG_int)+'&index=yes','memory layer','memory')
QgsMapLayerRegistry.instance().addMapLayer(capaDestino)
print"ok"
 