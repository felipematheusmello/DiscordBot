from environs import Env

env = Env()
env.read_env()

TOKEN = env("DISCORD_TOKEN")