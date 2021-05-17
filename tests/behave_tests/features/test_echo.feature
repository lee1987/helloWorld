Feature: test echo
  Scenario: hello world should output hello world
    Given there is a hello world app
    When run the app
    Then there is an output of "hello world"