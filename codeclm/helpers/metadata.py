from codeclm.helpers.prompts import get_encode_prompt
from codeclm.helpers.generate import f_s
from codeclm.helpers.response import extract_encoded_metadata_from_response

def get_metadata(instruction: str):
    prompt = get_encode_prompt(instruction)
    response = f_s(prompt)
    metadata = extract_encoded_metadata_from_response(response)

    return metadata