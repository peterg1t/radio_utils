import math
from utilities import wavelength_to_frequency


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

def radiation_loss_resistance(N: int, a: float, b: float, R_s: float, R_p: float, R_0: float):
    """Calculate radiation loss resistance of a loop

    Args:
        N (int): Numebr of loops
        a (float): radius of the loop
        b (float): thickness of the wire
        R_s (float): Surface resistance
        R_p (float): _description_
        R_0 (float): loss resistance per unit length (in Ω / m)

    Returns:
        float: Radiation loss resistance of N loops
    """
    return N *(a/b)*R_s*(R_p/R_0+1)


def radiation_resistance_loop(N: int, b: float, wavelength: float) -> float:
    """Calculate Radiation resistance of an N number of loops

    Args:
        N (int): Number of loops
        a (float): Radius of the loop
        wavelength (float): Wavelength

    Returns:
        float: Radiation resistance of an N number of loops
    """
    return (N**2)*20*math.pi**2*((2*math.pi*b)/wavelength)**4


def radiation_efficiency(N: int, a: float, b: float, wavelength: float, r_e: float) -> float:
    """Calculate radiation efficiency

    Args:

        r_e (float): in Ohms

    Returns:
        float: Efficiency
    """
    freq = wavelength_to_frequency(wavelength)
    print("Frequency", freq, N, b, wavelength)
    r_rad = radiation_resistance_loop(N, b, wavelength)
    print("Radiation resistance loop", r_rad)
    R_s = surface_resistance(freq)
    print("Surface resistance", R_s)
    R_p=0.5
    R_0=1
    r_loop = radiation_loss_resistance(N, a, b, R_s, R_p, R_0)
    print("Efficiency", r_rad, r_loop, r_rad/(r_rad + r_loop + r_e))
    return r_rad/(r_rad + r_loop + r_e)

