#include <iostream>
#include <cmath>
using namespace std;
float f(float x) {
	return x*x*x-2.92*x*x+1.4355*x+0.791136;
}
float prog(float x1,float x2, float eps) {
	float a = (x1+x2)/2;
	while (abs(f(a)) > eps) {
		if (f(x1)*f(a) < 0) 
			x2 = a;
		else 
			x1 = a;
		a = (x1+x2)/2;
	}
	return a;
}
	int main() {
		float q,w,e;
		cout << "write borders and error " << endl;
		cin >> q >> w >> e;
		cout << prog(q,w,e);
		return 0;
	}