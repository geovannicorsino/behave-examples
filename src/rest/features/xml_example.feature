Feature: Validate product values

  Scenario Outline: validate that product prices are higher than zero
    Given what i have the "<endpoint>"
    When read the prices
    Then I will not have any product with zero or lower price
    Examples:
      | endpoint      |
      | example ninja |