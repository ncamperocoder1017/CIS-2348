# Nicolas Campero
# 1856853

# get string input from user
pal_word = input('Enter a word to see if the word entered is a palindrome:')


def word_is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False


flag = word_is_palindrome(pal_word)

if flag:
    print(pal_word, "is a palindrome")
else:
    print(pal_word, "is not a palindrome")
