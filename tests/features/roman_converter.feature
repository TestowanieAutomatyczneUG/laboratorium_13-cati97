Feature: Convert Number to Roman Numeral
  converts decimal numbers to roman numerals

  Scenario: Convert 5 to V
    Given a decimal number equal to 5
    When the roman numeral is generated
    Then roman numeral should be V

  Scenario: Convert 24 to XXIV
    Given a decimal number equal to 24
    When the roman numeral is generated
    Then roman numeral should be XXIV


  Scenario: Convert 163 to CLXIII
    Given a decimal number equal to 163
    When the roman numeral is generated
    Then roman numeral should be CLXIII