#include <stdio.h>


#define swap(a,b) a=a^b;b=a^b;a=a^b


// ---[test zone]---
int main(int argc, char const *argv[])
{
	int a = 2;
	int b = 4;
	swap(a, b);
	printf("%d %d\n", a, b);
	return 0;
}
