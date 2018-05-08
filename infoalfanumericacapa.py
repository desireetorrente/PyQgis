#ACCEDE A LA CAPA ACTIVA
#CUENTA Y MUESTRA EL NUMERO DE ELEMENTOS DE LA CAPA
layer=qgis.utils.iface.mapCanvas().currentLayer()
print 'la capa tiene %s elementos' % (layer.featureCount())
#ACCEDE AL DATA PROVIDER DE LA CAPA Y OBTIENE CON EL LOS CAMPOS DE LA CAPA
layer_dp=layer.dataProvider()
layer_attrib_names = layer_dp.fields()
#CONVIERTE EL GRUPO DE CAMPOS (FIELDS) EN UN LISTADO
attributeList = layer_attrib_names.toList()
#RECORRE EL LISTADO DE CAMPOS Y PARA CADA UNO MUESTRA
#SU INFORMACION CON UN BUCLE FOR
for field in attributeList:
    print "Orden: %s, Nombre: %s, Tipo: %s, Longitud: %s" % (layer.fieldNameIndex(field.name()), field.name(),field.typeName(), field.length())
 #EVALUA EL TIPO DE CAMPO,SI ES ENTERO MUESTRA SU MAXIMO VALOR
if field.typeName() == 'Integer':
 print layer.maximumValue(layer.fieldNameIndex(field.name()))