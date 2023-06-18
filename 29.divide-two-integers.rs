impl Solution {
    pub fn divide(dividend: i32, divisor: i32) -> i32 {
        let mut x = (dividend as i64).abs();
        let y = (divisor as i64).abs();
        
        let mut res: i64 = 0;

        if y == 0 {
            return std::i32::MAX;
        }
        
        while x >= y {
            let mut n = y;
            let mut i = 1;
            
            while (x >= (n << 1)) {
                n <<= 1;
                i <<= 1;
            }
            x -= n;
            res += i;
        }

        if ((dividend < 0) ^ (divisor < 0)) {
            res = -res;
        }
        
        if res > std::i32::MAX as i64 {
            return std::i32::MAX;
        }
        res as i32
    }
}