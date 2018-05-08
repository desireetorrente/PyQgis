# -*- coding: utf-8 -*-
#hacemos la lista de las capas en el orden que queremos verlas
orden_capas = ['urbano', 'carreteras','vias','rios','ciudades','zona_estudio','marco']
#accedemos a la raiz del árbol de las capas
root = QgsProject.instance().layerTreeRoot()
#for para recorrer los nodos del árbol (capas)
for nodo in root.children():
    #comprobamos que nuestras capas estén entre los nodos 
    if nodo.layerName() in orden_capas:
        print "la capa está en la lista"
        #clonamos la capa y obtenemos su posición
        index = orden_capas.index(nodo.layerName())
        
        #clonamos el nodo que queremos cambiar
        clon = nodo.clone()
        
        #insertamos el nodo clonado en la posición que queremos
        root.insertChildNode(index, clon)
        #eliminamos el nodo original
        root.removeChildNode(nodo)
    