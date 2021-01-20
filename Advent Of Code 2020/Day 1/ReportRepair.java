import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;

class ReportRepair {
    
    public static int twoSumBruteForce(int[] nums, int target) {
        int[] arr = {0, 0};
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    arr[0] = nums[i];
                    arr[1] = nums[j];
                }
            }
        }
        int out = arr[0]*arr[1];
        return out;
    }

	public static int threeSumBruteForce(int[] nums, int target) {
        int[] arr = {0, 0, 0};
        for (int i = 0; i < nums.length; i++) {
			for (int j = i + 1; j < nums.length; j++) {
				for (int k = j + 1; k < nums.length; k++) {
					if (nums[i] + nums[j] + nums[k] == target) {
						arr[0] = nums[i];
						arr[1] = nums[j];
						arr[2] = nums[k];
					}
				}
            }
        }
        int out = arr[0]*arr[1]*arr[2];
        return out;
    }
	
    public static int twoSumHash(int[] nums, int target) {
		//Create and populate Hash Map
		Map<Integer, Integer> map = new HashMap<>();
		for (int i = 0; i < nums.length; i++) {
			map.put(nums[i], i);
		}
		//search for the compliment of each element. ensure the complement and i is unique
		for (int i = 0; i < nums.length; i++) {
			int complement = target - nums[i];
			if (map.containsKey(complement) && map.get(complement) != i) {
				int[] arr = {nums[i], nums[map.get(complement)]};
				return arr[0] * arr[1];
			}
		}
		throw new IllegalArgumentException("No two sum solution");
	}

	// convert elements of array list
	public static int[] convertIntegers(ArrayList<Integer> integers)
	{
		int[] ret = new int[integers.size()];
		for (int i=0; i < ret.length; i++)
		{
			ret[i] = integers.get(i).intValue();
		}
		return ret;
	}

	public static void main(String[] args) {
		ArrayList<Integer> input = new ArrayList<Integer>();
		try{
			List<String> inputString = Files.readAllLines(Paths.get("Input 1.txt"));
			for (String i : inputString) {
				input.add(Integer.parseInt(i));
			}
		}
		catch(IOException e){
			// Could not find file
		}
		int[] in = convertIntegers(input);
		//int out = twoSumBruteForce(in, 2020);
		int out = twoSumHash(in, 2020);
		//int out = threeSumBruteForce(in, 2020);
		System.out.println(out);
	}

}