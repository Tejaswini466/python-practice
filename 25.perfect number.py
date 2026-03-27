'''Input: num = 28
Output: true
Explanation: 28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, and 14 are all divisors of 28.'''

def checkPerfectNumber(self, num: int) -> bool:
        if num<=1:
            return False
        sum=1
        i=2
        while (i*i)<=num:
            if num%i==0:
                sum+=i
                if i!=num//i:
                    sum+=num//i
            i+=1
        return sum==num