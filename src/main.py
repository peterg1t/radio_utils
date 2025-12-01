import sys
import argparse
import cmd
from typing import TextIO
import math



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


class main_cli(cmd.Cmd):
    def __init__(self, completekey: str = "tab", stdin: TextIO | None = None, stdout: TextIO | None = None) -> None:
        super().__init__(completekey, stdin, stdout)

    def do_f2wl(self, arg: str) -> None:
        """Frequency to wavelength"""
        parser = argparse.ArgumentParser(description="Convert frequency to wavelength")
        parser.add_argument('frequency', help="Frequency")
        parser.add_argument('unit', choices=['Hz', 'k', 'M', 'G'])
        try:
            args = parser.parse_args(arg.split())
            frequency = rescale(float(args.frequency), args.unit)
            wavelength = frequency_to_wavelength(frequency)
            print(f"{wavelength:.4f} m")
        except SystemExit:
            pass
    
    
    def do_wl2f(self, arg: str) -> None:
        """Wavelength to frequency"""
        parser = argparse.ArgumentParser(description="Convert wavelength to frequency")
        parser.add_argument('wavelength', help="Wavelength in meters")
        try:
            args = parser.parse_args(arg.split())
            wavelength = float(args.wavelength)
            frequency = wavelength_to_frequency(wavelength)
            if frequency >= 1e9:
                print(f"{frequency / 1e9:.6g} GHz")

            elif frequency >= 1e6:
                print(f"{frequency / 1e6:.6g} MHz")

            elif frequency >= 1e3:
                print(f"{frequency / 1e3:.6g} kHz")
            
            else: 
                print(f"{frequency:.6g} Hz")
        except SystemExit:
            pass


    def do_db2pl(self, arg: str) -> None:
        """dB to Percentage loss"""
        parser = argparse.ArgumentParser(description="Convert dB to power loss in percentage")
        parser.add_argument('decibel', help="Decibel")
        try:
            args = parser.parse_args(arg.split())
            db = float(args.decibel)
            perloss = 100 * 10 ** (db/20)
            print(f"{perloss:.4f} %")
        except SystemExit:
            pass


    def do_pl2db(self, arg: str) -> None:
        """Percentage loss to dB"""
        parser = argparse.ArgumentParser(description="Convert power loss in percentage to dB")
        parser.add_argument('percentage',  help="Percentage loss")
        try:
            args = parser.parse_args(arg.split())
            perloss = float(args.percentage)
            db = 20*math.log10(perloss/100)
            print(f"{db:.4f} dB")
        except SystemExit:
            pass

    def do_exit(self, arg: str) -> None:
        """Exit the application"""
        sys.exit()


if __name__ == '__main__':
    main_cli().cmdloop()