def ConstructItemHashString(weapon='AK-47', skin='Asiimov', wear='Field-Tested'):
    return f"{weapon} | {skin} ({wear})"

def DeconstructItemHashString(string='AK-47 | Asiimov (Field-Tested)'):
    return weapon, skin, wear