Feature: testing the function from main
	Scenario: testing the function chastnoe(3, 2)
		Given I put values [3, 2] into the function
		Then I get 1.5

  Scenario: testing the function chastnoe(3, 0)
		Given I put values [3, 0] into the function
		Then I get Error
