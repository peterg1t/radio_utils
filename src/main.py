import sys
import argparse
import cmd
from typing import TextIO
import math
from utilities import rescale, frequency_to_wavelength, wavelength_to_frequency, calculate_ant_length
from loops import radiation_efficiency
import plotext as plt



class main_cli(cmd.Cmd):
    def __init__(self, completekey: str = "tab", stdin: TextIO | None = None, stdout: TextIO | None = None) -> None:
        super().__init__(completekey, stdin, stdout)

    def do_f2wl(self, arg: str) -> None:
        """Frequency to wavelength"""
        parser = argparse.ArgumentParser(description="Convert frequency to wavelength")
        parser.add_argument('frequency', required=True, help="Frequency")
        parser.add_argument('unit', required=True, choices=['Hz', 'k', 'M', 'G'])
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
        parser.add_argument('wavelength', required=True, help="Wavelength in meters")
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
        parser.add_argument('decibel', required=True, help="Decibel")
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
        parser.add_argument('percentage', required=True, help="Percentage loss")
        try:
            args = parser.parse_args(arg.split())
            perloss = float(args.percentage)
            db = 20*math.log10(perloss/100)
            print(f"dB = {db:.4f} dB")
        except SystemExit:
            pass

    def do_ant_len(self, arg:str) -> None:
        """Calculate the antenna length for a given frequency in MHz"""
        parser = argparse.ArgumentParser(description="Calculate antenna length")
        parser.add_argument('frequency', required=True, help="In MHz")
        try:
            args = parser.parse_args(arg.split())
            freq = float(args.frequency)
            antenna_length = calculate_ant_length(freq)
            print(f"Electrical wavelength = {antenna_length:.4f} m")
            print(f"Half-wavelength = {antenna_length/2:.4f} m")
            print(f"Quarter-wavelength = {antenna_length/4:.4f} m")
        except SystemExit:
            pass

    def do_bands(self, arg:str) -> None:
        """Print hams band information"""
        try:
            print(f"160 m    ->  1 800 -  1 850   kHz, center ->  1 875    kHz ")
            print(f" 80 m    ->  3 500 -  4 000   kHz, center ->  3 750    kHz ")
            # print(f"60 m   -> 5.330 -  5.400 kHz center -> 5 365 kHz ")
            print(f" 40 m    ->  7 000 -  7 300   kHz, center ->  7 150    kHz ")
            print(f" 30 m    -> 10 100 - 10 150   kHz, center -> 10 125    kHz ")
            print(f" 20 m    -> 14 000 - 14 350   kHz, center -> 14 175    kHz ")
            print(f" 17 m    -> 18 068 - 18 168   kHz, center -> 18 118    kHz ")
            print(f" 15 m    -> 21 000 - 21 450   kHz, center -> 21 225    kHz ")
            print(f" 12 m    -> 24 890 - 24 990   kHz, center -> 24 940    kHz ")
            print(f" 10 m    ->     28 -     29.7 MHz, center ->     28.35 MHz ")
            print(f"  6 m    ->     50 -     54   MHz, center ->     52    MHz ")
            print(f"  2 m    ->    144 -    148   MHz, center ->    146    MHz ")
            print(f"  1.25 m ->    222 -    225   MHz, center ->    223.5  MHz ")
            print(f" 70 cm   ->    430 -    450   MHz, center ->    440    MHz ")

            
            
        except SystemExit:
            pass

    def do_impedance_load(self, arg: str) -> None:
        """Calculate impedance from a pure resistive value on the Smith Chart (needs NanoVNA)"""
        parser = argparse.ArgumentParser(description="Calculate impedance from the load")
        parser.add_argument('r', type=float, required=True, help="In Ohms")
        try:
            args = parser.parse_args(arg.split())
            resistive = float(args.r)
            print(f"Impedance = { math.sqrt(resistive*50) } Ohms")
        except SystemExit:
            pass


    def do_mag_loop_eff(self, arg: str) -> None:
        """Tool to plot the effficiency of a magnetic loop antenna.
            
            Args:
                 -n: Number of loops (integer)
                -wd: Wire/Conductor diameter (in mm)
                -ld: Loop diameter (in mm)
                -re: (Additional resistance due to external losses (in Ohms)

        """
        bands=[160, 80, 60, 40, 20, 15, 10]
        efficiency = []
        parser = argparse.ArgumentParser(description="Plot magloop eficiency")
        parser.add_argument('-n', type=int, required=True, help="Number of loops") # Number of loops
        parser.add_argument('-wd', type=float, required=True, help="In mm") # Conductor diameter
        parser.add_argument('-ld', type=float, required=True, help="In mm") # Loop diameter
        parser.add_argument('-re', type=float, required=True, help="In Ohms") #Additional resistance due to external losses, due mainly from capacitor contact resistance and proximity-to-ground effects. Use Re=0.0 to assume the loop is in free-space with no capacitor losses
        try:
            args = parser.parse_args(arg.split())
            N = int(args.n)
            wire_diameter = float(args.wd)*10**(-3)
            loop_diameter = float(args.ld)*10**(-3)
            resistance = float(args.re)
            for band in bands:
                efficiency.append(radiation_efficiency(N, wire_diameter, loop_diameter, band, 0.0))
            plt.clf()
            plt.plot(bands, efficiency, marker='fhd')
            plt.scatter(bands, efficiency, marker='@')
            plt.xscale("log")
            plt.show()
        except SystemExit:
            pass

    def do_exit(self, arg: str) -> None:
        """Exit the application"""
        sys.exit()


if __name__ == '__main__':
    main_cli().cmdloop()
    
