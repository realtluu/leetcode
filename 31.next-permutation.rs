impl Solution {
    pub fn next_permutation(nums: &mut Vec<i32>) {
        let len = nums.len();
        if len < 2 { return }
        
        for i in (0..(len - 1)).rev() {
            if Self::try_swap(&mut nums[i..]) { return }
        }
        
        nums.sort();
    }
    
    fn try_swap(nums: &mut [i32]) -> bool {
        let len = nums.len();
        
        for i in (1..len).rev() {
            if nums[0] < nums[i] {
                nums[0] = nums[0] ^ nums[i];
                nums[i] = nums[0] ^ nums[i];
                nums[0] = nums[0] ^ nums[i];
                let mut rest = &mut nums[1..];
                rest.sort();
                return true;
            }
        }
        
        false
    }
}