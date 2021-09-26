
 
/******************************************************************************  
  
                      ===========================  
        Network:      Adaptive Resonance Theory 1  
                      ===========================  
  
        Application:  Brain Modeling  
                      Stability-Plasticity Demonstration  
  
        Author:       Karsten Kutza  
        Date:         27.6.96  
  
        Reference:    G.A. Carpenter, S. Grossberg  
                      A Massively Parallel Architecture  
                      for a Self-Organizing Neural Pattern Recognition Machine  
                      Computer Vision, Graphics, and Image Processing, 37,  
                      pp. 54-115, 1987  
  
 ******************************************************************************/   
   
   
   
   
/******************************************************************************  
                            D E C L A R A T I O N S  
 ******************************************************************************/   
   
   
#include <stdlib.h>   
#include <stdio.h>   
#include <math.h>   
   
   
typedef int           BOOL;   
typedef char          CHAR;   
typedef int           INT;   
typedef double        REAL;   
   
#define FALSE         0   
#define TRUE          1   
#define NOT           !   
#define AND           &&   
#define OR            ||   
   
#define MIN_REAL      -HUGE_VAL   
#define MAX_REAL      +HUGE_VAL   
   
   
typedef struct {                     /* A LAYER OF A NET:                     */   
        int           Units;         /* - number of units in this layer       */   
        int*         Output;        /* - output of ith unit                  */   
        double**        Weight;        /* - connection weights to ith unit      */   
        int*         Inhibited;     /* - inhibition status of ith F2 unit    */   
} LAYER;   
   
typedef struct {                     /* A NET:                                */   
        LAYER*        F1;            /* - F1 layer                            */   
        LAYER*        F2;            /* - F2 layer                            */   
        int           Winner;        /* - last winner in F2 layer             */   
        double          A1;            /* - A parameter for F1 layer            */   
        double          B1;            /* - B parameter for F1 layer            */   
        double          C1;            /* - C parameter for F1 layer            */   
        double          D1;            /* - D parameter for F1 layer            */   
        double          L;             /* - L parameter for net                 */   
        double          Rho;           /* - vigilance parameter                 */   
} NET;   
   
   
/******************************************************************************  
               A P P L I C A T I O N - S P E C I F I C   C O D E  
 ******************************************************************************/   
   
   
#define N             5   
#define M             10   
   
#define NO_WINNER     M   
   
#define NUM_DATA      30   
   
CHAR                  Pattern[NUM_DATA][N] = { "   O ",   
                                               "  O O",   
                                               "    O",   
                                               "  O O",   
                                               "    O",   
                                               "  O O",   
                                               "    O",   
                                               " OO O",   
                                               " OO  ",   
                                               " OO O",   
                                               " OO  ",   
                                               "OOO  ",   
                                               "OO   ",   
                                               "O    ",   
                                               "OO   ",   
                                               "OOO  ",   
                                               "OOOO ",   
                                               "OOOOO",   
                                               "O    ",   
                                               " O   ",   
                                               "  O  ",   
                                               "   O ",   
                                               "    O",   
                                               "  O O",   
                                               " OO O",   
                                               " OO  ",   
                                               "OOO  ",   
                                               "OO   ",   
                                               "OOOO ",   
                                               "OOOOO"  };   
   
int  Input [NUM_DATA][N];   
int  Output[NUM_DATA][M];   
    
   
   
void InitializeApplication(NET* Net)   
{   
  int n,i,j;   
   
  for (n=0; n<NUM_DATA; n++) {   
    for (i=0; i<N; i++) {   
      Input[n][i] = (Pattern[n][i] == 'O');   
    }   
  }   
  Net->A1  = 1;   
  Net->B1  = 1.5;   
  Net->C1  = 5;   
  Net->D1  = 0.9;   
  Net->L   = 3;   
  Net->Rho = 0.9;   
  for (i=0; i<Net->F1->Units; i++) {   
    for (j=0; j<Net->F2->Units; j++) {   
      Net->F1->Weight[i][j] = (Net->B1 - 1) / Net->D1 + 0.2;   
      Net->F2->Weight[j][i] = Net->L / (Net->L - 1 + N) - 0.1;   
    }   
  }   
}   
   
   
void WriteInput(NET* Net, BOOL* Input)   
{   
  int i;   
      
  for (i=0; i<N; i++) {   
    printf("%s", (Input[i]) ? "1," : "0,");   
  }   
  printf("\n");   
}   
   
   
void WriteOutput(NET* Net, int* Output)   
{   
  if (Net->Winner != NO_WINNER)   
    printf("Class %i\n", Net->Winner);   
  else   
    printf("new Input and all Classes exhausted\n");   
}   
   
   

   
   
/******************************************************************************  
                          I N I T I A L I Z A T I O N  
 ******************************************************************************/   
   
   
void reserveSpace(NET* Net)   
{   
  int i;   
   
  Net->F1 = (LAYER*) malloc(sizeof(LAYER));   
  Net->F2 = (LAYER*) malloc(sizeof(LAYER));   
         
  Net->F1->Units     = N;   
  Net->F1->Output    = (BOOL*)  calloc(N, sizeof(BOOL));   
  Net->F1->Weight    = (REAL**) calloc(N, sizeof(REAL*));   
   
  Net->F2->Units     = M;   
  Net->F2->Output    = (BOOL*)  calloc(M, sizeof(BOOL));   
  Net->F2->Weight    = (REAL**) calloc(M, sizeof(REAL*));   
  Net->F2->Inhibited = (BOOL*)  calloc(M, sizeof(BOOL));   
   
  for (i=0; i<N; i++) {   
    Net->F1->Weight[i] = (REAL*) calloc(M, sizeof(REAL));   
  }   
  for (i=0; i<M; i++) {   
    Net->F2->Weight[i] = (REAL*) calloc(N, sizeof(REAL));   
  }   
}   
   
   
void SetInput(NET* Net, int* Input)   
{   
  INT  i;   
  REAL Activation;   
      printf("Activation: ");
  for (i=0; i<Net->F1->Units; i++) {   
    Activation = Input[i] / (1 + Net->A1 * (Input[i] + Net->B1) + Net->C1);   
    Net->F1->Output[i] = (Activation > 0);   
    printf("%d ", Net->F1->Output[i]);
  }   
 printf("\n");
}   
   
   
void GetOutput(NET* Net, BOOL* Output)   
{   
  INT i;   
      
  for (i=0; i<Net->F2->Units; i++) {   
    Output[i] = Net->F2->Output[i];   
  }   
}   
   
   
/******************************************************************************  
                     P R O P A G A T I N G   S I G N A L S  
 ******************************************************************************/   
   
   
void PropagateToF2(NET* Net)   
{   
  INT  i,j;   
  REAL Sum, MaxOut;   
      
  MaxOut = MIN_REAL;   
  Net->Winner = NO_WINNER;   
  for (i=0; i<Net->F2->Units; i++) {   
    if (NOT Net->F2->Inhibited[i]) {   
      Sum = 0;   
      for (j=0; j<Net->F1->Units; j++) {   
        Sum += Net->F2->Weight[i][j] * Net->F1->Output[j];   
      }   
      if (Sum > MaxOut) {   
        MaxOut = Sum;   
        Net->Winner = i;   
      }   
    }   
    Net->F2->Output[i] = FALSE;   
  }   
  if (Net->Winner != NO_WINNER)   
    Net->F2->Output[Net->Winner] = TRUE;   
}   
   
   
void PropagateToF1(NET* Net, BOOL* Input)   
{   
  INT  i;   
  REAL Sum, Activation;   
      
  for (i=0; i<Net->F1->Units; i++) {   
    Sum = Net->F1->Weight[i][Net->Winner] * Net->F2->Output[Net->Winner];   
    Activation = (Input[i] + Net->D1 * Sum - Net->B1) /   
                 (1 + Net->A1 * (Input[i] + Net->D1 * Sum) + Net->C1);   
    Net->F1->Output[i] = (Activation > 0);   
  }   
}   
   
   
/******************************************************************************  
                        A D J U S T I N G   W E I G H T S  
 ******************************************************************************/   
   
   
REAL Norme(NET* Net, BOOL* Input)   
{   
  INT  i;   
  REAL Magnitude;   
   
  Magnitude = 0;   
  for (i=0; i<Net->F1->Units; i++) {   
    Magnitude += Input[i];   
  }   
  return Magnitude;   
}   
   
   
void AdjustWeights(NET* Net)   
{   
  INT  i;   
  REAL MagnitudeInput_;   
   
  for (i=0; i<Net->F1->Units; i++) {   
    if (Net->F1->Output[i]) {   
      MagnitudeInput_ = Norme(Net, Net->F1->Output);   
      Net->F1->Weight[i][Net->Winner] = 1;   
      Net->F2->Weight[Net->Winner][i] = Net->L / (Net->L - 1 + MagnitudeInput_);   
    }   
    else {   
      Net->F1->Weight[i][Net->Winner] = 0;   
      Net->F2->Weight[Net->Winner][i] = 0;   
    }   
  }   
}   
   
   
/******************************************************************************  
                      S I M U L A T I N G   T H E   N E T  
 ******************************************************************************/   
   
   
void SimulateNet(NET* Net, BOOL* Input, BOOL* Output)   
{   
  int  i;   
  int Resonance, Exhausted;   
  double MagnitudeInput, MagnitudeInput_;   
   
  WriteInput(Net, Input); 

  for (i=0; i<Net->F2->Units; i++) {   
    Net->F2->Inhibited[i] = FALSE;   
  }   
  Resonance = FALSE;   
  Exhausted = FALSE;   
  do {   
    SetInput(Net, Input);   
    PropagateToF2(Net);   
    GetOutput(Net, Output);   
    if (Net->Winner != NO_WINNER) {   
      PropagateToF1(Net, Input);   
      MagnitudeInput = Norme(Net, Input); 
      MagnitudeInput_ = Norme(Net, Net->F1->Output);   
      if ((MagnitudeInput_ / MagnitudeInput) < Net->Rho)   
        Net->F2->Inhibited[Net->Winner] = TRUE;   
      else      
        Resonance = TRUE;   
    }   
    else Exhausted = TRUE;   
  } while (NOT (Resonance OR Exhausted));   
  if (Resonance)   
    AdjustWeights(Net);   
  WriteOutput(Net, Output);   
     
}   
   
   
/******************************************************************************  
                                    M A I N  
 ******************************************************************************/   
   
   
void main()   
{   
  NET Net;   
  INT n;   
   
  reserveSpace(&Net);   
  InitializeApplication(&Net);   
   
  for (n=0; n<NUM_DATA; n++) {   
    SimulateNet(&Net, Input[n], Output[n]);   

     
  }   
     
}   

 