/*
**************************
*字符计数器*
*create:tianbo
*date:20201117
*note:keyboard sign tools
**************************
*/
#include <stdio.h>
int main(int argc, char const *argv[])
{
    long nc;
    nc = 0;
    while (getchar() != EOF)
    {
        ++nc;
        printf("%ld\n", nc);
    }

    return 0;
}
