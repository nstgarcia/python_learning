list comprenhension sirve para construir una lista en una sola linea de codigo y es mas clara la intencion al crear la lista:

symbols='$¢£¥€¤'
codes=[]
for x in symbols:
    codes.append(x)

Con list comprenhension:

codes=[ ord(x) for x in symbols  ]
