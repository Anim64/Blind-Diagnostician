from ModelConfig.Loader import load_config
from Models import ModelRegistry

def build_orchestrator():
    config = load_config("model-config.yaml")

    models = ModelRegistry(config)
