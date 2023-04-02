import time
import sys
import random
from typing import List
from openai import ApiError


def prompt_user(message, data_type=str, min_value=None, max_value=None):
    """Prompt the user for input and return the entered value."""
    while True:
        try:
            user_input = data_type(input(message))
            if min_value is not None and user_input < min_value:
                raise ValueError(f"Value must be at least {min_value}.")
            if max_value is not None and user_input > max_value:
                raise ValueError(f"Value cannot exceed {max_value}.")
            return user_input
        except ValueError as e:
            print(e)


def prompt_confirmation(message):
    """Prompt the user for confirmation and return True or False."""
    while True:
        response = input(f"{message} [y/n] ")
        if response.lower() in ["y", "yes"]:
            return True
        elif response.lower() in ["n", "no"]:
            return False
        else:
            print("Invalid input. Please enter y/n.")


def generate_sections(client, gpt_model, outline, num_tokens):
    """Generate each section of the text and return them in a list."""
    sections =     # calculate the number of API requests needed to generate each section
    num_sections = len(outline)
    tokens_per_section = [len(section.split()) for section in outline]
    requests_per_section = [num_tokens // tokens for tokens in tokens_per_section]
    requests_per_section[-1] += num_tokens % tokens_per_section[-1]
    
    sections = []
    
    # generate each section of the text
    for i in range(num_sections):
        section = outline[i]
        num_requests = requests_per_section[i]
        
        for j in range(num_requests):
            try:
                prompt = f"{DEFAULT_PROMPT} {section}"
                response = client.completions.create(
                    engine=gpt_model,
                    prompt=prompt,
                    max_tokens=tokens_per_section[i],
                    n=1,
                    stop=None,
                    temperature=0.7,
                )
                text = response.choices[0].text
                sections.append(text)
            except ApiError as e:
                handle_error("API Error", e)
    
    # return the list of sections
    return sections
def generate_sections(subject: str, essay_type: str, outline: List[str], num_tokens: int, client: Client) -> List[str]:
    """Generate each section of the text using the GPT model."""
    sections = []
    for i, section in enumerate(outline):
        cached_text = load_cached_section(subject, essay_type, i)
        if cached_text is not None:
            print(f"Cached text found for {subject} {essay_type} section {i}.")
            sections.append(cached_text)
        else:
            num_requests = calculate_num_requests(num_tokens, len(section.split()))
            section_text = ""
            for j in range(num_requests):
                try:
                    prompt = f"{os.environ['DEFAULT_PROMPT']} {section}"
                    response = client.completions.create(
                        engine=os.environ['GPT_MODEL'],
                        prompt=prompt,
                        max_tokens=len(section.split()),
                        n=1,
                        stop=None,
                        temperature=0.7,
                    )
                    text = response.choices[0].text
                    section_text += text
                except ApiError as e:
                    handle_error("API Error", e)
            save_cached_section(section_text, subject, essay_type, i)
            sections.append(section_text)
    return sections
def generate_text(subject: str, essay_type: str, outline: List[str], num_tokens: int) -> str:
    """Generate the entire text from the outline."""
    client = authenticate_api()
    sections = generate_sections(subject, essay_type, outline, num_tokens, client)
    text = "".join(sections)
    save_cached_text(text, subject, essay_type)
    return text

