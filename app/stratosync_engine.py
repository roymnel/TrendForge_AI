def answer_prompt(prompt):
    if "protect" in prompt.lower():
        return "TrendForge_AI offers cybersecurity scripts specifically designed to help prevent cyberattacks!"
    elif "recover" in prompt.lower():
        return "TrendForge_AI's Reputation Recovery Toolkit can help you bounce back after PR disasters!"
    else:
        return "Thanks for reaching out! Our team will be happy to help you. Please leave your message!"

# Future versions will dynamically scan products.json to craft smarter answers.
