#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>


// Déclaration du prototype sans argument
void *thread_1(void *arg);

// Fonction du THREAD de type "void * (* start_routine) (void *)"
void *thread_1(void *arg){
printf("Nous sommes dans le thread.\n");
pthread_exit(fact);
}


int main(void){
	
	// Déclaration du thread
    pthread_t thread1;
    printf("Avant la création du thread.\n");

	// initialisation et création du thread
    if (pthread_create(&thread1, NULL, thread_1, NULL)) {
	perror("pthread_create");
	return EXIT_FAILURE;
    }
    
	// Exécution du thread
    if (pthread_join(thread1, NULL)) {
	perror("pthread_join");
	return EXIT_FAILURE;
    }

    printf("Bloc : Après la création du thread.\n");

    return EXIT_SUCCESS;
}



