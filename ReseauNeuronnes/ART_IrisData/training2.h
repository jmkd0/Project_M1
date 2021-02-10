#ifndef __IRIS__H_
#define __ISIS__H_

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include <float.h>

/* Reserve memory space for weights */
Weights* reserve_space_weights(Weights* weights){
    weights = (Weights*) malloc(sizeof(Weights));
    weights->bottom_up = (double**) malloc(param.number_feature * sizeof(double*));
    weights->top_down = (double**) malloc(param.number_cluster * sizeof(double*));

    for (int i = 0; i < param.number_feature; i++)
        weights->bottom_up[i] = (double*) malloc(param.number_cluster * sizeof(double));

    for (int i = 0; i < param.number_cluster; i++)
        weights->top_down[i] = (double*) malloc(param.number_feature * sizeof(double));

    return weights;
}

/* Reserve space for activations */
Activation* reserve_space_activation(Activation* activation){
    activation = (Activation*) malloc(sizeof(Activation));
    activation->X = (double*) malloc(param.number_feature * sizeof(double));
    activation->Y = (double*) malloc(param.number_cluster * sizeof(double));
    activation->inhibited = (int*) calloc(param.number_cluster, sizeof(int));

    return activation;
}

/* Norm of vector */
double norm(double* vector){
    double norm = 0;
    for(int j= 0; j < size.columnIris; j++)
        norm += pow(vector[j],2);
    return norm;
}

/* Initialize values of weights Bottom-Top and Top-Down */
void init_weight(Weights* weights){
    for(int i = 0; i < param.number_feature; i++){
        for(int j = 0; j < param.number_cluster; j++){
            weights->bottom_up[i][j] = 1.0/(param.learning_rate - 1 + param.number_feature);
        }
    }
    for(int i = 0; i < param.number_cluster; i++){
        for(int j = 0; j < param.number_feature; j++){
            weights->top_down[i][j] = 1;
        }
    }
}

/* Initialize values of activations Bottom (X) and Top (Y) */
void init_activation(double* feature, Activation* activation){
    for(int i = 0; i < param.number_feature; i++)
        activation->X[i] = feature[i];
    for(int i = 0; i < param.number_cluster; i++)
        activation->Y[i] = 0;
}

/* Compute values of weights Bottom-Top*/
void update_bottom_up_activation(Weights* weights, Activation* activation){
    for(int j = 0; j < param.number_cluster; j++){
        if(!(activation->Y[j] == -1)){
            double y = 0;
            for(int i = 0; i < param.number_feature; i++){
                y += weights->bottom_up[i][j] * activation->X[i];
            }
           activation->Y[j] = y; 
        }
    }
}

/* Compute values of weights Top-Down */
void update_top_down_activation(double* feature, Weights* weights, Activation* activation, int winner){
    for(int i = 0; i < param.number_feature; i ++)
        activation->X[i] = feature[i] * weights->top_down[winner][i];
}

/* Find winner in vector (the max value) 
    return the index of the max         */
int find_winner(double* vector){
    int winner = 0;
    double max = vector[0];
    for(int i = 0; i < param.number_cluster; i++){
        if(vector[i] > max){
            max = vector[i];
            winner = i;
        }
    }
    return winner;
}

/* Update the weight Bottom-Top and Top-Down after one epoch */
void update_weights(Weights* weights, Activation* activation, int winner, double norme_x){
    for(int i = 0; i < param.number_feature; i++)
            weights->bottom_up[i][winner] = (param.learning_rate * activation->X[i])/(param.learning_rate - 1 + norme_x);

    for(int j = 0; j < param.number_feature; j++)
            weights->top_down[winner][j] = activation->X[j];
}


/* Learning  */
void learning(DataIris* data, Weights* weights, Activation* activation){
    init_weight(weights);                                    //Init Bottom-Top and Top-Down weight
    for (int epoch = 0; epoch < param.epoch; epoch++){       //Perform epoch itteration
        for(int i = 0; i < size.lineIris; i++){              //For each flower
            init_activation(data[i].normalized, activation); //Init activaton
            display_input_layer(data[i].normalized);
            double norm_feature = norm(data[i].normalized);  //Get the norm of the feature
            update_bottom_up_activation(weights, activation);//Update activation for Top (Y) layer
            display_activation_y(activation);
            int resonance = FALSE;
            int winner;
            double norm_activation_x;
            
            while(!resonance){                                   //Test for reset 
                winner = find_winner(activation->Y);        //Get the winner index in Y activation
                if(activation->inhibited[winner] == 1){            //If all activation is -1 this feature cannot be clustered
                    //data[i].predict_label = 0;
                    break;
                }
                update_top_down_activation(data[i].normalized, weights, activation, winner); //Update activation for Bottom (X) layer
                display_activation_x(activation);
                printf("\nWinner: %d", winner);
                norm_activation_x = norm(activation->X);            //Get norm of the new activation X

                double vigilance = norm_activation_x / norm_feature;//Calculate the rate of similarity
                printf("\n>>>>>%f", vigilance);
                if(vigilance >= param.vigilance){                   //If the similarity rate is above 0.4
                    resonance = TRUE;                                      //Reset becomes false
                    data[i].predict_label = winner + 1;             //And the label of this feature is the index of Y winner in the top
                }else{
                    activation->inhibited[winner] = TRUE;                     //This class will not participate the compétition the next reset
                    display_activation_y(activation);
                }
            }
            display_weights(weights);
                //Update weights
                update_weights(weights, activation, winner, norm_activation_x); //Update the weight of Bottom-Top and Top-Down weight
            
            
           
        }
    }
}
#endif