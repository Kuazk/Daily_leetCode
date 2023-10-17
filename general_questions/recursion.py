import random
class QuickSlect:
    def __init__(self,nums):
        self.nums = nums
        self.first_index =0
        self.last_index = len(nums)-1
    
    def run(self,k):
        return self.select(self.first_index, self.last_index, k-1)
    
    def select(self, first_index, last_index, k):

        pivot_index = self.partition(first_index, last_index)

        # selection phase when we compare the pivot_index with k
        if pivot_index < k:
            return self.select(pivot_index+1,last_index,k)
        elif pivot_index > k:
            return self.select(first_index,pivot_index,k)
        else:
            return self.nums[pivot_index]
    def partition(self,first_index,last_index):
        pivot_index = random.randint(first_index, last_index)
        self.nums[pivot_index], self.nums[last_index] = self.nums[last_index],self.nums[pivot_index]

        for i in range(first_index,last_index):
            if self.nums[i] < self.nums[last_index]:
                self.nums[i],self.nums[first_index] = self.nums[first_index],self.nums[i]
                first_index +=1

        self.nums[first_index],self.nums[last_index] = self.nums[last_index],self.nums[first_index]

        return first_index

quciks = QuickSlect([1,-2,6,8,7,5])
print(quciks.run(1))
        
def factorial(n):
    if n == 0:
        return 1
    
    return n * factorial(n-1)

def factorial_tail(n,acc =1):
    if n == 1:
        return acc
    print(acc)
    return factorial_tail(n-1, n * acc)

def fibonacci_head(n):
    if n <=1:
        return n 
    fib1 = fibonacci_head(n-1)
    fib2 = fibonacci_head(n-2)
    return fib1 + fib2
def fibonacci_tail(n,fib1=0,fib2=1):
    if n == 0:
        return fib1
    return fibonacci_tail(n-1,fib2,fib1+fib2)
    


def hanoi(disk,A,B,C):

    if disk == 0:
        print("move %s from %s to %s" % (disk,A,C))
        return
    hanoi(disk-1,A,C,B)
    print("move %s from %s to %s" % (disk,A,C))
    hanoi(disk-1,B,A,C)
def fibonacci_iteration(n):
    # these are the initial variables with initial values
    a, b = 0, 1
    
    while n >0:
        n -=1
        a,b = b, a+b
    return a

def GCD_tail(A,B):
    if A%B == 0:
        return B
    return GCD_tail(B,A%B)

def GCD_iter(A,B):
    while A%B != 0:
        A,B = B, A%B
    return B

stack = [(1,6)]
print(stack[0][1])