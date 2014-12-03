import java.util.List;
import java.util.ArrayList;

class SieveOfEratosthenes {
  public List<Integer> primesTo(int max) {
    List<Integer> nums = new ArrayList<>();
    List<Integer> primes = new ArrayList<>();

    for(int i = 0; i <= max; ++i) {
      nums.add(i);
    }

    return nums;

    // int p = 2;
    // for(int i = p; i <= max; i * 2) {
    // }

    // return primes;
  }

  public static void main(String[] args) {
    SieveOfEratosthenes s = new SieveOfEratosthenes();

    int max = 1000;
    List<Integer> nums = s.primesTo(max);
    for(int i = 1; i <= max; ++i) {
      System.out.println(nums.get(i));
    }
  }
}
