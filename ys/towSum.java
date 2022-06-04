public class towSum {
    /**
     * 双层循环，只要等于target就行
     *
     * @param nums
     * @param target
     * @return
     */
    public int[] twoSumWay1(int[] nums, int target) {
        int[] result = new int[2];
        for (int startIndex = 0; startIndex < nums.length; startIndex++) {
            for (int endIndex = startIndex + 1; endIndex < nums.length; endIndex++) {
                if (nums[startIndex] + nums[endIndex] == target) {
                    result[0] = startIndex;
                    result[1] = endIndex;
                    return result;
                }
            }
        }
        return null;
    }

    /**
     * 第一次for循环存储到Map中，map结构  <value,index>
     * 第二次for循环遍历，只要target-value在map中能找到，即可返回
     *
     * @param nums
     * @param target
     * @return
     */
    public int[] twoSumWay2(int[] nums, int target) {
        int[] result = new int[2];
        HashMap<Integer, Integer> map = new HashMap(4);
        for (int index = 0; index < nums.length; index++) {
            map.put(nums[index], index);
        }
        for (Integer index = 0; index < nums.length; index++) {
            Integer targetIndex = map.get(target - nums[index]);
            if (targetIndex != null && targetIndex != index) {
                result[0] = index;
                result[1] = targetIndex;
                return result;
            }
        }
        return null;
    }

    public int[] twoSumWay3(int[] nums, int target) {

    }
}