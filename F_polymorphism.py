from pathlib import Path
from abc import abstractmethod, ABC

class Audiofile(ABC):
    ext: str    # 클래스변수 - 값을 지정해두지 않음

    def __init__(self, filepath: Path) -> None:
        if not filepath.suffix == self.ext:
            raise ValueError("invalid file format.")
        self.filepath = filepath

    @abstractmethod
    def play(self)->None:
        pass

class MP3File(Audiofile):
    ext = ".mp3"

    def play(self)->None:
        print(f"Playing {self.filepath} as mp3")

class WavFile(Audiofile):
    ext = ".wav"

    def play(self)->None:
        print(f"Playing {self.filepath} as wav")

class OggFile(Audiofile):
    ext = ".ogg"

    def play(self)->None:
        print(f"Playing {self.filepath} as ogg")

if __name__ == "__main__":
    audiofiles = [MP3File(Path("Heart of the sunrise.mp3")),
                  WavFile(Path("Roundabout.wav")),
                  OggFile(Path("Heart of the sunrise.ogg"))]

    for audiofile in audiofiles:
        audiofile.play()