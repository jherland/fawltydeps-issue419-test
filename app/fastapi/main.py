import fastapi

app = fastapi.FastAPI()

print(f"fastapi found at {fastapi.__file__}")

import same_dir_module

print(f"same_dir_module found at {same_dir_module.__file__}")

import sys

print(f"sys.path is {sys.path}")

