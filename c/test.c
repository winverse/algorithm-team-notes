#include <stdio.h>

int sum(int x, int y) {
	return x + y;
};

int main()
{
	int n1, n2, n3, n4;
		
	n1 = 2;
	n2 = n1 * n1;	
	n3 = n2 * n1;
	n4 = n2 * n1;
		
	int result = n1 * sum(2, 3);
	printf("%i \n", result);
	return 0;
}
