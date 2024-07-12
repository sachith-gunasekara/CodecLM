import modal

from codeclm.config.modal import app, volume, GPU, MODEL_DIR, image

@app.function(
    gpu=GPU,
    timeout=86400, # Allow one day timout period
    image=image,
    mounts=[
        modal.Mount.from_local_file('setup.py', '/root/setup.py'),
        modal.Mount.from_local_file('pyproject.toml', '/root/pyproject.toml'),
        modal.Mount.from_local_python_packages('codeclm'),
    ],
    volumes={
        MODEL_DIR: volume
    },
    _allow_background_volume_commits=True
)
def encode_dataset_to_metadata(
    dataset_path: str,
    subset: str,
    split: str
):
    from datasets import load_dataset

    from codeclm.encoder import Encoder

    dataset = load_dataset(dataset_path, subset, split=split, streaming=True).drop(['text_token_length', 'text', 'seed_data', 'format', 'audience'])

    def map_func(example):
        encoder = Encoder(example['prompt'])
        metadata = encoder.generate_metadata()

        return {
            'use_case': metadata['use_case'],
            'skills': metadata['skills']
        }

    metadataset = dataset[:10].map(map_func, remove_columns=['prompt'])

    for i in metadataset:
        print(i)

@app.local_entrypoint()
def main(
    dataset_path: str = "HuggingFaceTB/cosmopedia",
    subset: str = "openstax",
    split: str = "train"
):
    encode_dataset_to_metadata.remote(dataset_path, subset, split)