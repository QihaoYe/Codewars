#include <stdio.h>


#define swap(a,b) a=a^b;b=a^b;a=a^b
#define string(a) #a
#define join(a,b) a##b


// ---[test zone]---
int main(int argc, char const *argv[])
{
	int a = 2;
	int b = 4;
	int join(a, b) = 8;
	swap(a, b);
	printf("%d %d\n", a, b);
	printf("%s\n", string(swap(a, b)));
	printf("%d\n", join(a, b));
	return 0;
}
