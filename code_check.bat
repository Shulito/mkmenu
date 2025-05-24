ruff format main.py src/
ruff check --fix main.py src/
ruff check --fix --select I main.py src/
mypy --strict main.py src/
