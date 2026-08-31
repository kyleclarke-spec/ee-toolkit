from ee_toolkit import voltage_divider

def test_equal_resistors_halve_voltage():
        assert voltage_divider(10, 1000, 1000) == 5.0