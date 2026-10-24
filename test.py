import gymnasium as gym

env = gym.make("CartPole-v1", render_mode="rgb_array")
obs, info = env.reset()

for _ in range(4):
    action = env.action_space.sample()  # random actions
    obs, reward, terminated, truncated, info = env.step(action)

    print(obs)
    
    if terminated or truncated:
        obs, info = env.reset()

env.close()