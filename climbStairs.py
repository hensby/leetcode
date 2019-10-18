class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        step = [1,2]
        for i in range (2,n):
            step.append(step[i-1]+step[i-2])
        return step[n-1]
    #Fibonacci sequence
so = Solution()
print(so.climbStairs(4))