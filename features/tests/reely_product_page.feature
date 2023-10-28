Feature: Tests for Reely Visualization Options

  Scenario: Logged In User Selects Visualization Options
    Given Open Reely page
    Given User enters login credentials
    When Click on off plan at the left side menu
    When Click on the first product
    Then Verify there are 3 options for visualization
    Then Verify the three options of visualization are Architecture, Interior, Lobby
    Then Verify the options of visualization are clickable