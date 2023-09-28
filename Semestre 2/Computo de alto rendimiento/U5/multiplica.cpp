/*
Realizar la multiplicación paralela de una matriz (NxN) con un vector (Nx1).

En este problema descomponemos la matriz A en filas, una por cada proceso. 
Por lo tanto, cada proceso tendrá una fila de la matriz y el vector por el que se va a multiplicar.
1.	El poceso 0 genera la matriz A y el vector x.
2.	La matriz A es distribuida (MPI_Scatter), y el vector difundido (MPI_Bcast).
3.	Cada proceso opera con los datos que tiene.
4.	Se reconstruye el vector solución en el proceso 0 mediante MPI_Gather.

Pistas:
Recuerda que el numero de filas de la matriz (que va a coincidir con su número de columnas, al asumirse que la matriz es cuadrada) 
debe ser igual al numero de procesos disponibles.
Cada proceso obtendrá como resultado un número, que al juntarlos (MPI_Gather) en el proceso 0 forman el vector solución.
Gracias a MPI_Wtime podemos tomar tiempos, pero hay que tener en cuenta que los tiempos son locales a un proceso, quizás te interesaría tomar tiempos asegurando que todos los procesos han tardado lo mismo, con MPI_Barrier fuerzas un punto de sincronización o 
reunión de todos los procesos del comunicador.

Funciones necesarias:
MPI_Init
MPI_Finalize
MPI_Comm_size
MPI_Comm_rank
MPI_Barrier
MPI_Wtime
MPI_Gather
MPI_Scatter
MPI_Bcast
*/

#include <iostream>
#include <cstdlib>
#include <ctime>
 
using namespace std;
 
int main(int argc, char * argv[]) {
 
    long **A, // Matriz a multiplicar
	 *x, // Vector que vamos a multiplicar
	 *comprueba; // Guarda el resultado final (calculado secuencialmente), su valor
 
    int n;
 
    if (argc <= 1) {// si no se pasa por parametro el tamaño de la matriz, 
                    //se coge por defecto el numero de procesadores
        cout << "Falta el tamanio de la matriz, por defecto cogemos 10"<< endl;
        n = 10;
    } else 
        n = atoi(argv[3]); 
 
	A = new long *[n];//reservamos espacio para las n filas de la matriz.
	x = new long [n];//reservamos espacio para el vector.
 
    //Rellena la matriz
    A[0] = new long [n * n];
    for (unsigned int i = 1; i < n; i++) {
	A[i] = A[i - 1] + n;
    }
 
    // Rellena A y x con valores aleatorios
    srand(time(0));
    cout << "La matriz y el vector generados son " << endl;
    for (unsigned int i = 0; i < n; i++) {
	for (unsigned int j = 0; j < n; j++) {
	    if (j == 0) cout << "[";
	    A[i][j] = rand() % 1000;
	    cout << A[i][j];
	    if (j == n - 1) cout << "]";
	    else cout << "  ";
	}
	x[i] = rand() % 100;
	cout << "\t  [" << x[i] << "]" << endl;
    }
    cout << "\n";
 
    comprueba = new long [n];
    //Calculamos la multiplicacion secuencial para 
    //despues comprobar que es correcta la solucion.
    for (unsigned int i = 0; i < n; i++) {
	comprueba[i] = 0;
	for (unsigned int j = 0; j < n; j++) {
	    comprueba[i] += A[i][j] * x[j];
	}
    }
  
    cout << "El resultado obtenido y el esperado son:" << endl;
    for (unsigned int i = 0; i < n; i++) {
	cout << comprueba[i] << endl;
    }
 
    delete [] comprueba;
    delete [] A[0]; 
    delete [] x;
    delete [] A; 
    return 0;
 
}
