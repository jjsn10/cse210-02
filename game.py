from card import Card

class Game:
    """A person who directs the game. 
    
    The responsibility of a Game is to control the sequence of play.

    Attributes:
        dice (List[Card]): A list of Card instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Game.
        
        Args:
            self (Game): an instance of Game.
        """
       
        self.cards =[]
        self.score = 0
        self.total_score = 300
        self.is_playing = True

        for i in range(2):
            card = Card()
            self.cards.append(card)

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Game): an instance of Game.
        """
        while self.is_playing:
            self.do_updates()
            self.do_outputs()
            self.get_inputs()

    def get_inputs(self):
        """Ask the user if they want to play again.

        Args:
            self (Game): An instance of Game.
        """
        if not self.is_playing:
            return 
            
        play_again = input("Play again? [y/n] ")
        self.is_playing = (play_again == "y")
       
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Game): An instance of Game.
        """

        if not self.is_playing:
            return 
        
        card1 = self.cards[0]
        card1.randomCard()
        print(f"The card is: {card1.number}")

        answer = input("Higher or lower? [h/l]:")

        card2 = self.cards[1]
        card2.randomCard()
        print(f"The card was: {card2.number}")

        if card1.number > card2.number and answer == "l":
            self.score = 100
            self.total_score += self.score
        elif card1.number < card2.number and answer == "h":
            self.score = 100
            self.total_score += self.score
        else:
            self.score = 75
            self.total_score -= self.score
        self.is_playing = (self.total_score > 0)

    def do_outputs(self):
        """Displays the score. Also check if the score is great than 0 
        Args:
            self (Game): An instance of Game.
        """
        if not self.is_playing:
            return

        print(f"Your score is: {self.total_score}")
        print()
        self.is_playing = (self.total_score > 0)

