package codeeval;

import java.util.List;
import java.util.ArrayList;

import codeeval.PrimeFinder;

class SieveOfEratosthenes implements PrimeFinder {
  int max = 1000;
  List<Integer> primes = null;

  SieveOfEratosthenes() {
    primes = primesTo(max);
  }

  SieveOfEratosthenes(int max) {
    primes = primesTo(max);
    this.max = max;
  }

  private List<Integer> primesTo(int max) {
    List<Integer> primes = new ArrayList<>();

    for (int i = 0; i <= max; ++i) {
      primes.add(i);
    }

    int p = 2;
    while (p <= max) {
      for (int i = p + p; i <= max; i += p) {
        primes.set(i, 0);
      }

      // increment p to the next number not already crossed out/set to 0
      for (++p; p <= max && primes.get(p) == 0; ++p) {}
    }

    return primes;
  }

  public boolean isPrime(int num) {
    if (num > max) {
      primes = primesTo(num);
      max = num;
    }

    if (primes.get(num) != 0) {
      return true;
    } else {
      return false;
    }
  }
}
