Feature: Login


  @QA.Geovanni @ui
  Scenario: Validate login valid
    Given what i´m the "MyPilas Login"
    When to fill in the data
    Then i´m online on MyPilas


  @QA.Geovanni @ui @skip
  Scenario: Validate field required
    Given what i´m the "MyPilas Login"
    When click the 'Login'
    Then I'll see error message
      | field  | message |
      | e-mail | asa     |
      | senha  | asa     |


  @QA.Geovanni @ui @skip
  Scenario: Validate login with invalid e-mail and password
    Given what i´m the "MyPilas Login"
    When click the 'Login'
    Then I'll see error message