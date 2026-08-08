from game.game import Game, Player
from agents.agent import Agent
from agents.random_agent import RandomAgent
from training.trainer import Trainer


def main() -> None:
    game: Game = Game()
    x_agent: Agent = RandomAgent()
    o_agent: Agent = RandomAgent()
    trainer: Trainer = Trainer(game, x_agent, o_agent)

    x_wins: int = 0
    o_wins: int = 0
    draw: int = 0
    episodes: int = 20000

    for episode in range(episodes):
        winner = trainer.run_episode()
        if winner == Player.X:
            x_wins += 1
        elif winner == Player.O:
            o_wins += 1
        else:
            draw += 1

    print("Stats:")
    print(f"X \t {x_wins} ({(x_wins / episodes) * 100}%)")
    print(f"O \t {o_wins} ({(o_wins / episodes) * 100}%)")
    print(f"Draw \t {draw} ({(draw / episodes) * 100}%)")



if __name__ == '__main__':
    main()