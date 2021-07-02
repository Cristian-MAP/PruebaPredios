# PruebaPredios
Aplicación que permite registrar y administrar propietarios de predios y sus predios
Es una aplicación que realiza el CRUD para los predios y los propietarios.
Link Deploy: https://administrador-predios.herokuapp.com
Para probar el proyecto de manera local, cambiar, en el archivo wsgi y manage.py, la palabra "production" por la palabra "local"

Funcionamiento
Para agregar predios/propietarios:
1. Presionar el botón "Predios"/"Propietarios" en la barra de navegación superior
2. En el menú desplegable seleccionar "Agregar"
3. Llenar el formulario con los datos solicitados
4. Oprimir el botón "Agregar" en la parte inferior derecha
5. El predio/propietario quedó agregado

Para ver la lista de los predios/propietarios agregados:
1. Presionar el botón "Predios"/"Propietarios" en la barra de navegación superior
2. En el menú desplegable seleccionar "Listado"
3. La lista de predios/propietarios es mostrada

Para ver los detalles de cada predio/propietario:
1. Presionar el botón "Predios"/"Propietario" en la barra de navegación superior
2. En el menú desplegable seleccionar "Listado"
3. Oprimir el botón "Detalle" del predio/propietario el cual quiere ver en detalle
4. Muestra los detalles del predio/propietario seleccionado

Para actualizar/editar predio/propietario:
1. Hacer los pasos para ver los detalles de cada predio/propietario
2. Oprimir el Botón "Editar" en la parte inferior de los datos mostrados
3. Modificar los datos a cambiar.
4. Oprimir el botón "Guardar"
5. El predio/propietario ha sido actualizado

Para eliminar predio/propietario:
1. Presionar el botón "Predios"/"Propietario" en la barra de navegación superior
2. En el menú desplegable seleccionar "Listado"
3. Oprimir el botón "Eliminar" del predio/propietario a eliminar
4. Oprimir el botón "Eliminar" para confirmar la eliminación el predio/propietario
5. El predio/propietario ha sido eliminado

Para buscar/filtrar por nombre/cedula del propietario:
1. Presionar el botón "Propietarios" en la barra de navegación superior
2. En el menú desplegable seleccionar "Listado"
3. Escribir en los espacios indicados(bajo la barra de navegación superior) el nombre/cedula del propietario a buscar
4. Oprimir botón "Buscar"
5. Si se encuentra la búsqueda aparecerá en la tabla

Para buscar/filtrar por cédula catastral/dirección/tipo de predio:
1. Presionar el botón "Predios" en la barra de navegación superior
2. En el menú desplegable seleccionar "Listado"
3. Escribir en los espacios indicados(bajo la barra de navegación superior) cédula catastral/dirección/tipo de predio del predio a buscar/filtrar
4. Oprimir botón "Buscar"
5. Si se encuentra la búsqueda aparecerá en la tabla

Observaciones:
- Hace la búsqueda teniendo en cuenta los parámetros diligenciados en los espacios designados
- Primero agregar predios
- Una vez que se haya registrado predios, registrar los propietarios











