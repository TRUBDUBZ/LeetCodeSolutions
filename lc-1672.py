# You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

# A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

class Solution:
    def maximumWealth(self, accounts):
        max_wealth = 0

        for customers in accounts:  # Fix the variable name to "customers"
            wealth = sum(customers)  # Calculate the wealth of the current customer
            max_wealth = max(max_wealth, wealth)

        return max_wealth
