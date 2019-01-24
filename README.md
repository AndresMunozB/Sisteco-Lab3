Integrante: Andrés Muñoz 
            Diego Mellis
            Javier Arredondo

Como se ha pedido en el enunciado, se ha utilizado el algoritmo realizado en la experiencia anterior para generar el MAC.
Dentro de los aspectos importantes definidos para ese protocolo se tiene lo siguiente:
    -El tamaño del bloque puede ser variable.
    -El tamaño de salida del MAC es igual al tamaño del bloque.
Para generar el MAC se realizan los siguientes pasos:
    - Se agrega un relleno al texto de entrada para que pueda ser dividido  en bloques del mismo tamaño.
    - Se invierte el texto.
    - Se divide el texto en bloques.
    - Se realiza CBC utilizando el algoritmo realizadno en la experiencia anterior.
    - El resultado del ultimo bloque es el MAC.

El texto entregado por la encriptación es el resultado de la concatenacion de la encriptación misma del texto junto al generado.

Otra cosa a considerar es que al momento de desencriptar se entrega la información correspondiente de si el mensaje es auténtico.


