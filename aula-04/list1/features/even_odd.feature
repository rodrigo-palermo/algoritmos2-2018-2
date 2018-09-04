Feature: Return the parity of a number in a list

  Scenario: For the list [0, 1, 2, 4], return [0(par), 1(impar), 2(par), 3(impar)]
  Given a knonw list
  When we want to know the parity of the numbers in the list
  Then the outcome is [True, False, True, False]
