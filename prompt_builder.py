def build_prompt(mode):

    base_prompt = """
    You are an expert programming debugger.
    Analyze the uploaded image (code error or stack trace).
    """

    if mode == "Hints":
        return base_prompt + """
        Give only hints and guidance.
        Do NOT provide full code solution.
        """

    elif mode == "Solution with code":
        return base_prompt + """
        Explain the error clearly and provide corrected code.
        """

    return base_prompt