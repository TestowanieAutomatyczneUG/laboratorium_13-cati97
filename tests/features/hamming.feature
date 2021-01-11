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


  Scenario: Two different strands G and T have distance 1
    Given first strand is G
    And second strand is T
    When the distance is calculated
    Then the distance should be 1

  Scenario: Two different strands AGT and TGC have distance 2
    Given first strand is AGT
    And second strand is TGC
    When the distance is calculated
    Then the distance should be 2


  Scenario: First strand is longer than second raises ValueError
    Given first strand is AATG
    And second strand is AAA
    When the distance is calculated
    Then ValueError should be raised


  Scenario: Second strand is longer than first raises ValueError
    Given first strand is AC
    And second strand is GTCC
    When the distance is calculated
    Then ValueError should be raised


  Scenario: First strand empty raises ValueError
    Given first strand is empty
    And second strand is GTCC
    When the distance is calculated
    Then ValueError should be raised

  Scenario: Second strand empty raises ValueError
    Given first strand is AC
    And second strand is empty
    When the distance is calculated
    Then ValueError should be raised

  Scenario: Two long strands GGACGGATTCTG and AGGACGGATTCT have distance 9
    Given first strand is GGACGGATTCTG
    And second strand is AGGACGGATTCT
    When the distance is calculated
    Then the distance should be 9