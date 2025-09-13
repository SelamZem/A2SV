class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        primes = set()

        def factors(n):
            d = 2
            while d * d <= n:
                while n % d == 0:
                    primes.add(d)
                    n //= d
                d += 1
            if n > 1:
                primes.add(n)

        for num in nums:
            factors(num)

        return len(primes)
