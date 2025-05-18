"""Language manager for handling translations in the task management system."""

from .languages import LANGUAGES

class LanguageManager:
    def __init__(self, language="en"):
        """Initialize the language manager with a default language."""
        self.current_language = language
        self._validate_language()

    def _validate_language(self):
        """Validate that the current language exists in our translations."""
        if self.current_language not in LANGUAGES:
            print(f"Warning: Language '{self.current_language}' not found. Falling back to English.")
            self.current_language = "en"

    def set_language(self, language):
        """Change the current language."""
        self.current_language = language
        self._validate_language()

    def get_text(self, key, *args):
        """Get translated text for a given key with optional format arguments."""
        try:
            text = LANGUAGES[self.current_language][key]
            if args:
                return text.format(*args)
            return text
        except KeyError:
            # Fallback to English if key not found in current language
            try:
                text = LANGUAGES["en"][key]
                if args:
                    return text.format(*args)
                return text
            except KeyError:
                return f"Missing translation: {key}"

    def get_all_languages(self):
        """Get a list of all available languages."""
        return list(LANGUAGES.keys())

    def get_status_options(self):
        """Get translated status options."""
        return [
            self.get_text("STATUS_IN_PROGRESS"),
            self.get_text("STATUS_ON_HOLD"),
            self.get_text("STATUS_ALMOST_DONE"),
            self.get_text("STATUS_COMPLETED")
        ]

    def get_priority_levels(self):
        """Get translated priority levels."""
        return [
            self.get_text("PRIORITY_LOW"),
            self.get_text("PRIORITY_MEDIUM"),
            self.get_text("PRIORITY_HIGH"),
            self.get_text("PRIORITY_URGENT")
        ]

    def get_categories(self):
        """Get translated categories."""
        return [
            self.get_text("CATEGORY_WORK"),
            self.get_text("CATEGORY_PERSONAL"),
            self.get_text("CATEGORY_SHOPPING"),
            self.get_text("CATEGORY_HEALTH"),
            self.get_text("CATEGORY_STUDY"),
            self.get_text("CATEGORY_OTHER")
        ] 