package codeeval;

import java.util.List;
import java.util.ArrayList;
import codeeval.PalindromeFinder;

class Palindrome implements PalindromeFinder {
  public boolean isPalindrome(int num) {
    List<Integer> nums = new ArrayList<>();

    for (; num >= 1; num = num / 10) {
      nums.add(num % 10);
    }

    for (int start = 0, end = nums.size() - 1; start <= end; ++start, --end) {
      if (nums.get(start) != nums.get(end)) {
        return false;
      }
    }

    return true;
  }
}
