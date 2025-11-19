
# Function to convert frequency to wavelength
def frequency_to_wavelength(frequency):
    # Speed of light in m/s
    c = 299792458
    # Calculate the wavelength
    wavelength = c / frequency
    return wavelength

try:
    while True:
        # Input frequency from the user
        try:
            frequency = float(input("Enter frequency in Hertz (Hz): "))
            
            if frequency <= 0:
                print("Frequency must be a positive number.")
            else:
                wavelength = frequency_to_wavelength(frequency)
                print(f"The wavelength for {frequency} Hz is {wavelength:.2f} meters.")
        except ValueError:
            print("Please enter a valid number for frequency.")

except KeyboardInterrupt:
    print("\nProgram interrupted by user. Exiting...")
