class Computation:
    def __init__(self):
        pass

    def factorial(self,n):
        if n == 0:
            return 1
        else:
            n * self.factorial(n-1)

    def naturalSum(self,n):
        return n*(n+1)//2
    
    def testprime(self,n):
        if n<=1:
            return False

        for i in range(2, int(n**0.5) + 1):
            if n% i == 0:
                return False
        
        return True

    def testPrims(self,a,b):
        return self.testprime(a) and self.testprime(b)
    
       