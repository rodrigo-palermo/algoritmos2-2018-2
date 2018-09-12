Feature: Display a starfield animation.
  As a user,
  I want to see a starfield moving,
  To think about life

Scenario: Choosing Y coordinate and the star speed.
  Given two positive integer values, 0 and 600
    And a list with values 1, 2 and 3
  When I create an object that represents a star
  Then its X coordinate is 800
    And its Y coordinate is between 0 and 600
    And its speed is 1, 2 or 3

Scenario: Moving the star.
  Given an object reresenting a star
  When I move the star
  Then its X coordinate changes according to its speed
    And its Y coordinate does not change
    And its speed does not change

Scenario: Creating multiple stars.
  Given two positive integer values, 0 and 600
    And a list with values 1, 2 and 3
  When I create a list with 20 stars
  Then the X coordinate of each star is 800
    And the Y coordinate of each star is between 0 and 600
    And the speed of each star is 1, 2 or 3

Scenario: Moving multiple stars.
  Given a list of objects representing stars
  When I move the stars in the list
  Then the X coordinate of each star changes according to its speed
    And the Y coordinate of each star does not change
    And the speed of each star does not change

Scenario: Deleting stars
  Given a specific list of stars:
    | x | y | speed |
    | 10| 10 | 3 |
    | 10| 20 | 2 |
    | 10| 14 | 1 |
  When I move the stars 4 times
  Then the list will have only 2 stars:
    | x | y | speed |
    | 2 | 20 | 2 |
    | 6 | 14 | 1 |
