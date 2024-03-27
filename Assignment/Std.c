#include<stdio.h>
#include<math.h>

int main(){
    int a[4]={8,16,24,32}; //initialize array with 4 integers
    double sum=0,avg,sum2=0,std;
    for(int i=0;i<4;i++){
        sum=sum+a[i]; //summing int
    }
    avg=sum/4; //taking avg
    for(int i=0;i<4;i++){
        double k=(a[i]-avg);
        double t=pow(k,2);
        sum2=sum2+t; //summing (x-m)**2
    }
    std=sqrt(sum2/4); // taking avg and square rooting it
    printf("%f", (std));
}

