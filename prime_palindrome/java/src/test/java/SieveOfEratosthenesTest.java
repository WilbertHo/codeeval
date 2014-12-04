package codeeval;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import org.junit.Before;
import org.junit.After;
import org.junit.Test;
import static org.junit.Assert.*;

import codeeval.SieveOfEratosthenes;

public class SieveOfEratosthenesTest {
  @Test
  public void testIsPrime() {
    SieveOfEratosthenes s = new SieveOfEratosthenes();

    assertTrue(s.isPrime(2));
    assertTrue(s.isPrime(73));
    assertTrue(s.isPrime(109));
    assertTrue(s.isPrime(127));
    assertTrue(s.isPrime(877));
    assertTrue(s.isPrime(997));

    assertFalse(s.isPrime(4));
    assertFalse(s.isPrime(1000));
  }
}
