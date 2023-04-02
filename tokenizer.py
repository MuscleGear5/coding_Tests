def word_count_to_tokens(word_count, max_tokens):
    """Convert the number of words to a set number of tokens using a tokenizer."""
    # calculate average token length based on GPT model name
    if "davinci" in GPT_MODEL:
        avg_token_len = 4.67
    elif "curie" in GPT_MODEL:
        avg_token_len = 4.85
    elif "babbage" in GPT_MODEL:
        avg_token_len = 4.35
    else:
        avg_token_len = 4.75
    # calculate maximum number of tokens based on average token length
    max_tokens = min(int(max_tokens), int(word_count * avg_token_len))
    return max_tokens
