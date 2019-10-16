package problem4;
import java.util.*;

public class SmallestMissing {
	
	public int smallestMissing(int[] numbers){
		//stores the int to be returned
		//set to 1 in case array is empty or only contains negative numbers
		int ret = 1;
		
		if(numbers == null || numbers.length == 0) {
			return ret;
		}

		Arrays.sort(numbers);

		//keeps track of positive numbers found
		int[] tracker = new int[numbers[numbers.length -1] + 1];

		//if a positive number is found, update tracker of that index to 1
		for(int i = 0; i < numbers.length; i++){
			if(numbers[i] > 0){
				tracker[numbers[i]] = 1;
			}
		}

		//find first instance of missing number
		for(int j = 1; j < tracker.length; j++){
			if(tracker[j] == 0){
				ret = j;
				break;
			}
			//if no positive numbers are missing, return the next largest
			if(j == tracker.length -1) {
				ret = tracker.length;
			}
		}

		return ret;

	}

}