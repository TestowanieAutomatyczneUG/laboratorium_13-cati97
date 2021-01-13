Feature: Create a user in go rest database

  @exampletag
  Scenario: Get firstname
  Given the user wants to create prop first name as "Joanna"
  And the user wants to create prop last name as "Kowalska"
  When get_firstname is run
  Then you should receive "Joanna"

  @exampletag
  Scenario: Get lastname
    Given the user wants to create prop first name as "Joanna"
    And the user wants to create prop last name as "Kowalska"
    When get_lastname is run
    Then you should receive "Kowalska"

  @exampletag
  Scenario: Create fullname
    Given the user wants to create prop first name as "Joanna"
    And the user wants to create prop last name as "Kowalska"
    When create_fullname is run
    Then you should receive "Joanna Kowalska"

  @exampletag
  Scenario: Check email is correct returns Correct
    Given the user wants to create prop first name as "Joanna"
    And the user wants to create prop last name as "Kowalska"
    And the user wants to create prop email as "kowalska@example.com"
    When check_email_is_correct is run
    Then you should receive "Correct"

  @exampletag
  Scenario: Check email is correct returns Incorrect
    Given the user wants to create prop first name as "Joanna"
    And the user wants to create prop last name as "Kowalska"
    And the user wants to create prop email as "k2exampleom"
    When check_email_is_correct is run
    Then you should receive "Incorrect"

  @exampletag
  Scenario: Check phone is int returns True
    Given the user wants to create prop first name as "Joanna"
    And the user wants to create prop last name as "Kowalska"
    And the user wants to create prop email as "k2exampleom"
    And the user wants to create prop phone as "899555666"
    When check_phone_is_int is run
    Then you should receive "True"

  @exampletag
  Scenario: Check phone is int returns True
    Given the user wants to create prop first name as "Joanna"
    And the user wants to create prop last name as "Kowalska"
    And the user wants to create prop phone as "899555666"
    And the user wants to create prop user_id as "1234"
    When check_user_id_is_length_four is run
    Then you should receive "True"

  @exampletag
  Scenario: Check phone is int returns False
    Given the user wants to create prop first name as "Joanna"
    And the user wants to create prop last name as "Kowalska"
    And the user wants to create prop phone as "899555666"
    And the user wants to create prop user_id as "34"
    When check_user_id_is_length_four is run
    Then you should receive "False"