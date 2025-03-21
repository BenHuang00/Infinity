from setuptools import setup, find_packages

with open('requirements.txt', 'r', encoding='utf-8') as f:
    requirements = f.read().splitlines()

setup(
    name='infinity',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'torch==2.5.1',
        'torchvision==0.20.1',
        'torchaudio==2.5.1',
        'easydict',
        'typed-argument-parser',
        'seaborn',
        'kornia',
        'gputil',
        'colorama',
        'omegaconf',
        'pandas',
        'timm==0.9.6',
        'decord',
        'transformers',
        'pytz',
        'wandb',
        'imageio',
        'einops',
        'openai',
        'httpx==0.20.0',
        'opencv-python',
        'flash_attn'
    ]
)