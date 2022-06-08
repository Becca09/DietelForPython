from .board import Board


class Game:
    def __int__(self) -> None:
        self.game_board = Board()
        self.player_one = None
        self.player_two = None

    def create_player_one(self, name, sign):
        self.player_one = player(name, sign)


    def create_player_one(self, name, sign):
        self.player_two = player(name, sign)

    def play(self, player: player, position: int):
        print(f"{player.name}'s turn")
        self.game_board.fill_cell(position,player)

    def play(self):
        pass
