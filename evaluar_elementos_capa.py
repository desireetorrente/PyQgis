ListaCapas = ['carreteras_ETRS89','urbano_ED50','rios_ED50', 'provincias_ETRS89', 'caminos_ED50', 'ffcc_ED50' ]

CapasETRS89 = []
CapasED50 = []

for i in ListaCapas:
	if 'ETRS89' in i:
		CapasETRS89.append(i)
	else:
		CapasED50.append(i)

print "ETRS89 tiene" + str(len(CapasETRS89)) + "elementos"
print "ED50 tiene" + str(len(CapasED50)) + "elementos"