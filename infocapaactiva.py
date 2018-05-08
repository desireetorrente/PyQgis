#ACCEDE A LA CAPA ACTIVA
layer=qgis.utils.iface.mapCanvas().currentLayer()
#CONDICION IF - ELIF QUE EVALUA EL TIPO DE GEOMETRIA
#UTILIZANDO EL METODO .wkbType():
if layer.wkbType()==QGis.WKBPoint:
 print 'La capa activa es de tipo punto'
elif layer.wkbType()==QGis.WKBLineString:
 print 'La capa activa es de tipo linea'

elif layer.wkbType()==QGis.WKBPolygon:
 print 'La capa activa es de tipo poligono'

else:
 print 'La capa activa tiene otro formato'