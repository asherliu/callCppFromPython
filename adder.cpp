
#include <iostream>

extern "C"{

void adder(int *a, int count)
{
	std::cout<<"Size: "<<count<<"\n";


	int sum = 0;
	for(int i = 0; i < count; i ++)
	{
		sum += a[i];	
	}

	std::cout<<"Summary: "<<sum<<"\n";
	return ;
}
}
