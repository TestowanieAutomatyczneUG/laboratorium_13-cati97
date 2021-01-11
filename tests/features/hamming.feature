Feature: Check difference in strands
  checks how many different letters two strands have at the same positions

  Scenario: Two empty strands have distance 0
    Given first strand is empty
    And second strand is empty
    When the distance is calculated
    Then the distance should be 0

  Scenario: Two identical strands have distance 0
    Given first strand is A
    And second strand is A
    When the distance is calculated
    Then the distance should be 0