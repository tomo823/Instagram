from dataclasses import dataclass
import yaml

@dataclass
class Config:
    name: str  # ex: イーサネット
    address: str
    netmask: str
    gateway: str = None
    metric: str = None

    @classmethod
    def load_yaml(cls, fname):
        with open(fname, "r", encoding="utf-8") as f:
            yml = yaml.safe_load(f)
            cfg = Config(**yml)
            return cfg