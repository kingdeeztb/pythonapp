/*
**************************
*华氏度，摄氏度对比*
*create:tianbo
*date:20201117
*note:温度对比
**************************
*/
#include <stdio.h>
int main(int argc, char const *argv[])
{
    float falr, cledr;        /*法华，摄氏度*/
    int lower, upper, step; /*最低，最高，步长*/

    lower = 0;
    upper = 300;
    step = 20;

    falr = lower;
    while (falr <= upper)
    {
        cledr = 5.0 * (falr - 32) / 9.0;
        printf("%3.2f %6.2f\n", falr, cledr);
        falr = falr + step;
    }
}
