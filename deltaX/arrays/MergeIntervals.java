package deltaX.arrays;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class MergeIntervals {
    public int[][] merge(int[][] intervals) {
    Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
    List<int[]> res = new ArrayList<>();
    int[] current = intervals[0];
    res.add(current);
    for (int[] interval : intervals) {
        if (current[1] >= interval[0]) current[1] = Math.max(current[1], interval[1]);
        else res.add(current = interval);
    }
    return res.toArray(new int[0][]);
}
}
