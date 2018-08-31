Feature: Verify if two rectangles collided with each other.

Scenario: The rectangles collided
  Given two rectangles on coordinates (6,7) (7,8) and dimensions (2,2) (2,2)
  When we want to know if the rectangles collided
  Then the outcome is true.

  Scenario: The rectangles did not collided
    Given two rectangles on coordinates (6,7) (2,5) and dimensions (2,2) (2,2)
    When we want to know if the rectangles collided
    Then the outcome is false.
