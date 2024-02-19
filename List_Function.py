'''
ans=0
def sum(a,b):
    ans = a + b
    return ans

def sum(a,b,c):
    ans = a+b+c 
    return ans


print(sum(3,5))
'''

# if __name__ == '__main__':
#     print(sum(4,5))

'''list = [2,3,4,5,7,8,8,8,8,8,8]
list2 = [34,56]
list.insert(3,23)
list.reverse()

print(list)'''


'''Q= list 2nd largest element find'''

# my_list = [1, 10, 15, 5, 35, 70]
# large = my_list[0]

# for i in my_list:
#     if i>large:
#         large = i


# print(large)

# sndLarge=my_list[0] 

# for i in my_list:
#     if i>sndLarge and i != large:
#         sndLarge = i

# print(sndLarge)

''''''
# for i in range (5):
#     print(type(i))
#     i = i+1

# str = "Prem"

# for i in str:
#     print(type(i))

'''
find palindrome no
'''

# str = input("Enter the string to check palindrome ")
# n = len(str)
# l_idx = -1

# ans = True

# for i in range(n//2):
#     if(l_idx>=(-n)):
#         if(str[i] != str[l_idx]):
#             ans = False
    
#     i = i+1
#     l_idx = l_idx - 1

# if ans == True:
#     print("yes")
# else:
#     print("no")


# a = 10
# print(a//2)

'''count digit'''

# def count_digits(num,cnt):
   
#     while(num!=0):
#       cnt = cnt +1
#       num = num//10

#     return cnt


# n = int(input("Enter a number"))
# # print(count_digits(n,0))

# str = str(n)
# print(len(str))


'''
reverse a number 
'''

# def function_to_reverse(num,dummy):
    
#     while(num!=0):
#         n1 = num%10
#         dummy = dummy*10 + n1
#         num = num//10
    
#     return dummy

# # n = 583

# n = int(input("Enter a number"))
# ans = function_to_reverse(n,0)
# print(ans)

'''
pattern printing
###
###
###

'''

# for i in range(0,5):
#     for j in range(0,5):
#         print("#",end=" ")
#     print()


'''
pattern printing
*
**
***
****
*****
******
'''

# for i in range(0,10):
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print()


'''
pattern printing
*******
******
*****
****
***
**
*
'''