package deltaX.arrays;

public class MaxSubarr {
    public int maxSubArray(int[] nums) {
    int currentSum = nums[0], maxSum = nums[0];
    for (int i = 1; i < nums.length; i++) {
        currentSum = Math.max(nums[i], currentSum + nums[i]);
        maxSum = Math.max(maxSum, currentSum);
    }
    return maxSum;
}
}
