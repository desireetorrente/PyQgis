#CAPA DE PUNTOS
mem_layer_ptos = QgsVectorLayer("Point?crs=epsg:4326&field=id:integer""&field=nombre:string&index=yes", "capa_memory_ptos", "memory")

#CAPA DE LINEAS
mem_layer_line = QgsVectorLayer("LineString?crs=epsg:4326&field=id:integer""&field=longitud:double&index=yes", "capa_memory_line", "memory")

#CAPA DE POLIGONOS
mem_layer_poly = QgsVectorLayer("Polygon?crs=epsg:4326&field=id:integer""&field=area:double&index=yes","capa_memory_polig", "memory")

#CARGA LAS CAPAS EN LA TOC
QgsMapLayerRegistry.instance().addMapLayer(mem_layer_ptos)
QgsMapLayerRegistry.instance().addMapLayer(mem_layer_line)
QgsMapLayerRegistry.instance().addMapLayer(mem_layer_poly)