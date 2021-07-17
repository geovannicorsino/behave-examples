Feature: Validate cds values

  @QA.Geovanni @api
  Scenario: validate that product prices are higher than zero
    When i execute the request https://raccoon-ninja-dummy-api.herokuapp.com/api/v1/cdcatalog?&format=xml
    Then I will have a list of CDs
    And no CD with zero or lower price
    And no CD with empty title