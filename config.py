import os

# define OpenAI API key variable
os.environ["OPENAI_API_KEY"] = "YOUR_API_KEY_HERE"

# define GPT model name variable (e.g. "davinci-3.5")
os.environ["GPT_MODEL"] = "YOUR_GPT_MODEL_NAME_HERE"

# define maximum token amount for the GPT model
os.environ["MAX_TOKENS"] = "YOUR_MAX_TOKENS_HERE"

# define API endpoint URL
os.environ["API_ENDPOINT"] = "YOUR_API_ENDPOINT_URL_HERE"

# define default prompt to be used when generating the outline
os.environ["DEFAULT_PROMPT"] = "YOUR_DEFAULT_PROMPT_HERE"

# define minimum and maximum number of words that can be requested for the essay
os.environ["MIN_WORDS"] = "YOUR_MINIMUM_WORDS_HERE"
os.environ["MAX_WORDS"] = "YOUR_MAXIMUM_WORDS_HERE"

# define filename and directory path where the generated text will be saved
os.environ["OUTPUT_DIR"] = "YOUR_OUTPUT_DIRECTORY_HERE"
os.environ["OUTPUT_FILE"] = "YOUR_OUTPUT_FILENAME_HERE"

# define message to be displayed when the text has been successfully generated and saved to a file
os.environ["SUCCESS_MESSAGE"] = "Text has been generated and saved to file."
CACHE_DIR = "cache/"
CACHED_TEXT_FILE = "cached_text_{}_{}.json"
CACHED_SECTION_FILE = "cached_section_{}_{}_{}.json"
CACHED_TIMESTAMP_FILE = "cached_timestamps_{}_{}.json"
