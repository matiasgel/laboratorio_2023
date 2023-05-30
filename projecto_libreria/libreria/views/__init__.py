#este paso lo realizo para cuando importe desde afuera pueda 
#importar directo del package y no tenga que referenciar el archivo
# sin esta linea debería importa de la forma "from libreria.views.autores import Autor"
# con esta linea importo de la forma "from libreria.views.views import Autor"
from .autores import AutoresList