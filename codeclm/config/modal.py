import modal
from modal import Image

# Initialize modal app
app = modal.App()

# Setup volume for storing model weights
volume = modal.Volume.from_name("codeclm", create_if_missing=True)
MODEL_DIR = "/vol"

GPU = 'T4'

image = (
    Image.from_registry("thr3a/cuda12.1-torch")
    .poetry_install_from_file("pyproject.toml", force_build=True)
)