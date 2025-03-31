import wikipedia

def text_handler():
    """
    Function to handle the text retrieval process.
    """
    wikipedia.set_lang('en')  # Language setting for Wikipedia

    try:
        title = wikipedia.random(pages=1)  # Get a random article title
        summary = wikipedia.summary(title, sentences=3)  # Get a short summary

        return f"How about this: '{summary.split('\\n')[0]}' (From Wikipedia: {title})"

    except Exception as e:
        return f"Error: {str(e)}"

# Example usage
# print(text_handler())
