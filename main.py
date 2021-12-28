import os
import ast

from dotenv import load_dotenv


load_dotenv()

env = ast.literal_eval(os.environ["DICT_ENV"])

print(type(env))

print(env)
