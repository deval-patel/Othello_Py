from othello.Controllers.controller import Controller
from othello.player.player_human import PlayerHuman
from othello.player.player_medium import PlayerMedium
from othello.OthelloGame.board import Board


class UserVSMedium(Controller):
    """
    This class is responsible for instantiating the human and medium AI
    players and running the controller through the main class
    """

    def __init__(self):
        """
        Initialize a human player and a medium AI
        """

        super().__init__()
        self.player_one = PlayerHuman(self.othello, Board.player1)
        self.player_two = PlayerMedium(self.othello, Board.player2)


def main():
    """
    Run this controller
    """

    othello_controller = UserVSMedium()
    othello_controller.play()


if __name__ == "__main__":
    main()
