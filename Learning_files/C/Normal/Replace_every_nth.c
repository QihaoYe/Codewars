#include <stdio.h>
#include <time.h>
#include <string.h>
#include <stdlib.h>


char* replaceNth(const char* text, int n, char oldValue, char newValue)
{
	int counter = 0, len = strlen(text);
	char* result = (char *)malloc((len + 1) * sizeof(char));
	for (int i=0;i<len;i++)
	{
		*(result + i) = *(text + i);
		if (*(text + i) == oldValue)
		{
			counter++;
			if (n > 0 && counter % n == 0)
				*(result + i) = newValue;
		}
	}
	*(result + len) = '\0';
	return result;
}


int main(int argc, char const *argv[])
{
	clock_t start;
	clock_t finish;
	double duration;



	start = clock();

	char* a = replaceNth("Vader said: No, I am your father!", 2, 'a', 'o');
	printf("%s\n", a);


	finish = clock();
	duration = (double)(finish - start) / CLOCKS_PER_SEC;



	printf( "%f seconds\n", duration);
	return 0;
}
