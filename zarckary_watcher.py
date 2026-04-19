import os
import json
import time
import sys
import random
import inspect

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import Zcryptv1



# Use the inherited working directory from the game process so both
# processes share the same tick/save files.
BASE_DIR = os.getcwd()

W_TICK_FILE = os.path.join(BASE_DIR, "wtick.json")
G_TICK_FILE = os.path.join(BASE_DIR, "gtick.json")
PLAYER_FILE = os.path.join(BASE_DIR, "zark.json")
SAFE_GUARD = 3
last = 0
current = 0
gtick = {"tick": 0,"exit": False}
wtick = 0
base_items = {"weapons_and_items":{"stars":{"owned":0,"damage":20,"chance":0.6545},"za'roc":{"owned":0},"axe":{"owned":0},"shovel":{"owned":0},"pickaxe_bad":{"owned":0},"pickaxe_good":{"owned":0},"pickaxe_perfect":{"owned":0},"rope":{"owned":0},"matches":{"owned":0},"lantern":{"owned":0,"on":False},"kerosene":{"owned":0},"mine_map":{"owned":0,"started":False},"letter":{"owned":0},"stick":{"owned":0}},   "food":{"starter_food":{"owned":0},"bread":{"owned":0}},   "water":{"0.5l_full_bottle":{"owned":0},"1l_full_bottle":{"owned":0},"2l_full_bottle":{"owned":0},"5l_full_bottle":{"owned":0},"0.5l_empty_bottle":{"owned":0},"1l_empty_bottle":{"owned":0},"2l_empty_bottle":{"owned":0},"5l_empty_bottle":{"owned":0}}}
save_key = "save_key_"
key_len = 30
JSON_ENCODED = True


def load_player_data():
    try:
        with open(PLAYER_FILE, "r") as f:
            raw = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

    if isinstance(raw, dict):
        return raw

    if not JSON_ENCODED:
        return {}

    try:
        data = Zcryptv1.ceasar_self_decode(raw, 10, "zarck", True)
        data = Zcryptv1.base64_decode1(data, True)
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def dump_player_data(data):
    if not JSON_ENCODED:
        with open(PLAYER_FILE, "w") as f:
            json.dump(data, f)
        return

    encoded = Zcryptv1.base64_encode1(data, True)
    encoded = Zcryptv1.ceasar_self_encode(encoded, 10, "zarck", True)
    with open(PLAYER_FILE, "w") as f:
        json.dump(encoded, f)

def line():
    frame = inspect.currentframe().f_back  # go one frame back
    return frame.f_lineno



if len (sys.argv) < 2:
    print(f"Error line: {line()}: No username provided.")
    os._exit(0)

username = sys.argv[1]
if len(sys.argv) >= 3:
    JSON_ENCODED = str(sys.argv[2]).strip().lower() in ("1", "true", "yes", "y", "on")

s = SAFE_GUARD

while True:
    # update watcher alive
    wtick += 1
    with open(W_TICK_FILE,"w") as f:
        json.dump(wtick,f)
    
    # get updated game tick
    try:
        with open(G_TICK_FILE,"r") as f:
            gtick = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        gtick = {"tick": 0,"exit": False}
    
    if gtick["exit"] == True:
        print("Game exited properly.")
        os._exit(0)

    # check if game alive
    current = gtick ["tick"]
    if current == last:
        s -= 1
    else:
        s = SAFE_GUARD
    if s < 1:
        playerdata = load_player_data()
        if not playerdata:
            print(f"Error line() {line()}: Player file not found.")
            os._exit(0)

        if username not in playerdata:
            print(f"Error line() {line()}: Username not found in player data.")
            os._exit(0)
        
        if "admin" in playerdata[username]["attrdict"]["attr"]:
            print(f"Error line() {line()}: As an admin you have been spared from the punishment of having your account reset. If you read this message, a problem with the watcher/game connection has occurred. Please report this to the creator of the game so it can be fixed. Thank you!")
            os._exit(0)

        for f in range(key_len):
            save_key += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")


        # save acount if watcher terminates game without reason
        if "save_key" not in playerdata[username]:
            print(f"Error line() {line()}: Game terminated without reason. Use the following save key to restore your account: {save_key}")
            playerdata[username]["save_key"] = {"key":save_key,"data":playerdata[username].copy()}
        else:
            yn = input(f"Error line() {line()}: Game terminated without reason. Do you want to overwrite your previous save? (y/n): ")
            if yn.lower() == "y":
                print(f"Use the following save key to restore your account: {save_key}")
                playerdata[username]["save_key"] = {"key":save_key,"data":playerdata[username].copy()}
            else:
                print(f"Previous save key: {playerdata[username]['save_key']['key']}")
                print(f"Use the previous save key to restore your account.")
        
        # reset acount
        playerdata[username]["x"] = 0
        playerdata[username]["y"] = 0
        playerdata[username]["items"] = base_items
        playerdata[username]["lastxy"] = "0,0"
        playerdata[username]["player_stats"]["health"] = 100
        playerdata[username]["player_stats"]["attack"] = 15
        playerdata[username]["player_stats"]["strength"] = 15
        playerdata[username]["player_stats"]["defense"] = 10
        playerdata[username]["attrdict"]["attr"].append("reset2")
        dump_player_data(playerdata)
        os._exit(0)
    
    # update last
    last = current

    time.sleep(1)