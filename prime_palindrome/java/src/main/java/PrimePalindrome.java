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
    String string = new Integer(num).toString();
    return palindromefinder.isPalindrome(string);
  }

  public boolean isPrime(int num) {
    return primefinder.isPrime(num);
  }

  public boolean isPrimePalindrome(int num) {
    if (isPrime(num) && isPalindrome())
  }

  public static void main(String[] args) {
    PrimePalindrome pp = new PrimePalindrome(new SieveOfEratosthenes(),
                                             new Palindrome());
    System.out.println("hi");
  }

  public void hi() {
    System.out.println("hi");
  }
}
