Feature: Verify if a point collided with a rectangle

  Scenario: a point is inside a rectangle.
    Given a point with coordinates (7, 8)
    And a rectangle wih coordinates (6, 7) and dimension (2, 2)
    When we want to know whether the point is inside the rectangle
    Then the outcome is true.

  Scenario: a point is not inside a rectangle.
    Given a point with coordinates (5, 9)
    And a rectangle with coordinates (6, 7) and dimension (2, 3)
    When we want to know whether the point is inside the rectangle
    Then the outcome is false.
