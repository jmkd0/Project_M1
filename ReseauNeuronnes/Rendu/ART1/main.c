#include <stdio.h>
#include <stdlib.h>
#include "iris_input.h"
#include "iris_output.h"
#include "training.h"



int main(){
    char* fileName = "iris.data"; /*https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data*/

        /* Find size line and colum of dataIris */
    set_size_data_iris ( fileName );

        /* set space for DataIris */
    DataIris* data = (DataIris*) malloc (sizeof(DataIris));
    data = reserve_space_data_iris (data);

        /* Charge datas from database */
    data = charge_database (fileName, data);

        /*  Normalize the datas          */
    normalize_matrix (data);

        /* Reserve memory space for weights */
    Weights* weights = (Weights*) malloc(sizeof(Weights));
    weights = reserve_space_weights(weights);

        /* Reserve space for activations */
    Activation* activation = (Activation*) malloc(sizeof(Activation));
    activation = reserve_space_activation(activation);
    
        /* Learning */
    learning(data, weights, activation);

        /*  Displays */
    //display_database (data);
    //display_nameflower (data );
    //display_normalise (data );
    display_result (data);
    return 0;
}