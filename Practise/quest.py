# def ispalindrome(s):
#     s=s.lower().replace(" ", "")
#     return s == s[::-1]

# print(ispalindrome('Kotok'))

# --------------------------------------------------------------------------------------

# def second_largest(num):
#     unique_numbers = list(set(num))
#     if len(unique_numbers) < 2:
#         print('Not enough number')
    
#     unique_numbers.sort(reverse=True)    
#     return unique_numbers[1]
    
    
# ls = [1,2,3,4,5,10,20,80,99]
# print(second_largest(ls))    

# --------------------------------------------------------------------------------------

# def fibonacci(n):
#     seq = [0,1]
#     for i in range (2,n):
#         seq.append(seq[-1] + seq[-2])
#     return seq[:n]
    
    
# print(fibonacci(15))


# -----------------------------------------------------------------------------------------

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int (n ** 0.5) +1):
#         if n % i ==0 :
#             return False
#     return True    


# print(is_prime(29))


# ----------------------------------------------------------------------------------


# def factorial(n):
#     if n == 0 or n == 1:
#         return 1 
#     return n * factorial(n-1)


# print(factorial(5))

# ----------------------------------------------------

# def remove_duplicates(ls):
#     unique_numbers = list(set(ls))
#     return unique_numbers


# numbers = [1,2,3,4,3,4,4]
# print(remove_duplicates(numbers))


# def remove_duplicates(n):
#     unique_number = []
#     for i in n:
#         if i not in unique_number:
#             unique_number.append(i)
            
#     return unique_number       


# ls = [1,1,1,1,2,2,2,2,3,43,3,4]
# print(remove_duplicates(ls))


# ---------------------------------------------------------------------------

# def merge_sorted_list(a,b):
#     merged=[]
#     i=j=0
#     while i < len(a) and j < len(b):
#         if a[i] < b[j]:
#             merged.append(a[i])
#             i+=1
#         else:
#             merged.append(b[j])
#             j+=1
            
#         merged.extend(a[i:])
#         merged.extend(b[j:])    
#         return merged
    

# a=[1,2,3,4,6,7,8]
# b=[1,5,9,11,12] 

# print(merge_sorted_list(a,b))   

# ---------------------------------------------------------------------------------------------------------------------------------------



