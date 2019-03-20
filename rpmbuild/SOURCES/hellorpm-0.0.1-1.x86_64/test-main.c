/*************************************************************************
    > File Name: test-main.c
    > Author: chaofei
    > Mail: chaofeibest@163.com 
    > Created Time: 2019-03-17 04:23:11
 ************************************************************************/

#include <stdio.h>
#include "swap.h"
#include "max.h"

int main(void) {
  int x = 2;
  int y = 8;
  printf("max(%d, %d) = %d\n", x, y, max(x, y));
  swap(&x, &y);
  printf("Hello, I'm chaofei\n");
  printf("This is a test of rpm build\n");
  return 0;
}
