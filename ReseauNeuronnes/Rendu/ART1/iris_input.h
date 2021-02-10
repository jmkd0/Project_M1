#ifndef __IRIS__H_
#define __ISIS__H_

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include <float.h>

#define TRUE    1
#define FALSE   0

struct Size{
    int     columnIris;                                     /* taille de vecteur d'un iris: 4 */
    int     lineIris;                                      /* nombre totale d'iris:   150    */
}size;

typedef struct{
    double*     dataIris;                 /* contient les données brutes       */
    double*     normalized;              /* contient les données normalisées  */
    char*       nameIris;               /* contient les noms des iris        */
    int         label;
    int         predict_label;
}DataIris;

struct Params{
    double vigilance; /*Vigilence parameter*/
    int learning_rate; /* Learning rate*/
    int number_feature;
    int number_cluster;
    int epoch;
} param = {.vigilance=0.9, .learning_rate=2, .number_feature=4, .number_cluster=3, .epoch=1};
//{.vigilance=0.4, .learning_rate=2, .number_feature=4, .number_cluster=3, .epoch=100};

typedef struct{
    double** bottom_up;
    double** top_down;
}Weights;

typedef struct{
    double* X;
    double* Y;
    int*    inhibited;
}Activation;

//Function to find the size (line and column ) of datas in database
void set_size_data_iris (char* fileName){
    int     line = 0, column = 0;
    char*   chaine; 
    int     lineSize = 100;
    char*   ligne = (char*) malloc(lineSize * sizeof(char));
    //Column size
    FILE* fichier = fopen(fileName, "r");
    if (fichier != NULL)
        if(fgets( ligne, lineSize, fichier) != NULL){
            chaine=strtok(ligne, ",");
            while(chaine != NULL){
                column++;
                chaine=strtok(NULL, ","); 
            }
            size.columnIris = column -1;
        }
    //Line Size
    if (fichier != NULL){
        while ( fgets( ligne, lineSize, fichier) != NULL ) line++;
        size.lineIris = line+1;
    }
    fclose( fichier ) ;

}

//Function to reserve space for DataIris
DataIris* reserve_space_data_iris (DataIris* data){
    data = malloc (size.lineIris * sizeof(DataIris));
    for(int i=0; i< size.lineIris; i++){
        data[i].dataIris = (double*) malloc (size.columnIris * sizeof(double));
        data[i].normalized = (double*) malloc (size.columnIris * sizeof(double));
    }
    return data;
}
//Function to charge all datas from the database
DataIris * charge_database(char* fileName, DataIris *data){
    int     lineSize = 100;
    char*   ligne = (char*)malloc(lineSize*sizeof(char));
    char*   chaine;   
    int     compterLine=0, compterColonne;
    FILE* fichier = fopen(fileName, "r");
    if (fichier != NULL){
        while ( fgets( ligne, lineSize, fichier) != NULL ){
            compterColonne = 1;
            chaine=strtok(ligne, ",");
            data[compterLine].dataIris[0] = atof(chaine);
            while(compterColonne < size.columnIris){
                chaine=strtok(NULL, ",");
                data[compterLine].dataIris[compterColonne] = atof(chaine);
                compterColonne++;
            }
            chaine=strtok(NULL, "\n");
            data[compterLine].nameIris  = strdup(chaine);
            if(strcmp(strdup(chaine), "Iris-setosa") == 0) data[compterLine].label = 1;
            if(strcmp(strdup(chaine), "Iris-versicolor") == 0) data[compterLine].label = 2;
            if(strcmp(strdup(chaine), "Iris-virginica") == 0) data[compterLine].label = 3;
           compterLine++;  
    } 
    fclose( fichier ) ;
    }
    return data;
} 
//Function to normalize the datas
void normalize_matrix(DataIris *data) {
	double norm = 0;
	for (int i = 0; i < size.lineIris; i++) {
		norm = 0;
        for(int j= 0; j < size.columnIris; j++)
                norm += pow(data[i].dataIris[j],2);
        norm = sqrt(norm);
		for (int j = 0; j < size.columnIris; j++) {
			data[i].normalized[j] = data[i].dataIris[j] / norm; 
		}
	}
}
#endif