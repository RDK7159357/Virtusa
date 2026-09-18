package deltaX.DP;

public class LongestIncSubSeq {
    public int lengthOfLIS(int[] nums) {
    int[] tails = new int[nums.length];
    int size = 0;
    for (int x : nums) {
        int l = 0, r = size;
        while (l < r) {
            int m = l + (r - l) / 2;
            if (tails[m] < x) l = m + 1;
            else r = m;
        }
        tails[l] = x;
        if (l == size) size++;
    }
    return size;
}
}
