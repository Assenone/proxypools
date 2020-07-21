import os
import sys
import json

strs = str(os.getcwd())#获取路径

def get_config(file_path, args):
    complete_path = strs + file_path
    with open(complete_path, "r") as f:
        text = f.read()
    js = json.loads(text)
    got = js.get(args)
    return got
