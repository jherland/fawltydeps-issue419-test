#!/usr/bin/env python3

import isort

config = isort.Config(src_paths=("app/fastapi", "."))

print(isort.place_module_with_reason("fastapi", config=config))
print(isort.place_module_with_reason("same_dir_module", config=config))
