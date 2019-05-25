"""
Test util functions
"""
import pytest
import os
import subprocess

import cct.main

here = os.path.abspath(os.path.join(__file__, os.pardir))
repo_root = os.path.abspath(os.path.join(here, os.pardir))


def test_main():
    assert cct.main.ret42() == 42
    
    
def test_docker():    
    cmd = 'docker pull ghdl/ghdl'
    
    # Pytest asserts the non-zero return status of subprocess
    out = subprocess.check_output(cmd.split(' '))
    