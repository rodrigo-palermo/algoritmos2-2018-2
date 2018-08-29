Feature:  Return the middle number is a list of 3 different numbers

  Scenario: middle number is in the first place
    Given a list with the numbers (2, 1, 3)
    When we want to know the middle one
    Then the outcome is 2

  Scenario: middle number is in the second place
    Given a list with the numbers (50, -27, -58)
    When we want to know the middle one
    Then the outcome is -27

  Scenario: middel number is in the third place
    Given a list with the numbers (125, 219, 198)
    When we want to know the middle one
    Then the outcome is 198
