/*************************************************************************
    > File Name: swap.c
    > Author: chaofei
    > Mail: chaofeibest@163.com 
    > Created Time: 2019-03-17 04:20:18
 ************************************************************************/

#include <stdio.h>

void swap(int *x, int *y) {
  printf("change begin a=%d b=%d\n", *x, *y);
  int z;
  z = *x;
  *x = *y;
  *y = z;
  printf("change end a=%d b=%d\n", *x, *y);
}
