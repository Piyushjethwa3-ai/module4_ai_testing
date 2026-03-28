def get_llm_response(prompt):
    # Mock AI responses for teaching
    if "doctor" in prompt.lower():
        return "He is a skilled doctor with years of experience."
    elif "leader" in prompt.lower():
        return "She is an strong leader."
    elif prompt.strip() == "":
        return "Invalid input provided."
    return "This is a generic AI response."