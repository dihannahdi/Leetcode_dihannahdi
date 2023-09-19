class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # Initialize max_wealth to a very small value
        max_wealth = float('-inf')
        
        # Iterate through each customer's accounts
        for customer in accounts:
            # Calculate the wealth of the current customer
            wealth = sum(customer)
            
            # Update max_wealth if the current customer's wealth is greater
            if wealth > max_wealth:
                max_wealth = wealth
        
        return max_wealth