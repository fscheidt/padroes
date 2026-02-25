from abc import ABC, abstractmethod
from pathlib import Path

class Image(ABC):
    @abstractmethod
    def export(self, filepath: str):
        pass

class PNG(Image):
    def __init__(self, channels: int = 16):
        self.channels = channels 
    def export(self, filepath: str, rgba: bool = None):
        print("="*40, f"\nPNG Image (channels={self.channels})")
        print(f"exporting file \n{filepath}")
        ext = Path(filepath).suffix
        # execução de lógica de conversão ...
        if rgba:
            print("\t=> Applying rgba filter")
        newfile = str(filepath).replace(ext,".png")        
        print(f"file save: {newfile}")


class JPG(Image):
    def __init__(self, quality: float):
        self.quality = quality or 0.4
    def export(self, filepath: str):
        print("="*40, f"\nJPG (quality={self.quality})")
        print(f"Converting {filepath} to JPG")
        print("✅ complete")
