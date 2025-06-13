import numpy as np
import matplotlib.pyplot as plt 
import random

sides = ['heads', 'tails']
count = [0, 0]
colors = ['r', 'b']
num_trials = 200  # Number of trials

# Lists to store history of percentages
heads_percentages = []
tails_percentages = []
trials = []

# Create figure with two subplots
plt.figure(figsize=(12, 5))
plt.ion()  

for i in range(num_trials):
    count[random.randint(0, 1)] += 1
    total = sum(count)
    
    # Calculate and store percentages
    heads_pct = count[0]/total * 100
    tails_pct = count[1]/total * 100
    heads_percentages.append(heads_pct)
    tails_percentages.append(tails_pct)
    trials.append(i + 1)

    plt.clf()
    
    # Create two subplots
    plt.subplot(1, 2, 1)
    plt.pie(count, colors=colors, labels=['', ''])
    percentages = [f'{side}: {count[i]/total*100:.2f}%' for i, side in enumerate(sides)]
    plt.legend(percentages, title='Current Distribution', loc='center left', bbox_to_anchor=(1, 0.5))
    plt.title(f'Distribution after {i+1} trials')
    
    # Plot the evolution of percentages
    plt.subplot(1, 2, 2)
    plt.plot(trials, heads_percentages, 'r-', label='Heads %')
    plt.plot(trials, tails_percentages, 'b-', label='Tails %')
    plt.axhline(y=50, color='g', linestyle='--', label='50% line')
    plt.xlabel('Number of Trials')
    plt.ylabel('Percentage')
    plt.title('Evolution of Distribution')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.pause(0.001)

plt.ioff()  
plt.show()