Actividad 2

Programadores: Cristina Ontiveros(Cristi1906) y Carlos S�nchez(Roy-maker)
Ac� se explican los cambios realizados en la actividad 2:

En el primer commit en la rama main se subi� el archivo README.txt y el c�digo
de snake original descargado de freegames. Este commit lo hizo Carlos.

En el segundo commit, Cristina hizo que la fruta se moviera aleatoriamente
hacia la derecha, izquierda, arriba, abajo, o que se quedara en su posici�n
poniendo las l�neas de c�digo de la 34 a la 50,esto li hizo en una branch
diferente y luego hizo el merge. De esta forma tiene una
posibilidad de moverse en las direcciones mencionadas anteriormente ya que se
us� un random.choice (para saber si el desplazamiento ser�a en x o en y) y un
randint (para saber si el desplazamiento ser�a positivo, negativo o nulo).
Adem�s se a�adi� un if que evita que la fruta se salga del espacio del juego.

En el tercer commit, Carlos cambi� las lineas del inicio desde la 12 hasta la
29 donde gener� una lista de colores que se puedan utilizar para la fruta y la
serpiente especificando que no pueden ser el mismo color. Esto s�lo se hace
una vez cada que se corre el c�digo por lo que cada vez que se reinicie el
juego hay una posibilidad de que toquen colores diferentes entre la lista de
cinco colores.

Finalmente, en el �ltimo commit, Carlos hizo un cambio en las l�neas 80 y 82 que
cambia los colores preestablecidos como negro y verde a algunos de los colores
aleatorios que se elijen antes por lo que se cambia es por col1 y col2 que son
las variables creadas para eso. Adem�s, se escribi� este README para poder
checar los cambios realizados.
