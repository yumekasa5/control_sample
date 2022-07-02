import numpy as np
from control_eng.libs.strength_of_materials import *

# def test_calc_shear_stress():
#     calc_shear_stress(340, 20, )

def test_calc_moment_of_inertia_of_area():
    result = calc_moment_of_inertia_of_area(40)
    assert result == 80000 * np.pi