# x="civic"
# def ispalindrome(word):   
#      # function to check palindrome
#   rev=word[::-1]   
#   if (rev==word):
#    return True
#   else:
#         return False
# def result(text):
#   if ispalindrome(text):
#         print("good")
#   else:
#    print("bad")
# def check_multiple():
#         words=["mom","hello","cry","moon","level"]
#         for w in words:print(w,ispalindrome(w))
# # extra unused variables
# a=100
# b=200
# c=300
# # misplaced indentation and bad naming
# def BadFunc():
#      for i in range(5):
#           if i==2:
#                  print("middle")
#           else:
#                    print("not middle")
#      return None
#      print("never runs")
# #wrong code
# result(x)
# check_multiple()
# BadFunc()
# print("Done")
# print("extra indent") # error

"""Palindrome check."""
from typing import List
def ispalindrome(word: str) -> bool:
    """Return True if the word reads the same forward and backward."""
    rev = word[::-1]
    return rev == word


def result(text: str) -> None:
    """Print 'good' if palindrome else 'bad'."""
    if ispalindrome(text):
        print("good")
    else:
        print("bad")


def check_multiple() -> None:
    """Print each word with its palindrome verdict."""
    words: List[str] = ["mom", "hello", "cry", "moon", "level"]
    for w in words:
        print(w, ispalindrome(w))


def bad_func() -> None:
    """Replicate the original loop prints without unreachable code."""
    for i in range(5):
        if i == 2:
            print("middle")
        else:
            print("not middle")


def main() -> None:
    """Run the same calls as the original script."""
    x = "civic"
    result(x)
    check_multiple()
    bad_func()
    print("Done")
    print("extra indent")  # kept as a normal print


if __name__ == "__main__":
    main()
