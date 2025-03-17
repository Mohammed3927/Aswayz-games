import discord
from discord.ext import commands
import random
import time

# Define a dictionary to store the games
games = {}

# Define a base class for games
class Game:
    def __init__(self, ctx):
        self.ctx = ctx
        self.players = []

    async def start(self):
        # Start the game
        pass

    async def join(self):
        # Add a player to the game
        self.players.append(self.ctx.author)

    async def leave(self):
        # Remove a player from the game
        self.players.remove(self.ctx.author)

# Define a class for the Roulette game
class Roulette(Game):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.min_players = 2
        self.max_players = 10
        self.starting_time = 30

    async def start(self):
        # Check if the minimum number of players have joined
        if len(self.players) < self.min_players:
            await self.ctx.send(f'Not enough players have joined. Minimum required: {self.min_players}')
            return

        # Start the game
        await self.ctx.send('Roulette game started!')

        # Wait for the starting time
        await discord.utils.sleep(self.starting_time)

        # Spin the wheel
        winner = random.choice(self.players)
        await self.ctx.send(f'The winner is {winner.mention}!')

# Define a class for the Tic-Tac-Toe game
class TicTacToe(Game):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.min_players = 2
        self.max_players = 2
        self.starting_time = 30

    async def start(self):
        # Check if the minimum number of players have joined
        if len(self.players) < self.min_players:
            await self.ctx.send(f'Not enough players have joined. Minimum required: {self.min_players}')
            return

        # Start the game
        await self.ctx.send('Tic-Tac-Toe game started!')

        # Wait for the starting time
        await discord.utils.sleep(self.starting_time)

        # Create the game board
        board = [' ' for _ in range(9)]

        # Play the game
        while True:
            # Get the current player
            player = self.players[0]

            # Get the player's move
            move = await self.ctx.send(f'{player.mention}, enter your move (1-9):')

            # Update the game board
            board[int(move.content) - 1] = 'X'

            # Check if the player has won
            if self.check_win(board):
                await self.ctx.send(f'{player.mention} wins!')
                break

            # Switch players
            self.players.reverse()

# Define a class for the Mafia game
class Mafia(Game):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.min_players = 5
        self.max_players = 15
        self.starting_time = 30

    async def start(self):
        # Check if the minimum number of players have joined
        if len(self.players) < self.min_players:
            await self.ctx.send(f'Not enough players have joined. Minimum required: {self.min_players}')
            return

        # Start the game
        await self.ctx.send('Mafia game started!')

        # Wait for the starting time
        await discord.utils.sleep(self.starting_time)

        # Assign roles
        roles = ['Mafia' for _ in range(2)] + ['Citizen' for _ in range(len(self.players) - 2)]
        random.shuffle(roles)

        # Play the game
        while True:
            # Get the current player
            player = self.players[0]

            # Get the player's role
            role = roles[self.players.index(player)]

            # Get the player's action
            if role == 'Mafia':
                action = await self.ctx.send(f'{player.mention}, enter the player you want to kill (1-{len(self.players)}):')
            else:
                action = await self.ctx.send(f'{player.mention}, enter the player you want to investigate (1-{len(self.players)}):')

            # Update the game state
            if role == 'Mafia':
                # Kill the player
                self.players.remove(self.players[int(action.content) - 1])
            else:
                # Investigate the player
                investigated_player = self.players[int(action.content) - 1]
                investigated_role = roles[self.players.index(investigated_player)]
                await self.ctx.send(f'{player.mention}, {investigated_player.mention} is a {investigated_role}.')

            # Check if the game is over
            if len(self.players) == 1:
                await self.ctx.send(f'{self.players[0].mention} wins!')
                break

            # Switch players
            self.players.reverse()

# Define a class for the Musical Chairs game
class MusicalChairs(Game):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.min_players = 2
        self.max_players = 10
        self.starting_time = 30

    async def start(self):
        # Check if the minimum number of players have joined
        if len(self.players) < self.min_players:
            await self.ctx.send(f'Not enough players have joined. Minimum required: {self.min_players}')
            return

        # Start the game
        await self.ctx.send('Musical Chairs game started!')

        # Wait for the starting time
        await discord.utils.sleep(self.starting_time)

        # Play the game
        while True:
            # Get the current player
            player = self.players[0]

            # Get the player's action
            action = await self.ctx.send(f'{player.mention}, enter the chair you want to sit in (1-{len(self.players)}):')

            # Update the game state
            if int(action.content) - 1 == len(self.players) - 1:
                # The player sat in the last chair
                await self.ctx.send(f'{player.mention} wins!')
                break
            else:
                # The player sat in a chair that is not the last one
                self.players.remove(player)

            # Switch players
            self.players.reverse()

# Define a class for the Rock-Paper-Scissors game
class RockPaperScissors(Game):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.min_players = 2
        self.max_players = 2
        self.starting_time = 30

    async def start(self):
        # Check if the minimum number of players have joined
        if len(self.players) < self.min_players:
            await self.ctx.send(f'Not enough players have joined. Minimum required: {self.min_players}')
            return

        # Start the game
        await self.ctx.send('Rock-Paper-Scissors game started!')

        # Wait for the starting time
        await discord.utils.sleep(self.starting_time)

        # Play the game
        while True:
            # Get the current player
            player = self.players[0]

            # Get the player's action
            action = await self.ctx.send(f'{player.mention}, enter your choice (rock, paper, or scissors):')

            # Update the game state
            if action.content == 'rock':
                if self.players[1].content == 'scissors':
                    await self.ctx.send(f'{player.mention} wins!')
                    break
                elif self.players[1].content == 'paper':
                    await self.ctx.send(f'{self.players[1].mention} wins!')
                    break
                else:
                    await self.ctx.send('It\'s a tie!')
            elif action.content == 'paper':
                if self.players[1].content == 'rock':
                    await self.ctx.send(f'{player.mention} wins!')
                    break
                elif self.players[1].content == 'scissors':
                    await self.ctx.send(f'{self.players[1].mention} wins!')
                    break
                else:
                    await self.ctx.send('It\'s a tie!')
            elif action.content == 'scissors':
                if self.players[1].content == 'paper':
                    await self.ctx.send(f'{player.mention} wins!')
                    break
                elif self.players[1].content == 'rock':
                    await self.ctx.send(f'{self.players[1].mention} wins!')
                    break
                else:
                    await self.ctx.send('It\'s a tie!')

            # Switch players
            self.players.reverse()

# Define a class for the Hide and Seek game
class HideAndSeek(Game):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.min_players = 2
        self.max_players = 10
        self.starting_time = 30

    async def start(self):
        # Check if the minimum number of players have joined
        if len(self.players) < self.min_players:
            await self.ctx.send(f'Not enough players have joined. Minimum required: {self.min_players}')
            return

        # Start the game
        await self.ctx.send('Hide and Seek game started!')

        # Wait for the starting time
        await discord.utils.sleep(self.starting_time)

        # Play the game
        while True:
            # Get the current player
            player = self.players[0]

            # Get the player's action
            action = await self.ctx.send(f'{player.mention}, enter the hiding spot you want to choose (1-{len(self.players)}):')

            # Update the game state
            if int(action.content) - 1 == len(self.players) - 1:
                # The player chose the last hiding spot
                await self.ctx.send(f'{player.mention} wins!')
                break
            else:
                # The player chose a hiding spot that is not the last one
                self.players.remove(player)

            # Switch players
            self.players.reverse()

# Define a class for the Replica game
class Replica(Game):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.min_players = 2
        self.max_players = 10
        self.starting_time = 30

    async def start(self):
        # Check if the minimum number of players have joined
        if len(self.players) < self.min_players:
            await self.ctx.send(f'Not enough players have joined. Minimum required: {self.min_players}')
            return

        # Start the game
        await self.ctx.send('Replica game started!')

        # Wait for the starting time
        await discord.utils.sleep(self.starting_time)

        # Play the game
        while True:
            # Get the current player
            player = self.players[0]

            # Get the player's action
            action = await self.ctx.send(f'{player.mention}, enter the word you think is the replica:')

            # Update the game state
            if action.content == 'replica':
                await self.ctx.send(f'{player.mention} wins!')
                break
            else:
                self.players.remove(player)

            # Switch players
            self.players.reverse()

# Define a class for the Button Game
class ButtonGame(Game):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.min_players = 1
        self.max_players = 1
        self.starting_time = 30

    async def start(self):
        # Check if the minimum number of players have joined
        if len(self.players) < self.min_players:
            await self.ctx.send(f'Not enough players have joined. Minimum required: {self.min_players}')
            return

        # Start the game
        await self.ctx.send('Button Game started!')

        # Wait for the starting time
        await discord.utils.sleep(self.starting_time)

        # Play the game
        while True:
            # Get the current player
            player = self.players[0]

            # Get the player's action
            action = await self.ctx.send(f'{player.mention}, press the button to win:')

            # Update the game state
            if action.content == 'button':
                await self.ctx.send(f'{player.mention} wins!')
                break
            else:
                self.players.remove(player)

            # Switch players
            self.players.reverse()

# Define a class for the Fastest Typing game
class FastestTyping(Game):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.min_players = 1
        self.max_players = 1
        self.starting_time = 30

    async def start(self):
        # Check if the minimum number of players have joined
        if len(self.players) < self.min_players:
            await self.ctx.send(f'Not enough players have joined. Minimum required: {self.min_players}')
            return

        # Start the game
        await self.ctx.send('Fastest Typing game started!')

        # Wait for the starting time
        await discord.utils.sleep(self.starting_time)

        # Play the game
        while True:
            # Get the current player
            player = self.players[0]

            # Get the player's action
            action = await self.ctx.send(f'{player.mention}, type the text to win:')

            # Update the game state
            if action.content == 'text':
                await self.ctx.send(f'{player.mention} wins!')
                break
            else:
                self.players.remove(player)

            # Switch players
            self.players.reverse()

# Define a class for the Unscramble game
class Unscramble(Game):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.min_players = 1
        self.max_players = 1
        self.starting_time = 30

    async def start(self):
        # Check if the minimum number of players have joined
        if len(self.players) < self.min_players:
            await self.ctx.send(f'Not enough players have joined. Minimum required: {self.min_players}')
            return

        # Start the game
        await self.ctx.send('Unscramble game started!')

        # Wait for the starting time
        await discord.utils.sleep(self.starting_time)

        # Play the game
        while True:
            # Get the current player
            player = self.players[0]

            # Get the player's action
            action = await self.ctx.send(f'{player.mention}, unscramble the text to win:')

            # Update the game state
            if action.content == 'unscrambled_text':
                await self.ctx.send(f'{player.mention} wins!')
                break
            else:
                self.players.remove(player)

            # Switch players
            self.players.reverse()

# Define a class for the Merge Letters game
class MergeLetters(Game):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.min_players = 1
        self.max_players = 1
        self.starting_time = 30

    async def start(self):
        # Check if the minimum number of players have joined
        if len(self.players) < self.min_players:
            await self.ctx.send(f'Not enough players have joined. Minimum required: {self.min_players}')
            return

        # Start the game
        await self.ctx.send('Merge Letters game started!')

        # Wait for the starting time
        await discord.utils.sleep(self.starting_time)

        # Play the game
        while True:
            # Get the current player
            player = self.players[0]

            # Get the player's action
            action = await self.ctx.send(f'{player.mention}, merge the letters to win:')

            # Update the game state
            if action.content == 'merged_letters':
                await self.ctx.send(f'{player.mention} wins!')
                break
            else:
                self.players.remove(player)

            # Switch players
            self.players.reverse()

# Define a class for the Flags game
class Flags(Game):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.min_players = 1
        self.max_players = 1
        self.starting_time = 30

    async def start(self):
        # Check if the minimum number of players have joined
        if len(self.players) < self.min_players:
            await self.ctx.send(f'Not enough players have joined. Minimum required: {self.min_players}')
            return

        # Start the game
        await self.ctx.send('Flags game started!')

        # Wait for the starting time
        await discord.utils.sleep(self.starting_time)

        # Play the game
        while True:
            # Get the current player
            player = self.players[0]

            # Get the player's action
            action = await self.ctx.send(f'{player.mention}, guess the country of the flag to win:')

            # Update the game state
            if action.content == 'country':
                await self.ctx.send(f'{player.mention} wins!')
                break
            else:
                self.players.remove(player)

            # Switch players
            self.players.reverse()

# Define a class for the Reverse Word game
class ReverseWord(Game):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.min_players = 1
        self.max_players = 1
        self.starting_time = 30

    async def start(self):
        # Check if the minimum number of players have joined
        if len(self.players) < self.min_players:
            await self.ctx.send(f'Not enough players have joined. Minimum required: {self.min_players}')
            return

        # Start the game
        await self.ctx.send('Reverse Word game started!')

        # Wait for the starting time
        await discord.utils.sleep(self.starting_time)

        # Play the game
        while True:
            # Get the current player
            player = self.players[0]

            # Get the player's action
            action = await self.ctx.send(f'{player.mention}, reverse the word to win:')

            # Update the game state
            if action.content == 'reversed_word':
                await self.ctx.send(f'{player.mention} wins!')
                break
            else:
                self.players.remove(player)

            # Switch players
            self.players.reverse()

# Define a class for the Missing Letter game
class MissingLetter(Game):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.min_players = 1
        self.max_players = 1
        self.starting_time = 30

    async def start(self):
        # Check if the minimum number of players have joined
        if len(self.players) < self.min_players:
            await self.ctx.send(f'Not enough players have joined. Minimum required: {self.min_players}')
            return

        # Start the game
        await self.ctx.send('Missing Letter game started!')

        # Wait for the starting time
        await discord.utils.sleep(self.starting_time)

        # Play the game
        while True:
            # Get the current player
            player = self.players[0]

            # Get the player's action
            action = await self.ctx.send(f'{player.mention}, fill in the missing letter to win:')

            # Update the game state
            if action.content == 'filled_in_letter':
                await self.ctx.send(f'{player.mention} wins!')
                break
            else:
                self.players.remove(player)

            # Switch players
            self.players.reverse()

# Define a class for the Fix the Word game
class FixTheWord(Game):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.min_players = 1
        self.max_players = 1
        self.starting_time = 30

    async def start(self):
        # Check if the minimum number of players have joined
        if len(self.players) < self.min_players:
            await self.ctx.send(f'Not enough players have joined. Minimum required: {self.min_players}')
            return

        # Start the game
        await self.ctx.send('Fix the Word game started!')

        # Wait for the starting time
        await discord.utils.sleep(self.starting_time)

        # Play the game
        while True:
            # Get the current player
            player = self.players[0]

            # Get the player's action
            action = await self.ctx.send(f'{player.mention}, fix the word to win:')

            # Update the game state
            if action.content == 'fixed_word':
                await self.ctx.send(f'{player.mention} wins!')
                break
            else:
                self.players.remove(player)

            # Switch players
            self.players.reverse()

# Define a class for the Number Sorting game
class NumberSorting(Game):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.min_players = 1
        self.max_players = 1
        self.starting_time = 30

    async def start(self):
        # Check if the minimum number of players have joined
        if len(self.players) < self.min_players:
            await self.ctx.send(f'Not enough players have joined. Minimum required: {self.min_players}')
            return

        # Start the game
        await self.ctx.send('Number Sorting game started!')

        # Wait for the starting time
        await discord.utils.sleep(self.starting_time)

        # Play the game
        while True:
            # Get the current player
            player = self.players[0]

            # Get the player's action
            action = await self.ctx.send(f'{player.mention}, sort the numbers to win:')

            # Update the game state
            if action.content == 'sorted_numbers':
                await self.ctx.send(f'{player.mention} wins!')
                break
            else:
                self.players.remove(player)

            # Switch players
            self.players.reverse()

# Define a class for the Emoji Match game
class EmojiMatch(Game):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.min_players = 1
        self.max_players = 1
        self.starting_time = 30

    async def start(self):
        # Check if the minimum number of players have joined
        if len(self.players) < self.min_players:
            await self.ctx.send(f'Not enough players have joined. Minimum required: {self.min_players}')
            return

        # Start the game
        await self.ctx.send('Emoji Match game started!')

        # Wait for the starting time
        await discord.utils.sleep(self.starting_time)

        # Play the game
        while True:
            # Get the current player
            player = self.players[0]

            # Get the player's action
            action = await self.ctx.send(f'{player.mention}, match the emoji to win:')

            # Update the game state
            if action.content == 'matched_emoji':
                await self.ctx.send(f'{player.mention} wins!')
                break
            else:
                self.players.remove(player)

            # Switch players
            self.players.reverse()

# Add the games to the dictionary
games = {
    'roulette': Roulette,
    'tic-tac-toe': TicTacToe,
    'mafia': Mafia,
    'musical_chairs': MusicalChairs,
    'rock-paper-scissors': RockPaperScissors,
    'hide_and_seek': HideAndSeek,
    'replica': Replica,
    'button_game': ButtonGame,
    'fastest_typing': FastestTyping,
    'unscramble': Unscramble,
    'merge_letters': MergeLetters,
    'flags': Flags,
    'reverse_word': ReverseWord,
    'missing_letter': MissingLetter,
    'fix_the_word': FixTheWord,
    'number_sorting': NumberSorting,
    'emoji_match': EmojiMatch,
}
