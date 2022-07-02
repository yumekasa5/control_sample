import numpy as np

def calc_moment_of_inertia_of_area(diamter_mm):
    """中実円形断面の断面2次モーメント"""
    ip_mm4 = (np.pi * (diamter_mm)^4) /32
    return ip_mm4

def calc_shear_stress(torque, radius_mm, moment_ip_mm4):
    """ねじりトルクが生じる場合のせん断応力"""
    shear_stress = (torque * radius_mm) / moment_ip_mm4
    return shear_stress