#include "template.inc.cpp"

// compile with -D DE flag using g++ or uncomment the line #define DE in template.inc.cpp
int main()
{
	hr();
	dbgs("UNIT TEST TEMPLATE.INC.CPP");
	hr();


	hr();
	dbgs("ARRAY DEBUGGING TEST");
	dbgs("INPUT\t: {0,1,2,3,4,5}");
	dbgs("OUTPUT\t: testing dbgarr(ARR,N)");
	int arr[] = {0,1,2,3,4,5};
	int n = sizeof(arr)/sizeof(arr[n]);
	dbgarr(arr,n);
	hr();

	return 0;
}
