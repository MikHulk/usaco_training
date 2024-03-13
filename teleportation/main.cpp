#include <iostream>

using namespace std;


int main () {
  int x, y, a, b;
  cin >> a >> b >> x >> y;
  int dab = abs(a - b);
  int nta = min(abs(a - x), abs(a - y));
  int ntb = min(abs(b - x), abs(b - y));
  cout << min(dab, nta + ntb);
}
