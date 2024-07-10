import re

def extract_encoded_metadata_from_response(response: str) -> str:
    response = response.lower()

    use_case = re.search(r'use case: (.*)', response)
    skills = re.search(r'skills: (.*)', response)
    metadata = {}

    if use_case:
        metadata['use_case'] = use_case.group(1).strip()
    if skills:
        metadata['skills'] = [skill.strip() for skill in skills.group(1).split(',')]
    
    return metadata