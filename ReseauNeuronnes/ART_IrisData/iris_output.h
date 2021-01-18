#ifndef __IRIS__H_
#define __ISIS__H_

//Displays
/* Donnée de la database */
void display_database (DataIris *data ){
    int i,j;
    printf("Espace de données:\n");
    for( i=0; i< size.lineIris; i++){
        for( j=0; j< size.columnIris; j++){
            printf("%f  ", data[i].dataIris[j]);
        }
        printf("%s\n", data[i].nameIris);
    }
}

/* Noms des fleurs */
void display_nameflower (DataIris *data ){
    int i;
     printf("\nNoms des fleurs:\n");
    for( i=0; i< size.lineIris; i++){
            printf("%s  --> %d\n", data[i].nameIris, data[i].label);
    }
    printf("\n");
}

/* Données normalisés */
void display_normalise (DataIris *data ){
    int i,j;
    printf("\nDonnées Normalisées:\n");
    for( i=0; i< size.lineIris; i++){
        printf("Iris %d: ",i);
        for( j=0; j< size.columnIris; j++){
            printf("%f  ", data[i].normalized[j]);
        }
        printf("\n");
    }
}
void display_weights(Weights* weights){
    printf("Weights_bottom_top\n");
    for(int i = 0; i < param.number_feature; i++){
        for(int j = 0; j < param.number_cluster; j++){
            printf("%f ",weights->bottom_up[i][j]);
        }
        printf("\n");
    }
    printf("Weights_Top_down\n");
    for(int i = 0; i < param.number_cluster; i++){
        for(int j = 0; j < param.number_feature; j++){
            printf("%f ",weights->top_down[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}
void display_input_layer(double* feature){
    printf("Input: ");
    for(int i = 0; i < param.number_feature; i++)
        printf("%f ",feature[i]);
}
void display_activation_x(Activation* activation){
    printf("Activations_x: ");
    for(int i = 0; i < param.number_feature; i++)
        printf("%f ",activation->X[i]);
    
}
void display_activation_y(Activation* activation){
    printf("\nActivations_y: ");
    for(int i = 0; i < param.number_cluster; i++)
        printf("%f ",activation->Y[i]);
    printf("\n");
}

/* Display result */
void display_result (DataIris *data ){
    int i;
     printf("Noms des fleurs:\n");
    for( i=0; i< size.lineIris; i++){
            printf("%s  --> %d predicted -->  %d\n", data[i].nameIris, data[i].label, data[i].predict_label);
    }
    printf("\n");
}
#endif