#include <stdio.h>
#include <time.h>

int main(int argc, char const *argv[])
{
	clock_t start;
	clock_t finish;
	double duration;



	start = clock();



	finish = clock();
	duration = (double)(finish - start) / CLOCKS_PER_SEC;



	printf( "%f seconds\n", duration);
	return 0;
}
