Feature: Tests for Best Sellers page UI

  Scenario: Verify that there are 5 links
    Given Open Amazon page
    When Click on Best Sellers link
    Then Verify that there are 5 links

  Scenario: Verify product is added to cart
    Given Open Amazon page
    When Add cup to cart
    Then Verify that cup is in cart