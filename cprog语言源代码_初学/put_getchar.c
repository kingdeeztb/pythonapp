/*
**************************
*键盘记录器，可以记录键盘输入*
*create:tianbo
*date:20201117
*note:keyboard sign tools
**************************
*/
#include <stdio.h>
int main(int argc, char const *argv[])
{
    int c;
    c = getchar();
    while (c != EOF)
    {
        putchar(c);
        c = getchar();
    }
    return 0;
}
