# Two way anti-cheat system for zarckary game. 
# The watcher process monitors the game process and resets the player's account if the game process is not updating its tick file. 
# The game process updates its tick file every second and checks if the watcher process is alive. 
# If the watcher process is not alive, the game process will exit. 
# This way, if the player tries to cheat by pausing the game or killing the watcher process, their account will be reset. 
# The player can restore their account using a save key that is generated when their account is reset. 
# The save key is stored in the player's data and can be used to restore their account if they contact the creator of the game.

import os
import json
import time
import sys
import inspect
import copy

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
JSON_ENCODED = True
ATTRDICT_TEMPLATE = {"death": {}, "barn": False, "attr": [], "searched_ditch": {"-5,-9": False, "-4,-9": False, "-4,-8": False, "-3,-8": False, "-3,-7": False, "-2,-7": False, "-2,-6": False, "-1,-6": False, "-1,-5": False, "-1,-4": False, "0,-3": False, "0,-2": False, "0,-1": False, "0,0": False, "0,1": False, "0,2": False, "0,3": False, "0,4": False, "1,4": False, "1,5": False, "1,6": False, "2,6": False, "2,7": False, "2,9": False}, "searched": [], "water_sources": []}
PLAYER_STATS_TEMPLATE = {"health": 100, "hunger": 100, "thirst": 100, "attack": 15, "strength": 15, "defense": 10, "start_time": 0, "play_time": 0, "xp": {"total": 0}}


def build_default_player_attrdict(password_value=""):
    state = copy.deepcopy(ATTRDICT_TEMPLATE)
    state.update({
        "password": password_value,
        "x": 0,
        "y": 0,
        "items": copy.deepcopy(base_items),
        "achieved": [],
        "turns": -1,
        "trespass": 0,
        "player_stats": copy.deepcopy(PLAYER_STATS_TEMPLATE),
        "lastxy": "0,0",
        "wilhelm_pixy_fairy": False,
        "barnx": 0,
        "barny": 0,
    })
    return state


def normalize_player_record(record):
    player_record = record if isinstance(record, dict) else {}
    player_attrdict = build_default_player_attrdict()

    nested_attrdict = player_record.get("attrdict")
    if isinstance(nested_attrdict, dict):
        player_attrdict.update(copy.deepcopy(nested_attrdict))

    for field, value in player_record.items():
        if field == "attrdict":
            continue
        player_attrdict[field] = copy.deepcopy(value)

    return {"attrdict": player_attrdict}


def normalize_save_data(raw_data):
    if not isinstance(raw_data, dict):
        return {}
    return {player_name: normalize_player_record(player_record) for player_name, player_record in raw_data.items()}


def get_player_attrdict(player_data, player_name):
    return player_data[player_name]["attrdict"]


def load_player_data():
    try:
        with open(PLAYER_FILE, "r") as f:
            raw = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

    if isinstance(raw, dict):
        return normalize_save_data(raw)

    if not JSON_ENCODED:
        return {}

    try:
        data = Zcryptv1.ceasar_self_decode(raw, 10, "zarck", True)
        data = Zcryptv1.base64_decode1(data, True)
        return normalize_save_data(data)
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
        
        player_attrdict = get_player_attrdict(playerdata, username)

        if "admin" in player_attrdict["attr"]:
            print(f"Error line() {line()}: As an admin you have been spared from the punishment of having your account reset. If you read this message, a problem with the watcher/game connection has occurred. Please report this to the creator of the game so it can be fixed. Thank you!")
            os._exit(0)

        print(f"Error line() {line()}: Game terminated without reason. Resetting account.")
        
        # reset acount
        player_attrdict["x"] = 0
        player_attrdict["y"] = 0
        player_attrdict["items"] = copy.deepcopy(base_items)
        player_attrdict["lastxy"] = "0,0"
        player_attrdict["wilhelm_pixy_fairy"] = False
        player_attrdict["barnx"] = 0
        player_attrdict["barny"] = 0
        player_attrdict.setdefault("player_stats", copy.deepcopy(PLAYER_STATS_TEMPLATE))
        player_attrdict["player_stats"]["health"] = 100
        player_attrdict["player_stats"]["attack"] = 15
        player_attrdict["player_stats"]["strength"] = 15
        player_attrdict["player_stats"]["defense"] = 10
        player_attrdict["player_stats"]["thirst"] = 100
        player_attrdict["player_stats"]["hunger"] = 100
        player_attrdict.setdefault("attr", [])
        if "reset2" not in player_attrdict["attr"]:
            player_attrdict["attr"].append("reset2")
        dump_player_data(playerdata)
        os._exit(0)
    
    # update last
    last = current

    time.sleep(1)
