import json
import base64
import random


def ceasar_self_encode(data, exponent, pas, flag):
    if flag == True:
        char = ""
        base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=()!#$%&?`*@^¨-_:.;,§'<>•Ωé†µüıœπ˙ß∂ƒ¸˛√ªﬁöä≈ç‹›‘’©™£€∞§|[]≈±{}"
        # Ensure the alphabet is reversible (no duplicate symbols).
        base64_chars = "".join(dict.fromkeys(base64_chars))
        try:
            key = json_load()
        except Exception:
            key = {}
        if not isinstance(key, dict):
            key = {}

        if pas in key and isinstance(key[pas], list) and len(set(key[pas])) == len(key[pas]) and len(key[pas]) == len(base64_chars):
            chars = key[pas]
        else:
            chars = randomize(base64_chars,"list")
            key[pas] = chars
            json_dump(key)

        for f in data:
           i = chars.index(f)
           i = (i + exponent) % len(chars)
           char += chars[i]
        return char
    return data

def ceasar_self_decode(data, exponent,pas,flag):
    if flag == True:
        char = ""

        key = json_load()
        if isinstance(key, dict):
            chars = key[pas]
        else:
            # backward compatibility for old zkey.json that stored only a list
            chars = key

        for f in data:
            i = chars.index(f)
            i = (i - exponent) % len(chars)
            char += chars[i]
        return char
    return data


def base64_encode1(data,flag):
    if flag == True:
        json_str = json.dumps(data)                   # dict → JSON string
        b64_str = base64.b64encode(json_str.encode()).decode()  # JSON → base64 string
        return b64_str
    return data

def base64_decode1(data,flag):
    if flag == True:
        data = str(data)
        json_str = base64.b64decode(data.encode()).decode() # decode base64
        data = json.loads(json_str)                  # parse JSON → dict
        return(data)
    return data

def randomize(data,type:str):
    data = str(data)
    output = ""
    while data:
        i = random.randint(0,len(data)-1)
        output += data[i]
        data = data[:i] + data[i+1:]
    
    if type == "list":
        output1 = []
        for f in output:
            output1.append(f)
    elif type == "str":
        output1 = output
    elif type[0:4] == "str:":
        i = type[4:]
        output1 = i.join(output)
    elif type == "tuple":
        output1 = tuple(output)
    return output1

def json_dump(data):
    filename = "zkey.json"
    data = base64_encode1(data,True)
    with open(filename, "w") as f:
        json.dump(data, f)

def json_load():
    filename = "zkey.json"
    with open(filename, "r") as f:
        data = json.load(f)   
    datas = base64_decode1(data,True)
    return datas

