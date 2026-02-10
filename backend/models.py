from dataclasses import dataclass

@dataclass
class Probe:
    uid: str

@dataclass
class FlashResult:
    success: bool
    message: str
