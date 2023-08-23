import java.util.ArrayList;
import java.util.List;

public class task02 {
    public static List<List<Integer>> splitArray(int[] nums, int X) {
        List<List<Integer>> subArrays = new ArrayList<>();
        List<Integer> currentSubArray = new ArrayList<>();
        int subSum = 0;

        for (int num : nums) {
            if (subSum + num <= X) {
                currentSubArray.add(num);
                subSum += num;

            } else {

                subArrays.add(currentSubArray);
                currentSubArray = new ArrayList<>();
                currentSubArray.add(num);
                subSum = num;

            }
        }
        subArrays.add(currentSubArray);

        return subArrays;
    }

    public static void main(String[] args) {
        int[] nums = { 2, 3, 4, 5, 6, 3, 2, 7 };
        int X = 4;
        List<List<Integer>> subArrays = splitArray(nums, X);

        System.out.println("Подмассивы с суммой меннее или равной " + X + "-");

        for (List<Integer> subArray : subArrays) {
            System.out.println(subArray);
        }
    }

}
