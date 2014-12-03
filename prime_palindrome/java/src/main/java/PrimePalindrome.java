package codeeval;

import java.util.List;

import codeeval.PrimeFinder;
import codeeval.SieveOfEratosthenes;

class PrimePalindrome {
  PrimeFinder primes = null;

  PrimePalindrome() {
    primes = new SieveOfEratosthenes();
  }

  public boolean isPrime(int num) {
    return primes.isPrime(num);
  }

  public static void main(String[] args) {
    System.out.println("hi");
  }

  public void hi() {
    System.out.println("hi");
  }
}
