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

from typing import List
def ispalindrome(word: str) -> bool:
    rev = word[::-1]
    return rev == word


def result(text: str) -> None:
    if ispalindrome(text):
        print("good")
    else:
        print("bad")


def check_multiple() -> None:
    words: List[str] = ["mom", "hello", "cry", "moon", "level"]
    for w in words:
        print(w, ispalindrome(w))


def bad_func() -> None:
    for i in range(5):
        if i == 2:
            print("middle")
        else:
            print("not middle")


def main() -> None:
    x = "civic"
    result(x)
    check_multiple()
    bad_func()
    print("Done")
    print("extra indent")  # kept as a normal print


if __name__ == "__main__":
    main()

