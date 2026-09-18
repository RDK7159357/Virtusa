package deltaX.Strings;

public class LongestSubStrWithOutRepeating {
    public int lengthOfLongestSubstring(String s) {
    int[] map = new int[128];
    int max = 0;
    for (int r = 0, l = 0; r < s.length(); r++) {
        l = Math.max(map[s.charAt(r)], l);
        max = Math.max(max, r - l + 1);
        map[s.charAt(r)] = r + 1;
    }
    return max;
}
}
