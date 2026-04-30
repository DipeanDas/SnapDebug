def build_prompt(language, mode):

    lang_line = "" if language == "Auto" else f"Language: {language}\n"

    base = f"""
You are a programming debugger.

{lang_line}
Analyze input (image or text).

Respond in this exact format:

### Error
(one line)

### Cause
(short reason)

### Fix
(clear steps)

"""

    if mode == "Solution":
        base += """
### Code
(corrected code only if needed)
"""
    else:
        base += """
Do not include full code.
"""

    return base.strip()