from pathlib import Path

import environ

ROOT_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
env.read_env(ROOT_DIR / ".env")
