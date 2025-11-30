import sys
import argparse
import cmd
from typing import TextIO


class main_cli(cmd.Cmd):
    def __init__(self, completekey: str = "tab", stdin: TextIO | None = None, stdout: TextIO | None = None) -> None:
        super().__init__(completekey, stdin, stdout)

    def do_f2wl(self, arg: str) -> None:
        """Frequency to wavelength"""
        parser = argparse.ArgumentParser(description="Convert frequency to wavelength")
        parser.add_argument('frequency', help="Frequency")
        parser.add_argument('unit')
        args = parser.parse_args()
    
    
    def do_wl2f(self, arg: str) -> None:
        """Wavelength to frequency"""
        parser = argparse.ArgumentParser(description="Convert wavelength to frequency")
        parser.add_argument('wavelength', help="Wavelength")
        parser.add_argument('unit')
        args = parser.parse_args()


    def do_db2pl(self, arg: str) -> None:
        """dB to Percentage loss"""
        parser = argparse.ArgumentParser(description="Convert dB to power loss in percentage")
        parser.add_argument('decibel', help="Decibel")
        parser.add_argument('unit')
        args = parser.parse_args()


    def do_pl2db(self, arg: str) -> None:
        """Percentage loss to dB"""
        parser = argparse.ArgumentParser(description="Convert power loss in percentage to dB")
        parser.add_argument('percentage',  help="Percentage loss")
        parser.add_argument('unit')
        args = parser.parse_args()

    def do_exit(self, arg: str) -> None:
        """Exit the application"""
        sys.exit()


if __name__ == '__main__':
    main_cli().cmdloop()