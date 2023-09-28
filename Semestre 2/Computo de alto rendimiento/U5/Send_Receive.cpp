/*El objetivo es hacer un programa paralelo que encadene el envío y recepción de un mensaje, en este caso el mensaje es el rango 
 * (id) del proceso que envía. Los mensajes se envian de forma encadenada, lo que quiere decir que el primero enviará 
 * un mensaje al segundo, el segundo recibirá uno del primero y enviará uno al tercero,  así sucesivamente para todos los procesos 
 * lanzados. Cada proceso que reciba un mensaje debe escribir en pantalla "Soy el proceso X y he recibido M", siendo X el rango 
 * del proceso y M el mensaje recibido.

Pistas
No olvides inicializar y finalizar las estructuras de paralelismo  (MPI_Init y MPI_Finalize).
Recuerda obtener el rango y el total de procesos participantes.
Recuerda que el último proceso no envía ningún mensaje.
Si observas  MPI_Send y MPI_Recv se puede especificar a quien se envía o de quien se recibe un mensaje. Estas funciones reciben 
* el mensaje siempre por referencia ( MPI_Send(&rank, .... ), MPI_Recv(&buzon, .... ) ).
funciones necesarias:
MPI_Init
MPI_Finalize
MPI_Comm_size
MPI_Comm_rank
MPI_Send
MPI_Recv

*/
#include "mpi.h"
#include <iostream>
using namespace std;
 
int main(int argc, char *argv[])
{
    int rank, contador;
    MPI_Status estado;
 
    MPI_Init(&argc, &argv); // Inicializamos la comunicacion de los procesos
    MPI_Comm_rank(MPI_COMM_WORLD, &rank); // Obtenemos el valor de nuestro identificador
 
    //Envia y recibe mensajes
    MPI_Send(&rank //referencia al vector de elementos a enviar
            ,1 // tamaño del vector a enviar
            ,MPI_INT // Tipo de dato que envias
            ,rank // pid del proceso destino
            ,0 //etiqueta
            ,MPI_COMM_WORLD); //Comunicador por el que se manda
 
    MPI_Recv(&contador // Referencia al vector donde se almacenara lo recibido
            ,1 // tamaño del vector a recibir
            ,MPI_INT // Tipo de dato que recibe
            ,rank // pid del proceso origen de la que se recibe
            ,0 // etiqueta
            ,MPI_COMM_WORLD // Comunicador por el que se recibe
            ,&estado); // estructura informativa del estado
 
	cout<< "Soy el proceso "<<rank<<" y he recibido "<<contador<<endl;
 
    MPI_Finalize();
    return 0;
}
