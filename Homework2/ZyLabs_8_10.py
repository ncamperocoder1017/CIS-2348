# Nicolas Campero
# 1856853

# get string input from user
pal_word = input()
new_word = pal_word.replace(' ', '')  # Replace any spaces to test for palindromes in multiple-word phrases

if new_word == new_word[::-1]:
    print(pal_word, "is a palindrome")
else:
    print(pal_word, "is not a palindrome")
