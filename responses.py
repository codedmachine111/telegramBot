def sample_resources(input_text):
    user_message= str(input_text).lower()

    if user_message in ("line"):
        return "to generate a new line type in /start"

    return "Sorry I dont understand"