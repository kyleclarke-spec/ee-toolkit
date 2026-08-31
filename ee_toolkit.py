def voltage_divider(vin, r1, r2):
    """Vout across R2 in a series divider."""
    return vin * r2 / (r1 + r2)