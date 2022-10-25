import random, time, os

# Colors For Terminal
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = "\033[4m"

# Full Black Jack Code
class BlackJack():
    def __init__(self):
        self.deck = {}
        # The type of suit
        self.suits = ["Spades", "Hearts", "Clubs", "Diamonds"]

        # The suit value
        self.suits_values = {"Spades": "\u2664", "Hearts": "\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"}

        self.cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

        self.cards_values = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10,
                        "K": 10}

    def mixed_fulldeck(self):
        # Returns tuple of deck mixed
        suits = self.suits * 13
        cards = self.cards * 4
        self.x = list(zip(suits,cards))
        self.deck = random.sample((self.x), k=len(self.x))
        return self.deck

    def calc(self, args):
        # Calculate the amount of points in current cards
        self.total = 0
        for arg in args:
            for key, value in self.cards_values.items():
                if arg[1] == key:
                    if arg[1] == "A" and self.total + 11 > 21:
                        self.total += 1
                    else:
                        self.total += value
        return self.total


    def dealers_choice(self, *args):
        return random.choice(['hit', 'stand'])

    #The game code
    def startgame(self):
        for round in range(1,4):
            deck = (self.mixed_fulldeck())
            # Defining the current card and other variables
            current_card = 4
            players_cards = list((deck[0], deck[2]))
            players_points = 0
            dealers_cards = list((deck[1], deck[3]))
            dealers_points = 0
            choice = ""
            loop = True


            while loop:
                    time.sleep(1)
                    print(f"""{bcolors.OKBLUE}Game Has Started. Dealing Out The Cards Now..\n----------------------------------------------{bcolors.ENDC}""")
                    print(f'There are 3 rounds starting round -> {bcolors.OKGREEN}{round}{bcolors.ENDC}')
                    print(f'Your cards are {players_cards} total: {self.calc(players_cards)}')
                    print(f'Dealers cards {dealers_cards[1]} ***** ')


                    while choice.lower() != "hit" or choice.lower() != "stand":
                        #If the player has 21 he dosen't need to hit
                        if self.calc(players_cards) == 21:
                            print(f"You have 21 let's see what the dealer has")
                            break

                        choice = input("Would you like to hit or stand: ")

                        #Players choice of hit or stand
                        if choice.lower() == 'hit':
                            players_cards.append(deck[current_card])
                            current_card += 1
                            if self.calc(players_cards) > 21:
                                print(f'{bcolors.WARNING}Busted! You made it over 21{bcolors.ENDC}{players_cards}\nYou had a total of {self.calc(players_cards)}')
                                print(f"\nLet see what the dealer had - {dealers_cards} total: {self.calc(dealers_cards)}")
                                round += 1
                                dealers_points += 1
                                dealers_cards.clear()
                                players_cards.clear()
                                time.sleep(5)
                                break
                            else:
                                print(f"Your cards are now {players_cards} total: {self.calc(players_cards)}")
                                choice = input('Would You like to hit again? Y/N: ')
                                if choice.lower() == "n":
                                    break
                        else:
                            print(f"Your cards are now {players_cards} total: {self.calc(players_cards)}")
                            break

                    print("\nDealers turn")
                    dealers_choice = self.dealers_choice()
                    print(f'Dealer chose to {dealers_choice}')
                    if dealers_choice.lower() == 'hit':
                        dealers_cards.append(deck[current_card])
                        current_card += 1
                        if self.calc(players_cards) > 21:
                            print(f'{bcolors.FAIL}The dealer made it above 21{bcolors.ENDC}{dealers_cards}\nDealer had a total of {self.calc(dealers_cards)}')
                            print(f"\nYou had - {players_cards} total: {self.calc(players_cards)}")
                            round += 1
                            players_points += 1
                            break

                    print(f"The dealer had {dealers_cards} total:{self.calc(dealers_cards)}")
                    print(f"\nYou had {players_cards} total: {self.calc(players_cards)}")


                    #Adding points after both finished
                    if 21 > self.calc(dealers_cards) > self.calc(players_cards):
                        dealers_points += 1
                        print(f"{bcolors.UNDERLINE}Dealer Won This Round{bcolors.UNDERLINE}")
                    if self.calc(dealers_cards) == self.calc(players_cards):
                        print(f"{bcolors.OKCYAN}There is a tie{bcolors.ENDC}")
                    else:
                        if 21 > self.calc(players_cards) < self.calc(players_cards):
                            players_points += 1
                            print(f"{bcolors.UNDERLINE}You Won This Round{bcolors.UNDERLINE}")

                    time.sleep(5)
                    round += 1
                    break

        print("""<------------------------------------------>
               Final Results
<------------------------------------------>\n""")
        if players_points > dealers_points:
            print(f'{bcolors.OKGREEN}You beat the dealer with {players_points}/3{bcolors.ENDC}')
        if players_points == dealers_points:
            print(f"{bcolors.HEADER}Its a tie with 1-1{bcolors.ENDC}")
        if players_points < dealers_points:
            print(f'{bcolors.WARNING}The dealer won.{bcolors.ENDC} With {dealers_points} How can you let this happen.')

if __name__ == "__main__":
    b = BlackJack()
    b.startgame()
