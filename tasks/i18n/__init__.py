"""Internationalization package for the task management system."""

from .language_manager import LanguageManager

# Create a global language manager instance
language_manager = LanguageManager()

__all__ = ['language_manager'] 