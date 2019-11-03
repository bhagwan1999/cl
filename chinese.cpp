#include<bits/stdc++.h> 
#include<iostream>
using namespace std; 

// Returns modulo inverse of a with respect to m using extended  
int inv(int a, int m) 
{ 
	/*int m0 = m, t, q; 
	int x0 = 0, x1 = 1; 

	if (m == 1) 
	return 0; 

	// Apply extended Euclid Algorithm 
	while (a > 1) 
	{ 
		// q is quotient 
		q = a / m; 

		t = m; 

		// m is remainder now, process same as 
		// euclid's algo 
		m = a % m, a = t; 

		t = x0; 

		x0 = x1 - q * x0; 

		x1 = t; 
	} 

	// Make x1 positive 
	if (x1 < 0) 
	x1 += m0; 

	return x1; */
        int q=a%m;
        int l=0;
        int i=1;
        while(l!=1)
        {
         l=(q*i)%m;
	  i=i+1;
        }
        return i-1;

} 
 
// (gcd for every pair is 1) 
int findMinX(int num[], int rem[], int k) 
{ 
	// Compute product of all numbers 
	int prod = 1; 
	for (int i = 0; i < k; i++) 
		prod *= num[i]; 

	// Initialize result 
	int result = 0; 

	// Apply above formula 
	for (int i = 0; i < k; i++) 
	{ 
		int pp = prod / num[i]; 
		result += rem[i] * inv(pp, num[i]) * pp; 
	} 

	return result % prod; 
} 


// Driver method 
int main(void) 
{ 
	int num[] = {3,4,5}; 
	int rem[] = {2,3,4}; 
        int r;

	int k = sizeof(num)/sizeof(num[0]);
	cout << "x is " << findMinX(num, rem, k); 
	return 0; 
} 
