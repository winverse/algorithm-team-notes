#include <iostream>
// 거스름돈 구하기

using namespace std;

int main () {
  int n = 1260;
  int count = 0;

  int coinTypes[4] = {500, 100, 50, 10};

  for(int i = 0; i < 4; i++) {
    count += n / coinTypes[i];
    n %= coinTypes[i];
  }

  cout << count << '\n'; 
}


