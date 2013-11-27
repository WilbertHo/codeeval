#include <iostream>
#include <fstream>

int main(int argc, char* argv[]) {
  std::ifstream file("input.txt");

  int div1, div2, numIterations;

  while(file >> div1 >> div2 >> numIterations) {
    std::cout << div1 << " " << div2 << " " << numIterations << std::endl;
  }

  return 0;
}
