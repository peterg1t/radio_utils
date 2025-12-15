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


def calculate_ant_length(frequency: float) -> float:
    if frequency < 30:
        return 286/frequency
    return 300/frequency


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
            print(f"Wavelength = {wavelength:.4f} m")
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
                print(f"Frequency = {frequency / 1e9:.6g} GHz")

            elif frequency >= 1e6:
                print(f"Frequency = {frequency / 1e6:.6g} MHz")

            elif frequency >= 1e3:
                print(f"Frequency = {frequency / 1e3:.6g} kHz")
            
            else: 
                print(f"Frequency = {frequency:.6g} Hz")
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
            print(f"% loss = {perloss:.4f} %")
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
            print(f"dB = {db:.4f} dB")
        except SystemExit:
            pass

    def do_ant_len(self, arg:str) -> None:
        """Calculate the antenna length for a given frequency"""
        parser = argparse.ArgumentParser(description="Calculate antenna length")
        parser.add_argument('frequency',  help="In MHz")
        try:
            args = parser.parse_args(arg.split())
            freq = float(args.frequency)
            antenna_length = calculate_ant_length(freq)
            print(f"Electrical wavelength = {antenna_length:.4f} m")
            print(f"Half-wavelength = {antenna_length/2:.4f} m")
            print(f"Quarter-wavelength = {antenna_length/4:.4f} m")
        except SystemExit:
            pass

    def do_exit(self, arg: str) -> None:
        """Exit the application"""
        sys.exit()


if __name__ == '__main__':
    main_cli().cmdloop()