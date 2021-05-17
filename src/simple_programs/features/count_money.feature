Feature: Simples programs

  Scenario Outline: i need count the number of notes for <value>
    Given what i have <value>
    When i count the minimun number of notes
    Then i will have <quantity> notes

    Examples:
      | value | quantity |
      | 100   | 1        |
      | 101   | 2        |
      | 50    | 1        |
      | 372   | 6       |
      | 216   | 5        |
      | 80    | 3        |