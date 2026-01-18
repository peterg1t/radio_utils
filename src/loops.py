import math


def perimeter(radius: float) -> float:
    return 2*math.pi*radius

def surface_resistance(freq: float) -> float:
    """R_s

    Args:
        w (float): angular frequency
        sigma (float): electrical conductivity
        mu_0: permeability of free space
    """
    mu_0 = 4*math.pi*10**(-7) #(H/m)
    sigma = 5.8*10**(7) #Siemens/m
    return math.sqrt((2*math.pi*freq*mu_0)/(2*sigma))

def radiation_loss(N: int, R_s: float, r_conductor: float, R_p: float, R_0: float):
    l_perim = perimeter(r_conductor)
    return N *(l_perim/r_conductor)*R_s*(R_p/R_0+1)

def radiation_efficiency(r_rad: float, r_loop: float, r_e: float) -> float:
    """_summary_

    Args:
        r_rad (float): _description_
        r_loop (float): _description_
        r_e (float): in Ohms

    Returns:
        _type_: _description_
    """
    return r_rad/(r_rad + r_loop + r_e)

