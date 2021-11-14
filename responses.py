def sample_resources(input_text):
    user_message= str(input_text).lower()

    if user_message in ("hey"):
        return "Type /new to get my github"

    return "Sorry I dont understand"
