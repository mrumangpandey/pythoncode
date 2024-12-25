class Utils:
    def find_max(self, numbers):
        max_num = numbers[0]  # Use a different name to avoid shadowing
        for i in numbers:
            if i > max_num:
                max_num = i  # Fix the assignment issue
        return max_num  # Return the maximum value after the loop

# Create an instance of Utils
utils = Utils()

# Input list
ls = [1, 2, 4, 5, 6, 710]

# Call the method and print the result
print(utils.find_max(ls))
