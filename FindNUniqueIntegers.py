#SOLUTION FOR LEETCODE QUESTION:
#1304 - FIND N UNIQUE INTEGERS SUM UP TO ZERO
#*****DIFFICULTY - EASY*****

#<summary>
#Method that finds N unique Integers that Sum up to 0 (in an array)
#</summary>
#<param name="n"></param>
#<returns>Array of integers summing up to 0</returns>

def sum_zero(n):
    if n > 1000:
        #As per constraint in question, 1 < n < 1000. Else return 0.
        return []

    #Using basic math. Lower bound is -ve value of n/2. This will satisy the condition of returning 0 if we only have a single element array
    #and want to return a symmetric array (-x, +x)
    sum_array = [i for i in range(-n // 2, (n //2) + 1) if not (n % 2 == 0 and i == 0)]
    print(sum_array)

sum_zero(1000)