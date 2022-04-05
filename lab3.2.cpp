#include <iostream>
#include <cmath>
using namespace std;
double f(double x)
{ return sin(x)- pow(2-x,1.5);}
double prog(double x0,double eps,int n)
{
	double x1=x0+eps;
    double x2;
    double fx0=f(x0), fx1=f(x1), fx3;
    int k;
    for(k=0; k<n; k++)
   {   x2=x0-fx0*(x1-x0)/(fx1-fx0);
    double fx2=f(x2);
      if(fabs(fx2)<eps)
     	 break;
    x0=x1; 
	fx0=fx1;
    x1=x2; 
	fx1=fx2;
}
   return x2;
}
int main() {
	double x1,eps;
	cout << "write borders and error" << endl;
	cin >> x1  >> eps;
	cout << prog(x1,eps,10000);
	
}