#include <iostream>
#include <fstream>

int main(int argc, char* argv[]) {
  std::ifstream file;
  file.open(argv[1]);

  int div1, div2, numIterations;

  while(file >> div1 >> div2 >> numIterations) {
    for(int i = 1; i <= numIterations; ++i) {
      if(i % div1 == 0) std::cout << "F";
      if(i % div2 == 0) std::cout << "B";
      if(i % div1 != 0 && i % div2 != 0) std::cout << i;
      std::cout << " ";
    }
    std::cout << std::endl;
  }

  return 0;
}
