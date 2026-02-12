import yaml

from Config.Schemas import AppConfig

def load_config(path: str) -> AppConfig:
    with open(path, "r") as f:
        raw_config = yaml.safe_load(f)
    return AppConfig(**raw_config)
