Logic:

- For roman numerals, numerals that represent smaller numbers are in front. So first, we need to reverse the string. eg. IV becomes VI.
- Then, you take in the first roman numeral and convert it to the corresponding number, eg. V is converted to 5.
- Then, we see if this corresponding value is larger or smaller than the previous value. eg. in this case previous value is 0.
- If it is bigger, we add it to the value, vice versa. eg. 5 is bigger than 0, so the value becomes 5.
- We then repeat this till all string numerals are checked. eg. the next numeral is I, which converts to 1. 1 is smaller than 5, so we deduct it from the value thus 5-1=4, which is IV, the original string numeral.

Runtime: 17ms, beats 96.78% of users
