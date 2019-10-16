package problem4;

import static org.junit.Assert.assertEquals;
import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class SmallestMissingTest {
 	SmallestMissing tester = new SmallestMissing();

    @Test
    public void shouldReturnSmallestPositiveMissingInt() {
        int[] t1 = {1,2,3,4,6,7,8};
        int[] t2 = {1,-2,3,-4,-6,-7,8};
        int[] t3 = {1,2,3,4,5,6,7};
        assertEquals("Should return 5 for [1,2,3,4,6,7,8]", 5, tester.smallestMissing(t1));
        assertEquals( "Should return 2 for [1,-2,3,-4,-6,-7,8]", 2, tester.smallestMissing(t2));
        assertEquals("Should return 8 for [1,2,3,4,5,6,7]", 8, tester.smallestMissing(t3));
    }

    @Test
    public void shouldReturn1WhenEmptyArray() {
        int[] t1 = {};
        assertEquals( "Should return 1 for empty array", 1, tester.smallestMissing(t1));
    }

    @Test
    public void shouldReturn1WhenAllNonpositive() {
        int[] t1 = {-1,-2,-3,-4,-6,-7,-8};
        assertEquals( "Should return 1 for [-1,-2,-3,-4,-6,-7,-8]", 1, tester.smallestMissing(t1));
    }

}
