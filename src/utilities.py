def rescale(freq, unit):
    if unit == 'k':
        return freq*1000
    elif unit == 'M':
        return freq*1000000
    elif unit == 'G':
        return freq*1000000000
    return freq

# Function to convert frequency to wavelength
def frequency_to_wavelength(frequency: float) -> float:
    # Speed of light in m/s
    c = 299792458
    # Calculate the wavelength
    wavelength = c / frequency
    return wavelength

# Function to convert wavelength to frequency
def wavelength_to_frequency(wavelength: float) -> float:
    # Speed of light in m/s
    c = 299792458
    # Calculate the wavelength
    freq_hz = c / wavelength
    return freq_hz


def calculate_ant_length(frequency: float) -> float:
    if frequency < 30:
        return 286/frequency
    return 300/frequency