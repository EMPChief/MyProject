# Internationalization (i18n) Documentation

## Overview
The internationalization system provides multi-language support for the task management system, allowing users to interact with the application in their preferred language.

## Components

### LanguageManager Class
- Location: `i18n/language_manager.py`
- Purpose: Manages language selection and text translation
- Features:
  - Language switching
  - Text translation
  - Fallback handling
  - Message formatting

### Language Definitions
- Location: `i18n/languages.py`
- Supported Languages:
  - English (en)
  - Spanish (es)
  - Norwegian Bokmål (nb)
  - Chinese (zh)
  - Romanian (ro)

## Usage

### Basic Translation
```python
from tasks.i18n import language_manager

# Get translated text
text = language_manager.get_text("KEY")

# Get formatted text
text = language_manager.get_text("KEY_WITH_ARGS").format(arg1, arg2)
```

### Language Selection
```python
# Set language
language_manager.set_language("es")  # Spanish

# Get available languages
languages = language_manager.get_all_languages()
```

## Translation Keys

### Common Messages
- `WELCOME`: Welcome message
- `GOODBYE`: Exit message
- `ERROR_UNEXPECTED`: Unexpected error
- `INVALID_INPUT`: Invalid input error

### Authentication Messages
- `LOGIN_PROMPT`: Login prompt
- `REGISTER_PROMPT`: Registration prompt
- `USER_NOT_FOUND`: User not found error
- `LOGIN_SUCCESS`: Successful login

### Task Messages
- `TASK_ADDED`: Task added confirmation
- `TASK_UPDATED`: Task updated confirmation
- `TASK_DELETED`: Task deleted confirmation
- `NO_TASKS`: No tasks found message

### Field Labels
- `FIELD_NAME`: "Name"
- `FIELD_DESCRIPTION`: "Description"
- `FIELD_PRIORITY`: "Priority"
- `FIELD_CATEGORY`: "Category"
- `FIELD_STATUS`: "Status"

### Status Options
- `STATUS_IN_PROGRESS`: "In Progress"
- `STATUS_ON_HOLD`: "On Hold"
- `STATUS_ALMOST_DONE`: "Almost Done"
- `STATUS_COMPLETED`: "Completed"

### Priority Levels
- `PRIORITY_LOW`: "Low"
- `PRIORITY_MEDIUM`: "Medium"
- `PRIORITY_HIGH`: "High"
- `PRIORITY_URGENT`: "Urgent"

### Categories
- `CATEGORY_WORK`: "Work"
- `CATEGORY_PERSONAL`: "Personal"
- `CATEGORY_SHOPPING`: "Shopping"
- `CATEGORY_HEALTH`: "Health"
- `CATEGORY_STUDY`: "Study"
- `CATEGORY_OTHER`: "Other"

## Adding a New Language

1. Add language dictionary to `languages.py`:
```python
"language_code": {
    "KEY": "Translated text",
    ...
}
```

2. Update supported languages list
3. Add language selection option
4. Test all translations

## Fallback System
1. Try requested language
2. Fall back to English
3. Return key name if no translation found

## Best Practices
1. Always use translation keys, never hardcode strings
2. Use format placeholders for variable text
3. Keep translations consistent across languages
4. Document all translation keys
5. Test with all supported languages

## Future Improvements
- [ ] Add right-to-left language support
- [ ] Implement language auto-detection
- [ ] Add translation management tools
- [ ] Support language variants
- [ ] Add translation memory
- [ ] Implement machine translation fallback 