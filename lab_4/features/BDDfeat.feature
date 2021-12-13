Feature: testing the function get_roots
	Scenario: get roots of biquadratic equation for coef. [-4, 16, 0]
		Given I put coefficients [-4, 16, 0] into the function
		Then I get roots [-2.0, 0.0, 2.0]

	Scenario: get roots of biquadratic equation for coef. [1, 1, -2]
		Given I put coefficients [1, 1, -2] into the function
		Then I get roots [-1.0, 1.0]

    Scenario: get roots of biquadratic equation for coef. [1, 1, 1]
		Given I put coefficients [1, 1, 1] into the function
		Then I get roots []