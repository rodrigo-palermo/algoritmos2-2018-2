Feature: From a list, computes some operations and queries

  Scenario: The biggest is 3, with index 2
  Given the list [1,2,3]
  When we want to know the biggest and its index
  Then the outcome is "Biggest: 3, Index: 2"

  Scenario: The smallest is 1, with index 0
  Given the list [1,2,3]
  When we want to know the smallest and its index
  Then the outcome is "Smallest: 1, Index: 0"

  Scenario: The sum of the even numbers is 2
  Given the list [1,2,3]
  When we want to know the sum of the even numbers
  Then the outcome is "Sum of even numbers: 2"

  Scenario: The sum of the odd numbers is 4
  Given the list [1,2,3]
  When we want to know the sum of the odd numbers
  Then the outcome is "Sum of odd numbers: 4"

  Scenario: The division of sum of the even numbers by the sum of odd numbers is 0.5
  Given the list [1,2,3]
  When we want to know the sum of the even divided by sum of the odd 
  Then the outcome is 0.5

  Scenario: The inverse order of the list is [3,2,1]
  Given the list [1,2,3]
  When we want to know the list in its inverse order
  Then the outcome is "Inverse order list: [3, 2, 1]"
