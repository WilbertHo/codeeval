package codeeval;

import java.util.List;

import codeeval.PrimeFinder;
import codeeval.PalindromeFinder;
import codeeval.SieveOfEratosthenes;
import codeeval.Palindrome;

class PrimePalindrome {
  PrimeFinder primefinder = null;
  PalindromeFinder palindromefinder = null;

  PrimePalindrome() {}

  PrimePalindrome(PrimeFinder primefinder,
                  PalindromeFinder palindromefinder) {
    this.primefinder = primefinder;
    this.palindromefinder = palindromefinder;
  }

  public boolean isPalindrome(int num) {
    return palindromefinder.isPalindrome(num);
  }

  public boolean isPrime(int num) {
    return primefinder.isPrime(num);
  }

  public boolean isPrimePalindrome(int num) {
    if (isPrime(num) && isPalindrome(num)) {
      return true;
    }
    return false;
  }

  public int findLargestPrimePalindrome(int num) {
    for (; num >= 0; --num) {
      if (isPrimePalindrome(num)) {
        return num;
      }
    }
    return 0;
  }

  public static void main(String[] args) {
    PrimePalindrome pp = new PrimePalindrome(new SieveOfEratosthenes(),
                                             new Palindrome());
    System.out.println(pp.findLargestPrimePalindrome(1000));
  }

  public void hi() {
    System.out.println("hi");
  }
}
