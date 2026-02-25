from abc import ABC, abstractmethod
from pathlib import Path

class Image(ABC):
    @abstractmethod
    def export(self):
        pass

class PNG(Image):
    def __init__(self, filepath, channels: int = 16):
        self.filepath = filepath
        self.channels = channels 
    def export(self, rgba: bool = None):
        print("="*40, f"\nPNG Image (channels={self.channels})")
        print(f"exporting file \n{self.filepath}")
        ext = Path(self.filepath).suffix
        # execução de lógica de conversão ...
        if rgba:
            print("\t=> Applying rgba filter")
        newfile = str(self.filepath).replace(ext,".png")        
        print(f"file save: {newfile}")


class JPG(Image):
    def __init__(self, filepath, quality: float = 0.4):
        self.filepath = filepath
        self.quality = quality
    def export(self):
        print("="*40, f"\nJPG (quality={self.quality})")
        print(f"Converting {self.filepath} to JPG")
        print("✅ complete")
