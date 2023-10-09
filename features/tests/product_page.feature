Feature: Tests for Product Page UI

  Scenario: Verify that user can click each color
    Given Open Amazon product B07BJKRR25 page
    When Store product name
    Then Verify user can click through colors
