#include<bits/stdc++.h> 
#include<iostream>

using namespace std;
int gcd(int a, int b) {
   int t;
   while(1) {
      t= a%b;
      if(t==0)
      return b;
      a = b;
      b= t;
   }
}
int modInverse(int a, int m)
{
    /*a = a%m;
    for (int x=1; x<m; x++)
       if ((a*x) % m == 1)
          return x;*/
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
int main() {
   double p,q;
cout<<"Enter the value p (prime number):";
cin>>p;
cout<<"\nEnter the value of q (prime number):";
cin>>q;
   double n=p*q;
   double track;
   double phi= (p-1)*(q-1);
   double e;

cout<<"\nEnter the value of e:";
cin>>e;
   while(e<phi) {
      track = gcd(e,phi);
      if(track==1)
         break;
      else
         e++;
   }
   double d=modInverse(e,phi);
   double message;
   cout<<"\nEnter the message: ";
   cin>>message;
   double c = pow(message,e);
   
   c=fmod(c,n);

   double m = pow(c,d);
   m=fmod(m,n);
 
   cout<<"\nOriginal Message = "<<message;
   cout<<"\n"<<"p = "<<p;
   cout<<"\n"<<"q = "<<q;
   cout<<"\n"<<"n = pq = "<<n;
   cout<<"\n"<<"phi = "<<phi;
   cout<<"\n"<<"e = "<<e;
   cout<<"\n"<<"d = "<<d;
   cout<<"\n"<<"Encrypted message = "<<c;
    cout<<"\nDecrypted message = "<<m<<"\n";
   return 0;
}
