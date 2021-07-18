Feature: Validate product values

  @QA.Geovanni @api
  Scenario: validate that product prices are higher than zero
    When i execute the request https://geovanni-corsino-sds2.herokuapp.com/products
    Then I will have a list of pasta