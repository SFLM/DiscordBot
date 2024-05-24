from random import choice, randint

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return "bruh"
    elif "hello" in lowered:
        return "hey"
    elif "what" in lowered:
        return "tf u mean 'what' bitch use ur words"
    elif "how" in lowered:
        return "how what"
    elif "roll da dice" in lowered:
        return f"yeah so basically you rolled {randint(1, 6)}"
    else:
        return choice(["uhh, yeah idk man", "yeah i dont know what that means", "what u say"])