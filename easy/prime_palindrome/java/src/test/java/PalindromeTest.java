package codeeval;

import org.junit.Before;
import org.junit.After;
import org.junit.Test;
import static org.junit.Assert.*;

import codeeval.Palindrome;

public class PalindromeTest {
  @Test
  public void testPalindrome() {
      Palindrome p = new Palindrome();

      assertTrue(p.isPalindrome(9));
      assertTrue(p.isPalindrome(99));
      assertTrue(p.isPalindrome(909));
      assertTrue(p.isPalindrome(90909));
      assertTrue(p.isPalindrome(10901));
      assertTrue(p.isPalindrome(00000));

      assertFalse(p.isPalindrome(12345));
      assertFalse(p.isPalindrome(12));
  }
}
