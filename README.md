# Tic-Tac-Toe Agent
A reinforcement learning agent that learn to plays Tic-Tac-Toe through self-play.

This project contains 4 core modules
1. Environment
2. Agent
3. Trainer
4. Evaluation

## Planned Project Architecture 
```
tictactoe-agent/
├── game/            # Tic-Tac-Toe Game engine
├── agents/
├── training/        # Training loop
├── evaluation/      # Benchmarking
├── visualization/   # Plots and demos
├── scripts/         # CLI entry points
└── models/          # Saved models
```

## Baseline Results

### RandomAgent vs RandomAgent

20,000 Episodes — runtime ~3 seconds:

| Result | Games | Rate |
|---|---|---|
| X wins | 11546 | 57.73% |
| O wins | 5919 | 29.59% |
| Draws | 2535 | 12.67% |

Both players use the same uniformly random policy; X moves first

