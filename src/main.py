import argparse
import cmd
from typing import TextIO


class main_cli(cmd.Cmd):
    def __init__(self, completekey: str = "tab", stdin: TextIO | None = None, stdout: TextIO | None = None) -> None:
        super().__init__(completekey, stdin, stdout)

    def f2wl(self, arg: str) -> None:
        parser = argparse.ArgumentParser(description="Convert frequency to wavelength")
    
    
    def wl2f(self, arg: str) -> None:
        parser = argparse.ArgumentParser(description="Convert wavelength to frequency")


    def db2pl(self, arg: str) -> None:
        parser = argparse.ArgumentParser(description="Convert dB to power loss in percentage")

    def pl2db(self, arg: str) -> None:
        parser = argparse.ArgumentParser(description="Convert power loss in percentage to dB")