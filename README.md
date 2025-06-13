# Coin Toss Distribution Visualization

This project demonstrates the Law of Large Numbers through an simulation of coin tosses. It shows how the distribution of heads and tails approaches a 50-50 split as the number of trials increases.

## What This Project Shows

The simulation creates two visualizations:
1. A pie chart showing the current distribution of heads and tails
2. A line plot showing how the percentages evolve over time

As you run the simulation, you'll observe:
- Initial fluctuations in the distribution
- Gradual convergence towards 50% for both heads and tails
- The effect of increasing the number of trials on the stability of the distribution

## Mathematical Concept: Law of Large Numbers

The Law of Large Numbers states that as the number of trials increases, the average of the results becomes closer to the expected value. In this case:
- Expected probability of heads = 50%
- Expected probability of tails = 50%

With a small number of trials (e.g., 10), you might see significant deviations from 50-50. However, as the number of trials increases (e.g., 200), the distribution becomes more stable and approaches the theoretical 50-50 split.


## How to Run

1. Install the required packages:
```bash
pip install -r requirements.txt
```

2. Run the simulation:
```bash
python coinFlipSimulation.py
```

The visualization updates in real-time, allowing you to observe how the distribution changes with each addition of trial. 
