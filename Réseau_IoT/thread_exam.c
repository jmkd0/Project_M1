#include	<stdio.h>
#include	<stdlib.h>
#include	<pthread.h>	
#define	N_Threads 15

void *func_1(int thread_id){	
    int	id	= (int)thread_id;	
    printf("Hello from thread	%d\n",	id);	
    return	NULL;	
    }	
int	main(){	
    pthread_t thread_ID[N_Threads];
    for(int	i = 0; i < N_Threads-1; i++){	
        pthread_create(&thread_ID[i], NULL, func_1, i);	
        
    }	
    for(int	i = 0; i < N_Threads-1; i++){

        pthread_join(thread_ID[i], NULL);
    }
return	EXIT_SUCCESS;	
}	