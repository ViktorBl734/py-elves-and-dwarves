from abc import ABC, abstractmethod
from app.players.player import Player


class Elf(Player):
    def __init__(self, nickname: str, musical_instrument: str) -> None:
        super().__init__(nickname)
        self._musical_instrument = musical_instrument


    def play_elf_song(self) -> str:
        print(f"{self.nickname} is playing a song on the {self._musical_instrument}")

    @abstractmethod
    def get_rating(self) -> None:
        pass

    @abstractmethod
    def player_info(self) -> None:
        pass

