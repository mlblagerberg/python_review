"""
General Python Testing Review
January 16th, 2024
Madeleine Lagerberg
"""

# Import standard testing framework
import unittest

# General idea is to have functions defined in a seperate module that can be imported/sourced by other python scripts.
# Test code is then housed in a if statement that checks if the script is being run as the primary python script or 
# if it is being imported as a module. If it is imported the test code does not run.

# Check if script is executatable or imported
if __name__ == "__main__":
    # run test code

