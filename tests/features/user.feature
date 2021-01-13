Feature: Create a user in go rest database
  Scenario: Get firstname
  Given the user wants to create prop first name as "Joanna"
  And the user wants to create prop last name as "Kowalska"
  When get_firstname is run
  Then you should receive "Joanna"

  Scenario: Get lastname
    Given the user wants to create prop first name as "Joanna"
    And the user wants to create prop last name as "Kowalska"
    When get_lastname is run
    Then you should receive "Kowalska"

  Scenario: Create fullname
    Given the user wants to create prop first name as "Joanna"
    And the user wants to create prop last name as "Kowalska"
    When create_fullname is run
    Then you should receive "Joanna Kowalska"

  Scenario: Check email is correct returns Correct
    Given the user wants to create prop first name as "Joanna"
    And the user wants to create prop last name as "Kowalska"
    And the user wants to create prop email as "kowalska@example.com"
    When check_email_is_correct is run
    Then you should receive "Correct"

  Scenario: Check email is correct returns Incorrect
    Given the user wants to create prop first name as "Joanna"
    And the user wants to create prop last name as "Kowalska"
    And the user wants to create prop email as "k2exampleom"
    When check_email_is_correct is run
    Then you should receive "Incorrect"

  Scenario: Check phone is int returns True
    Given the user wants to create prop first name as "Joanna"
    And the user wants to create prop last name as "Kowalska"
    And the user wants to create prop email as "k2exampleom"
    And the user wants to create prop phone as "899555666"
    When check_phone_is_int is run
    Then you should receive "True"