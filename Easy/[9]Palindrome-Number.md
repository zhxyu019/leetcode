Logic:

- First, we need to account for exceptions -- test cases where int < 0 eg. -12321, which return false immediately
- Next, we reverse the number digit by digit (alternatively you could store the number as a string in a list)
- To do this, we first find the remainder of the test case number eg. 123 when divided by 10. This will give us the last digit.
- Then, we create the reverse_number by appending the last digit, which in the case of 123, would be 0\*10+3=3
- We then divide the original number by 10 and exclude the remainder, which would basically cut off the last digit of the original number, so in the case of 123 again, that gives us 12.
- We then repeat these steps. So we divide 12 % 10 = 2, then we append it to the reverse_number, which will be 3+2=32, and divide the original number to get 12//10=1
- The reverse_number would be 321 after all iterations, which is not equivalent to the original number so it will return false
- Exception: in the case of 0, the test case returns true, so we do not need to account for it in the exceptions listed.

Runtime: 52ms, beats 18.91% of users...
