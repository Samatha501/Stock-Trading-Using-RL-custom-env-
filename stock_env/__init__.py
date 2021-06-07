from gym.envs.registration import register


register(
    id='stock1-v0',
    entry_point='stock_env.envs:StockEnv'

)
