#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include <string.h>



// Déclaration du prototype avec argument
void *print_message_function(void *ptr);

void *print_message_function(void *ptr){
	char *message;
	message = (char *)ptr;
	printf("%s\n",message);
	pthread_exit(0);
	}


int main(){
	
	int i;
	
	// Déclaration du thread 1
    pthread_t thread1, thread2, thread3, thread4, thread5, thread6, thread7, thread8, thread9, thread10, thread11, thread12;

	char *message1 = "THREAD_1";
	char *message2 = "THREAD_2";
	char *message3 = "THREAD_3";
	char *message4 = "THREAD_4";
	char *message5 = "THREAD_5";
	char *message6 = "THREAD_6";
	char *message7 = "THREAD_7";
	char *message8 = "THREAD_8";
	char *message9 = "THREAD_9";
	char *message10 = "THREAD_10";
	char *message11 = "THREAD_11";
	char *message12 = "THREAD_12";
	
	
	for(i = 0; i<5 ; i++){
	// Création des THREADS

    pthread_create(&thread1,NULL,print_message_function,message1);
    pthread_create(&thread2,NULL,print_message_function,message2);  
    pthread_create(&thread3,NULL,print_message_function,message3);
    pthread_create(&thread4,NULL,print_message_function,message4);
    pthread_create(&thread5,NULL,print_message_function,message5);
    pthread_create(&thread6,NULL,print_message_function,message6);
    pthread_create(&thread7,NULL,print_message_function,message7);
    pthread_create(&thread8,NULL,print_message_function,message8);
    pthread_create(&thread9,NULL,print_message_function,message9);
    pthread_create(&thread10,NULL,print_message_function,message10);
    pthread_create(&thread11,NULL,print_message_function,message11);
    pthread_create(&thread12,NULL,print_message_function,message12);	
	
	// Exécution des THREADS

    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);
    pthread_join(thread3, NULL);
	pthread_join(thread4, NULL);
    pthread_join(thread5, NULL);
    pthread_join(thread6, NULL);
    pthread_join(thread7, NULL);
    pthread_join(thread8, NULL);
    pthread_join(thread9, NULL);
    pthread_join(thread10, NULL);
    pthread_join(thread11, NULL);
    pthread_join(thread12, NULL);
}
    return 0;

}



