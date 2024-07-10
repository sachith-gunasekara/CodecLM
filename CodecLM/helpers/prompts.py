from pyprojroot import here

def _get_encode_prompt_template() -> str:
    filename = 'codeclm/prompts/encode.txt'

    with open(here(filename), 'r') as f:
        prompt = f.read()
    
    return prompt

def get_encode_prompt(instruction: str) -> str:
    return _get_encode_prompt_template().format(instruction)