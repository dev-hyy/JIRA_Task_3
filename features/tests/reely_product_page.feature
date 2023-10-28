Feature: Tests for Sign In Page UI

#Scenario: Logged out user sees Sign in page when clicking Orders
#  Given Open Amazon page
#  When Click Amazon Orders link
#  Then Verify Sign In page is opened

  Scenario: test
    Given Open Reely page
    Given User enters login credentials
    When Click on off plan at the left side menu
    When Click on the first product
    Then Verify there are 3 options for visualization
    Then Verify the three options of visualization are Architecture, Interior, Lobby
    Then Verify the options of visualization are clickable