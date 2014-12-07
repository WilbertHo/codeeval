package codeeval;

import codeeval.PalindromeFinder;

class Palindrome implements PalindromeFinder {
  public boolean isPalindrome(String string) {
    for (int start = 0, end = string.length() - 1; start <= end; ++start, --end) {
      if (string.charAt(start) != string.charAt(end)) {
        return false;
      }
    }
    return true;
  }
}
