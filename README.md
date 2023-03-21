# BNE lab

### 6-3-2023

1. Fichero mrc para extraer datos (menor peso a mrc-xml)
2. Conversión unitaria de registro a diccionario
3. ? Guardar datos en colección de datos asociativa: **set**, **dict** ordenada: **tuple**
4. Las etiquetas con coincidencia (024) serán almacenadas de la siguiente manera -> \<tag>:[1,2...]

### 7-3-2023

1. Solicitud a catálogo para emitir mrc con etiquetas incluidas en texto plano
2. csv mapper realizado
3. Implementación del QMO (Query Marc Object)
4. Prueba satisfactoria esquematización de 1.5KK
5. Consulta por valor en tag
6. Filtrar por ausencia de etiqueta
7. Funcionamiento correcto en diferentes tipos de registros (persona, geográfico)

### 8-3-2023

1. Selección de ficheros

### 16-3-2023

1. Enric. en 43307 registros de autoría
* Todos los registros con $0 en la casilla 307 fueron enriquecidos con la casilla 781 de geográfico
* Solicitud a catálogo
2. Multi query funcionando correctamente
3. Prueba no satisfactoria realizada en obras (3.5KK, 3.5GB)
* Si bien los registros pueden ser esquematizados, la subida es lenta
* Se invesitgará multi-procesamiento
