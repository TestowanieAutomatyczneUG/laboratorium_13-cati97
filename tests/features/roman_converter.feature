Feature: Convert Number to Roman Numeral
  converts decimal numbers to roman numerals

  Scenario: Convert 5 to V
    Given a decimal number equal to 5
    When the roman numeral is generated
    Then roman numeral should be V