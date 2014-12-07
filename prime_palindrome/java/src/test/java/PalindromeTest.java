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
      assertTrue(p.isPalindrome("mm"));
      assertTrue(p.isPalindrome("mom"));
      assertTrue(p.isPalindrome("voodoov"));

      assertFalse(p.isPalindrome("mma"));
      assertFalse(p.isPalindrome("voodoo"));
  }
}
