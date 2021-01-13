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