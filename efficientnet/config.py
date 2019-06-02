from .utils import AttrDict, load_yaml


class Config(AttrDict):

    @classmethod
    def from_yaml(cls, f):
        data = load_yaml(f)
        return cls(**data)
