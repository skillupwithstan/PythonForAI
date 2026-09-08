import random

random.seed(42)

# --- 1. The Environment ---
# States: "Hot" or "Cold"
# Actions: 0 = Turn OFF, 1 = Turn ON
q_table = {
    "Hot": [0.0, 0.0],   # [Score for OFF, Score for ON]
    "Cold": [0.0, 0.0]   # [Score for OFF, Score for ON]
}

learning_rate = 0.5

# --- 2. Training Loop (Trial and Error) ---
for episode in range(20):  # Simulate 20 days
    # Pick a random weather state
    state = random.choice(["Hot", "Cold"])
    
    # The agent chooses a random action to explore
    action = random.choice([0, 1]) 
    
    # Determine the reward
    if state == "Hot" and action == 1:   # Correct choice
        reward = 10
    elif state == "Cold" and action == 0: # Correct choice
        reward = 10
    else:                                 # Wrong choice (wasting energy or uncomfortable)
        reward = -10
        
    # Update the score in memory
    old_score = q_table[state][action]
    q_table[state][action] = old_score + learning_rate * (reward - old_score)

# --- 3. The Result ---
print("Final Learned Scores (Higher is better):")
print(f"When HOT -> OFF score: {q_table['Hot'][0]:.1f} | ON score: {q_table['Hot'][1]:.1f}")
print(f"When COLD -> OFF score: {q_table['Cold'][0]:.1f} | ON score: {q_table['Cold'][1]:.1f}")
