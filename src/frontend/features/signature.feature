Feature: Signature


  @QA.Geovanni @ui
  Scenario: Signature
    Given what i´m the "MyPilas Signature"
    When to fill in the data
    Then i did my signature on MyPilas

  @QA.Geovanni @ui @skip
  Scenario: Signature
    Given what i´m the "MyPilas Signature"
    When click on 'Assinar MyPilas'
    Then i´ll see the error message
      | field  | message            |
      | e-mail | e-mail is required |