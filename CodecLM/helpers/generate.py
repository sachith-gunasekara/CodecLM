from codeclm.helpers.model import pipe, generation_args

def f_s(prompt: str) -> str:
    return pipe(prompt, **generation_args)[0]['generated_text']

def f_t(prompt: str) -> str:
    pass