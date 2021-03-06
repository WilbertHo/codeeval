package codeeval;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import org.junit.Before;
import org.junit.After;
import org.junit.Test;
import static org.junit.Assert.*;

import codeeval.PrimePalindrome;
import codeeval.SieveOfEratosthenes;
import codeeval.Palindrome;

public class PrimePalindromeTest {
  private final PrintStream stdout = System.out;
  private final ByteArrayOutputStream output = new ByteArrayOutputStream();

  @Before
  public void setup() {
    System.setOut(new PrintStream(output));
  }

  @After
  public void cleanup() {
    System.setOut(stdout);
  }

  @Test
  public void testOutput() {
      PrimePalindrome pp = new PrimePalindrome();
      pp.hi();
      assertEquals("hi\n", output.toString());
  }

  @Test
  public void testPrimePalindrome() {
      PrimePalindrome pp = new PrimePalindrome(new SieveOfEratosthenes(),
                                               new Palindrome());
      assertEquals(929, pp.findLargestPrimePalindrome(1000));
  }
}
