Feature: Create a starfield

#Scenario 1
  Scenario: Choose Y coord and star speed
  Given two positive integer values 0 and 600
  And  a list with values 1, 2 and 3
  When I creat an object tha representas a star
  Then the X coord is 800
  And the Y coord is between 0 and 600
  And the star speed is 1, 2 or 3
