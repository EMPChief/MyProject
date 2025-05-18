"""Utility functions for the task management system."""

import os
import platform


def clear_screen():
    """Clear the terminal screen in a cross-platform way."""
    # For Windows
    if platform.system().lower() == "windows":
        os.system('cls')
    # For Linux/Unix/MacOS
    else:
        os.system('clear')


def print_with_clear(text="", clear_first=True):
    """Print text with optional screen clearing.
    
    Args:
        text (str): Text to print after clearing the screen
        clear_first (bool): Whether to clear screen before printing
    """
    if clear_first:
        clear_screen()
    if text:
        print(text) 