def is_palindrome(name):
    # Remove spaces and convert to lowercase for a case-insensitive check
    cleaned_name = name.replace(" ", "").lower()
    
    # Check if the cleaned name is equal to its reverse
    return cleaned_name == cleaned_name[::-1]

# Input a name from the user
name = input("Enter a name: ")

if is_palindrome(name):
    print(f"{name} is a palindrome!")

else:
    print(f"{name} is not a palindrome.")
