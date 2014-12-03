import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import org.junit.Before;
import org.junit.After;
import org.junit.Test;
import static org.junit.Assert.*;

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
  public void testIsPrime() {
    PrimePalindrome pp = new PrimePalindrome();
    assertTrue(pp.isPrime(3));
    assertTrue(pp.isPrime(503));
    assertTrue(pp.isPrime(2887));
  }
}
