/*Paralelizar el calculo de la aproximación del numero PI indicando un factor de precisión. El numero PI es definido como la integral 0 a  *  1 de 4/(1+x*x), i.e, el área que forma.

Pistas

La aproximación de una integral mediante la suma de Riemann permite dividir el trabajo en unidades independientes, siendo un factor * de precision el numero de divisiones.

El factor de precisión lo solicita el proceso 0 y se distribuye entre los procesos mediante el uso de la función MPI_Bcast.

Despues de que cada proceso calcule su parte se reuniran todas las partes en el proceso 0 para mostrar el resultado * con MPI_Reduce.

Funciones necesarias:

MPI_Init
MPI_Finalize
MPI_Comm_size
MPI_Comm_rank
MPI_Bcast
MPI_Reduce

*/

#include <math.h>
#include <cstdlib> // Incluido para el uso de atoi
#include <iostream>
using namespace std;
 
int main(int argc, char *argv[]) 
{ 
 
	// Calculo de PI
        int n;
	cout<<"introduce la precision del calculo (n > 0): ";
	cin>>n;
	double PI25DT = 3.141592653589793238462643;
	double h = 1.0 / (double) n;
	double sum = 0.0;
	for (int i = 1; i <= n; i++) {
		double x = h * ((double)i - 0.5);
		sum += (4.0 / (1.0 + x*x));
	}
	double pi = sum * h;
	cout << "La aproximacion del valor de  PI es: " << pi << ", con un error de " << fabs(pi -PI25DT) << endl;
	return 0;
 
}
