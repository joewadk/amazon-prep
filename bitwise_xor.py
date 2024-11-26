#Problem statement
'''
Developers at Amazon are working on a new algorithm using the Bitwise XOR operation.

Given an array arr of even length n, developers can perform an operation on a given array which is defined below as many times as necessary:

Choose two indices L and R, where 
0<=L≤R<n.
Let x be the bitwise XOR of all elements of the subarray represented by indices L and R of the given array.
Assign all elements of the chosen subarray to x.
Given an integer array arr, find the minimum number of operations required to make all elements of the given array equal to zero.

Note: Bitwise XOR for an array of numbers is determined by examining each bit position across all numbers in the array.

The binary representations are:

13 = 1101₂
6 = 0110₂
10 = 1010₂
7 = 0111₂
The count of set bits for each bit position:

bit-position 0 = 2 (from 13, 7) → Result: 0
bit-position 1 = 3 (from 6, 10, 7) → Result: 1
bit-position 2 = 3 (from 13, 6, 7) → Result: 1
bit-position 3 = 2 (from 13, 10) → Result: 0
Final result: 0110₂, or 6.
'''
def bitwise_xor(arr,l,r):
    
    zero=[0]*(r-l+1)
    if zero==arr[l:r+1]:  #base case. if its already 0'd then no need to xor
        return 0
    x=0
    for i in range(l,r+1): #get the xor of the array
        x=x^arr[i]
    for i in range(l,r+1): #assign the xor to the subarray
        arr[i]=x
    print(arr)
    if zero==arr[l:r+1]: #if its already 0'd then return 1
        return 1
    else:
        return 2 
    #by this point we already did x xor x. due to associative property of xor, our first xor gives us the cumulative value of x. by the second xor we do x xor x, which is 0


print(bitwise_xor([0,2,2,0],1,2)) #expecting 1