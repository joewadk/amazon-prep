'''
Problem Statement:

Amazon's software developers are enhancing their inventory management system with a new feature. The goal is to analyze an array of n products, where the price of the i-th product is given by prod_price[i]. The objective is to determine the minimum number of price adjustments needed to ensure that the Amazon pricing algorithm yields the same price for the sums of all subarrays of length k within the array prod_price.

Price Adjustment Operations:

Modify any number of values in the array prod_price[i] to any positive integer.
Task:

Given the array prod_price and a positive integer k, find the minimum number of changes required so that the sum of elements in all subarrays of length k is equal.

Note:

A subarray is a contiguous segment of an array.
Example:

Given:

n = 4
prod_price = [5, 7, 7, 8]
k = 2
Output:

The minimum number of changes required is 2.'''


def inventory_management(prod_price,k):
    