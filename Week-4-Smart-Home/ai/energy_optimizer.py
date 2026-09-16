"""Rule-guided energy optimization baseline.

This intentionally provides an interpretable baseline before deploying a learned
policy. A production system should train on measured device power and validate
recommendations against user comfort and safety constraints.
"""


def recommend(occupied: bool, temperature: float, light: float, hvac_on: bool, lights_on: bool):
    actions = []
    if not occupied and lights_on:
        actions.append("turn_lights_off")
    if not occupied and hvac_on:
        actions.append("set_hvac_to_eco")
    if occupied and light > 800 and lights_on:
        actions.append("dim_lights")
    if occupied and temperature < 18 and not hvac_on:
        actions.append("consider_heating")
    return actions


if __name__ == "__main__":
    print(recommend(False, 24.0, 900, True, True))
