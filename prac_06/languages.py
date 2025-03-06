"""
Intermediate Exercises
Estimate: 30 minutes
Actual: 17 minutes
"""

from prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

programming_languages = [python, ruby, visual_basic]
dynamic_programming_languages = [programming_language for programming_language in programming_languages if programming_language.is_dynamic()]
print(f"The dynamically typed languages are:")
for dynamic_programming_language in dynamic_programming_languages:
    print(dynamic_programming_language.name)
