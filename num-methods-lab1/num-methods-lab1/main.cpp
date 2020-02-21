using namespace std;

#define _USE_MATH_DEFINES

#include <iostream>
#include <cmath>
#include <math.h>

double x = 0.5, a = 0.2, s1 = 0, s2 = 0;

int main()
{
	s1 = -(M_PI / (2 * a)) * (cos((M_PI - x)*a) / (sin(M_PI*a))) + 1 / (2 * a * a);
	a = a * a;
	double k = 1;

	while (fabs(s1 - s2) >= pow(10, -10))
	{
		if (a != k * k)
		{
			s2 += cos(k*x) / (k*k - a);
			k++;
		}
	}

	printf("%s%.0f\n", "k = ", k);
	printf("%.16f\n ", s2);
	
	system("pause");
	return 0;
}

