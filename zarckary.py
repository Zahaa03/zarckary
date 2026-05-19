# main game file

print("hello world")

import json
import os
import Zcryptv1
import time
import random 
import sys
import subprocess
from datetime import datetime
import threading
import inspect
from threading import Event
import re

HEARTBEAT_FILE = "tick.json"

global typespeed
global lastxy
global trespass
global data
global LETTER
global attrdict


TYPE_SPEED = 0.02
JSON_ENCODED = False
JSON_ENCODED_KEY = "zarckary"


COMMON_SUFFIXES = (
    "ingly", "edly", "iness", "ments", "ment", "ness", "less", "iest",
    "iers", "ier", "ies", "ied", "ing", "ers", "est", "ful", "ly",
    "er", "ed", "es", "s",
)

WORDS = {
    "mean": {
        "words": [
            "hate", "idiotic", "worst", "dumb", "irritating", "annoying", "stupid",
            "rude", "cruel", "nasty", "mean", "awful", "terrible", "useless",
            "hostile", "insulting", "selfish", "bratty", "disrespectful", "hurtful",
            "bitter", "offensive", "rotten", "obnoxious", "unkind",
        ],
        "phrases": [
            "Let's keep the conversation respectful.",
            "That sounded a little harsh.",
            "Please choose kinder words.",
            "Let's try a more respectful tone.",
            "We can say that more nicely.",
            "Kind words work better here.",
            "Please keep it friendly.",
            "That message feels hurtful.",
            "Let's slow down and be respectful.",
            "I'd rather keep this positive.",
            "Let's avoid insulting language.",
            "Please speak with kindness.",
            "That came across as mean.",
            "Let's make this conversation safer.",
            "Try saying that in a calmer way.",
            "Respect goes a long way.",
            "Let's not tear people down.",
            "Please keep the tone polite.",
            "That wording is a bit rough.",
            "Let's aim for kindness instead.",
            "Maybe rephrase that more gently.",
            "Harsh words can hurt people.",
            "Let's be civil with each other.",
            "Friendly language helps more.",
            "Please avoid hurtful comments.",
            "We can disagree without being rude.",
            "Let's keep things thoughtful.",
            "That sounds disrespectful.",
            "Try a kinder response.",
            "Let's reset and speak calmly.",
            "Please keep this welcoming.",
            "That feels unnecessarily mean.",
            "Let's use considerate words.",
            "A gentler tone would help.",
            "Please be mindful of others.",
            "Let's keep the energy positive.",
            "That comment could be kinder.",
            "We can do better than insults.",
            "Please keep the chat respectful.",
            "Let's focus on helpful words.",
            "That was not very kind.",
            "Let's leave out the insults.",
            "Please keep your response polite.",
            "Let's make room for respect.",
            "That tone may upset someone.",
            "Try speaking with more care.",
            "Let's keep things encouraging.",
            "A respectful reply would be better.",
            "Please avoid personal attacks.",
            "Let's keep it kind and calm.",
        ],
    },
    "nice": {
        "words": [
            "kind", "awesome", "best", "smart", "helpful", "amazing", "wonderful",
            "caring", "sweet", "friendly", "polite", "generous", "thoughtful", "lovely",
            "great", "fantastic", "brilliant", "excellent", "supportive", "patient",
            "cheerful", "honest", "warm", "gentle", "respectful","like",
        ],
        "phrases": [
            "That's really kind of you.",
            "I appreciate that positive energy.",
            "That was a thoughtful thing to say.",
            "You're bringing a great vibe.",
            "That message was really uplifting.",
            "Thanks for being so considerate.",
            "That was genuinely sweet.",
            "I love the kindness in that.",
            "That's a wonderful response.",
            "You made that sound very encouraging.",
            "That was nice to hear.",
            "Your words are appreciated.",
            "That was a very supportive comment.",
            "You handled that kindly.",
            "That was full of warmth.",
            "Thanks for saying something positive.",
            "That was really respectful.",
            "You sound very thoughtful.",
            "That kind tone stands out.",
            "You're making this conversation better.",
            "That was a lovely thing to say.",
            "Your kindness is showing.",
            "That felt encouraging.",
            "Thanks for being uplifting.",
            "That was such a good-hearted comment.",
            "You're being very considerate.",
            "That response was full of grace.",
            "You made that sound really positive.",
            "That's the kind of energy I like.",
            "That was friendly and kind.",
            "You're adding something good here.",
            "That sounded generous and warm.",
            "Thanks for keeping it positive.",
            "That was an excellent response.",
            "You said that with a lot of care.",
            "That was beautifully supportive.",
            "I appreciate the kindness in that message.",
            "That was very encouraging.",
            "You're speaking with real respect.",
            "That came across as genuinely nice.",
            "Thank you for the thoughtful words.",
            "That was a bright and cheerful message.",
            "You made that feel welcoming.",
            "That was kind in the best way.",
            "I appreciate your positive tone.",
            "That was a graceful response.",
            "You brought real warmth to the chat.",
            "That message felt supportive.",
            "Thanks for being so uplifting.",
            "That was wonderfully kind.",
        ],
    },
    "funny": {
        "words": [
            "joke", "funny", "hilarious", "laugh", "comedy", "humor", "witty",
            "silly", "goofy", "pun", "giggle", "chuckle", "amusing", "playful",
            "clown", "meme", "prank", "comedian", "banter", "quirky", "ridiculous",
            "snicker", "jest", "gags", "joker","funny-looking",
        ],
        "phrases": [
            "That got a laugh out of me.",
            "Okay, that was funny.",
            "You nailed the joke there.",
            "That had great comedic timing.",
            "That was genuinely hilarious.",
            "I can see the humor in that.",
            "That's a solid joke.",
            "That was a playful comment.",
            "You brought some fun into this.",
            "That was a clever one.",
            "Nice, that was witty.",
            "That joke landed well.",
            "That definitely lightened the mood.",
            "You have good comedic instincts.",
            "That was silly in a good way.",
            "I wasn't expecting that punchline.",
            "That was surprisingly funny.",
            "You slipped humor in nicely.",
            "That's the kind of joke that works.",
            "That made the conversation more fun.",
            "You have a fun sense of humor.",
            "That line was amusing.",
            "That was delightfully goofy.",
            "You turned that into a laugh.",
            "That was comedy gold.",
            "I like the humor in that response.",
            "That was a good bit.",
            "You made that moment entertaining.",
            "That joke had some spark.",
            "That gave the chat some personality.",
            "That was light and funny.",
            "You really played that well.",
            "That was a nice little punchline.",
            "You made that more amusing.",
            "That comment was full of humor.",
            "That was a clever twist.",
            "I like how playful that sounded.",
            "That joke was well placed.",
            "You gave that some real charm.",
            "That was a fun response.",
            "You know how to make it entertaining.",
            "That was unexpectedly witty.",
            "That line had good energy.",
            "You made that pretty memorable.",
            "That was laugh-worthy.",
            "You delivered a strong joke there.",
            "That had a good sense of fun.",
            "You turned that into a funny moment.",
            "That was nicely comedic.",
            "That one definitely worked.",
        ],
    },
    "sad": {
        "words": [
            "sad", "unhappy", "depressed", "cry", "tears", "lonely", "heartbroken",
            "upset", "miserable", "gloomy", "down", "sorrow", "grief", "hopeless",
            "tired", "hurt", "abandoned", "blue", "crushed", "defeated",
            "disappointed", "stressed", "anxious", "withdrawn", "broken",
        ],
        "phrases": [
            "I'm here with you.",
            "That sounds really heavy.",
            "I'm sorry you're feeling this way.",
            "You don't have to carry that alone.",
            "It's okay to have hard days.",
            "That sounds painful.",
            "I hope things ease up soon.",
            "Please be gentle with yourself.",
            "What you're feeling matters.",
            "You deserve support.",
            "I'm sorry that hurts.",
            "It's okay to pause and breathe.",
            "That sounds exhausting.",
            "You are not alone in this.",
            "Take things one step at a time.",
            "I hope you get some comfort today.",
            "Your feelings are valid.",
            "It's understandable to feel low sometimes.",
            "I'm sorry things feel rough right now.",
            "You matter, even on difficult days.",
            "Please give yourself some care.",
            "That sounds deeply disappointing.",
            "It's okay to reach out for help.",
            "I hope tomorrow feels lighter.",
            "You deserve kindness right now.",
            "That sounds really lonely.",
            "I'm sorry you're dealing with that.",
            "Take your time getting through this.",
            "You don't need to rush feeling better.",
            "I hope you can rest a little.",
            "Even small steps count.",
            "It makes sense that you're hurting.",
            "Please remember to be patient with yourself.",
            "Hard moments can take time.",
            "I hear the sadness in that.",
            "You deserve compassion.",
            "I hope something good reaches you today.",
            "You're allowed to feel what you feel.",
            "That sounds really discouraging.",
            "I'm sorry this has been so hard.",
            "Please take care of yourself.",
            "I hope you find a little peace soon.",
            "It's okay to lean on support.",
            "This sounds like a tough moment.",
            "You're still important through all of this.",
            "I hope things soften with time.",
            "That kind of hurt can be a lot.",
            "You deserve understanding.",
            "Please keep going one moment at a time.",
            "I'm sending a little encouragement your way.",
        ],
    },
    "angry": {
        "words": [
            "angry", "mad", "furious", "rage", "irritated", "annoyed", "upset",
            "bitter", "heated", "frustrated", "resentful", "hostile", "aggressive",
            "grumpy", "offended", "outraged", "livid", "cross", "stormy", "fuming",
            "tense", "snappy", "sharp", "cranky", "seething",
        ],
        "phrases": [
            "Let's take a breath first.",
            "That sounds really frustrating.",
            "I can tell you're upset.",
            "Let's slow the moment down.",
            "A calmer tone might help here.",
            "Try taking a pause before replying.",
            "That sounds heated.",
            "Let's keep this steady.",
            "You seem really frustrated right now.",
            "It may help to step back for a second.",
            "Let's not let this escalate.",
            "Try a deep breath and a reset.",
            "That sounds intense.",
            "Let's work through it calmly.",
            "It's okay to be upset, but let's stay respectful.",
            "Maybe take a short pause.",
            "That feels like a strong reaction.",
            "Let's bring the temperature down.",
            "Try putting that a little more calmly.",
            "Let's keep the response measured.",
            "You sound really annoyed.",
            "A little distance might help.",
            "Let's slow things down before continuing.",
            "That sounds like a frustrating situation.",
            "Let's stay in control of the tone.",
            "It might help to respond after a pause.",
            "That's a lot of anger at once.",
            "Let's aim for calm words.",
            "You can be honest without exploding.",
            "Try to keep it grounded.",
            "That frustration is coming through clearly.",
            "Let's turn that into a calmer response.",
            "A quieter approach may work better.",
            "Let's not add more heat to this.",
            "Take a second and reset.",
            "That sounds really aggravating.",
            "Let's keep things constructive.",
            "You sound close to boiling over.",
            "A calm reply might help more.",
            "Let's keep this from becoming harsher.",
            "You can say that with less force.",
            "That message feels tense.",
            "Let's make space for a calmer answer.",
            "Try easing the tone a little.",
            "That seems like a high-stress moment.",
            "Let's aim for control instead of reaction.",
            "It may help to cool off first.",
            "That irritation is understandable.",
            "Let's keep your next words deliberate.",
            "Pause, breathe, then answer.",
        ],
    },
}

ENEMY_SPAWN_CHANCE = {
    "fields": [250.5,3000.5],
    "plains": [2000.5,10000.5],
    "forest": [400.5,4000.5],
    "rocky_area": [750.5,6000.5],
    "dense_forest": [700.5,6500.5],
    "valley_and_hills": [1000.5,8000.5],
    "road": [1200.5,9000.5],
}

RANDOM_FEEDBACK = [
  "Sorry, I don't understand. Could you repeat that?",
  "What did you say?",
  "I don't understand you.",
  "Could you say that again?",
  "I didn't catch that—can you repeat it?",
  "I'm not sure I understood. Can you rephrase?",
  "Can you repeat that, please?",
  "I didn't understand that. Could you reword it?",
  "Sorry, could you clarify what you mean?",
  "I'm confused—could you explain that differently?",
  "That didn't make sense to me. Can you rephrase?",
  "I'm not following. Could you try saying it another way?",
  "Could you restate that?",
  "Please rephrase that for me.",
  "Can you say that in a different way?",
  "I didn't quite get it. Can you clarify?",
  "I'm not sure what you mean. Could you elaborate?",
  "Sorry, I missed that. Can you repeat?",
  "Could you try again? I didn't understand.",
  "I'm having trouble understanding—can you rephrase?",
  "I'm not sure I heard you correctly. Can you repeat?",
  "I don't get it. Could you say that differently?",
  "Sorry, can you say that again more clearly?",
  "Can you repeat what you just said?",
  "I'm not understanding. Can you rephrase your question?",
  "Could you clarify your request?",
  "Sorry—what do you mean by that?",
  "I'm not sure what you're asking. Can you rephrase?",
  "I didn't understand your message. Can you try again?",
  "Could you say that again in simpler terms?",
  "I'm not sure I follow. Can you restate it?",
  "That's unclear to me. Could you clarify?",
  "I'm not certain what you mean. Can you explain?",
  "I didn't catch your meaning. Could you rephrase?",
  "Sorry, I'm not following you. Can you try again?",
  "Can you clarify that a bit?",
  "I'm not sure I understand what you're saying.",
  "I don't understand—could you explain it another way?",
  "Could you repeat the last part?",
  "I didn't understand that statement. Can you rephrase?",
  "Sorry, I'm lost. Could you restate your point?",
  "I'm not sure what that means. Can you clarify?",
  "Can you reword that for me?",
  "I didn't get that. Could you repeat it, please?",
  "Sorry, could you say that again?",
  "I'm not sure I understood correctly. Could you rephrase?",
  "I don't quite understand. Can you clarify?",
  "Could you repeat your question?",
  "I'm not following—could you rephrase?",
  "That wasn't clear to me. Can you reword it?",
  "I'm having difficulty understanding. Can you try again?",
  "Sorry, I don't understand what you mean.",
  "Can you say that again with more detail?",
  "I didn't understand. Could you explain more clearly?",
  "Could you rephrase that in a simpler way?",
  "I'm not sure what you're trying to say. Can you rephrase?",
  "Sorry, I didn't get your request. Can you repeat it?",
  "I don't understand that. Could you clarify your intent?",
  "Can you rephrase your message for clarity?",
  "I'm confused. Could you restate that?",
  "I'm not sure I understand your question.",
  "Sorry, what was that?",
  "I didn't catch that. Can you say it again?",
  "I'm not sure what you mean—could you clarify?",
  "I don't understand. Can you rephrase it differently?",
  "Can you repeat that more slowly?",
  "I'm not following your meaning. Can you reword it?",
  "I didn't understand the last message. Can you try again?",
  "Sorry, could you clarify your question?",
  "I'm not sure I understood—can you restate it?",
  "I didn't get what you meant. Can you clarify?",
  "Could you explain that again?",
  "I'm not sure what you said. Can you repeat?",
  "I don't understand. Can you provide more context?",
  "Sorry, I'm not understanding this. Can you rephrase?",
  "I didn't follow that. Can you reword it?",
  "I'm not sure what you're referring to. Can you clarify?",
  "Could you restate your request more clearly?",
  "I'm confused by that. Could you explain it differently?",
  "I don't understand your last message. Can you rephrase?",
  "Sorry, could you try phrasing that another way?",
  "I didn't understand. Can you say it again?",
  "I'm not following. Can you repeat your request?",
  "That's not clear to me. Can you clarify what you mean?",
  "I'm not sure what you're asking for. Can you restate it?",
  "Could you rephrase that question?",
  "I'm not understanding. Could you elaborate a little?",
  "Sorry, I didn't understand that. Could you clarify?",
  "I'm not sure how to interpret that. Can you rephrase?",
  "I didn't catch your point. Can you restate it?",
  "Sorry, can you clarify what you want?",
  "I'm not sure I understand the request. Can you rephrase?",
  "I don't get it—could you reword your message?",
  "Could you say that again using different words?",
  "I'm not sure what you mean. Can you be more specific?",
  "I didn't understand that. Could you provide an example?",
  "Sorry, I'm not following. Could you clarify your message?",
  "I don't understand. Can you restate it with more detail?",
  "I'm not sure what you meant. Can you rephrase that?",
  "Could you clarify what you're trying to do?",
  "I'm confused—can you repeat your question?",
  "I didn't quite understand that. Can you reword it?",
  "Sorry, could you clarify what you're saying?",
  "I'm not sure I understood. Can you rephrase your sentence?",
  "I don't understand. Could you explain your point again?",
  "Can you say that again in plain language?",
  "I didn't catch that. Can you repeat the question?",
  "Sorry, I didn't understand. Can you try again?",
  "I'm not following. Could you restate your question?",
  "That doesn't make sense to me. Can you clarify?",
  "I'm not sure what you mean. Could you reword that?",
  "I don't understand what you're asking. Can you rephrase?",
  "Could you repeat that with a bit more clarity?",
  "I didn't get that. Can you clarify your meaning?",
  "Sorry, I'm still not understanding. Can you rephrase?",
  "I'm not sure what you're saying. Can you restate it?",
  "I don't understand. Could you please rephrase?",
  "Could you clarify your last message?",
  "I'm confused about that. Can you explain it differently?",
  "I'm not sure I understand. Can you reword your request?",
  "I didn't understand that. Can you repeat it more clearly?",
  "Sorry, that's unclear. Can you rephrase?",
  "I'm not following your question. Can you restate it?",
  "I don't get it. Could you clarify what you mean?",
  "Could you rephrase that so I can understand?",
  "I'm not sure I understood the last part. Can you repeat it?",
  "I didn't catch what you meant. Can you clarify?",
  "Sorry, I'm not sure I understand your meaning.",
  "I don't understand. Can you say it another way?",
  "Could you clarify that request?",
  "I'm confused—can you explain it in a different way?",
  "I didn't understand that. Could you simplify it?",
  "Sorry, I'm not sure what you mean by that.",
  "I'm not following—could you clarify what you're asking?",
  "I don't understand. Can you repeat with more details?",
  "Could you restate what you want me to do?",
  "I'm not sure what you're trying to say. Can you clarify?",
  "I didn't get your point. Can you rephrase it?",
  "Sorry, I didn't understand your question. Can you reword it?",
  "I'm not sure I can interpret that. Can you clarify?",
  "That's unclear. Could you please rephrase?",
  "I don't understand—could you restate your message?",
  "Sorry, can you clarify what you're asking me?",
  "I'm not sure I understood. Could you repeat it?",
  "I didn't catch that. Could you rephrase it?",
  "I'm not understanding this. Can you explain it another way?",
  "I don't get it. Can you reword that?",
  "Could you clarify what you mean here?",
  "I'm confused. Can you rephrase the question?",
  "I didn't understand your intent. Can you clarify?",
  "Sorry, I'm not sure I understand. Can you elaborate?",
  "I'm not following. Can you explain with different wording?",
  "I don't understand. Could you give me more context?",
  "Could you restate your question more simply?",
  "I'm not sure what you mean. Can you clarify the details?",
  "I didn't quite get that. Can you say it again?",
  "Sorry, can you rephrase your message?",
  "I'm not sure I understood what you said. Can you repeat it?",
  "I don't understand that. Can you clarify what you mean?",
  "Could you reword that sentence?",
  "I'm confused by your message. Can you restate it?",
  "I didn't understand your last question. Can you rephrase?",
  "Sorry, could you repeat that more clearly?",
  "I'm not sure what you meant. Could you clarify it?",
  "I don't understand. Can you restate what you're asking?",
  "Could you clarify your request for me?",
  "I'm not following your explanation. Can you rephrase?",
  "I didn't understand that. Could you try again with different words?",
  "Sorry, I'm not sure what you're saying. Can you clarify?",
  "I'm not understanding your question. Can you restate it?",
  "I don't get it. Can you explain it differently?",
  "Could you clarify what you want exactly?",
  "I'm confused—could you reword your request?",
  "I didn't understand. Could you say that again, please?",
  "Sorry, I'm not following. Can you repeat what you said?",
  "I'm not sure I understand. Could you clarify your meaning?",
  "I don't understand. Can you rephrase your question more clearly?",
  "Could you repeat that, but in different words?",
  "I'm not sure what you're asking. Can you clarify the question?",
  "I didn't catch that. Can you rephrase the last message?",
  "Sorry, I didn't understand your statement. Can you reword it?",
  "I'm confused. Can you clarify what you mean?",
  "I don't understand. Can you restate that in another way?",
  "Could you clarify your last point?",
  "I'm not sure I understood. Can you rephrase what you said?",
  "I didn't get that. Could you explain it again?",
  "Sorry, I'm not understanding. Can you clarify the request?",
  "I'm not following. Could you say that again differently?",
  "I don't understand your question. Could you restate it?",
  "Could you clarify what you're trying to ask?",
  "I'm confused—can you repeat your message?",
  "I didn't understand that. Can you explain it in simpler terms?",
  "Sorry, I'm not sure I understand. Could you rephrase your question?",
  "I'm not following what you mean. Can you clarify it?",
  "I don't get it. Could you clarify your message?",
  "Could you reword that to make it clearer?",
  "I'm not sure what you mean. Could you explain it again?",
  "I didn't catch your question. Can you repeat it?",
  "Sorry, I didn't understand. Can you clarify what you said?",
  "I'm confused by that. Can you rephrase the statement?",
  "I don't understand. Could you restate your request?",
  "Could you clarify what you mean by that?",
  "I'm not sure I follow. Can you rephrase your question?",
  "I didn't understand your message. Could you clarify it?",
  "Sorry, I'm not following. Can you explain it again?",
  "I'm not sure what you're asking. Could you reword it?",
  "I don't get it. Can you repeat that?",
  "Could you clarify the question for me?",
  "I'm confused. Can you restate it in other words?",
  "I didn't understand. Can you provide more detail?",
  "Sorry, I'm not sure what you mean. Can you clarify?",
  "I'm not following. Can you restate your request more clearly?",
  "I don't understand that. Could you rephrase your sentence?",
  "Could you say that again, but more clearly?",
  "I'm not sure I got it. Can you clarify what you mean?",
  "I didn't understand. Could you explain what you mean?",
  "Sorry, I'm confused. Can you reword your message?",
  "I'm not sure I understand. Can you restate the question?",
  "I don't understand. Could you repeat your last message?",
  "Could you clarify what you're referring to?",
  "I'm confused—could you explain that again?",
  "I didn't understand that. Can you rephrase your request?",
  "Sorry, I didn't get that. Can you clarify?",
  "I'm not sure what you mean. Can you restate it clearly?",
  "I don't understand. Can you reword the question?",
  "Could you clarify what you want me to answer?",
  "I'm confused. Can you rephrase what you said?",
  "I didn't catch that. Could you repeat it again?",
  "Sorry, can you clarify your meaning?",
  "I'm not following. Could you reword it in simpler terms?",
  "I don't understand. Could you please clarify?",
  "Could you repeat your request, please?",
  "I'm not sure I understand what you mean. Can you restate it?",
  "I didn't understand your question. Can you clarify what you mean?",
  "Sorry, I'm not sure what you're asking. Could you rephrase?",
  "I'm confused by that. Could you restate it?",
  "I don't get what you mean. Can you clarify?",
  "Could you clarify your question a bit more?",
  "I'm not sure I understood. Could you explain with different words?",
  "I didn't catch your meaning. Can you clarify it?",
  "Sorry, I'm not following your request. Can you rephrase?",
  "I'm not sure what you mean. Can you explain it more clearly?",
  "I don't understand. Could you rephrase your last message?",
  "Could you clarify what you're asking me to do?",
  "I'm confused—can you rephrase the question?",
  "I didn't understand that. Could you clarify your point?",
  "Sorry, I'm not sure I understand your message.",
  "I'm not following. Can you repeat your question more clearly?",
  "I don't understand. Can you restate it with more context?",
  "Could you clarify what you mean in your last message?",
  "I'm confused. Can you reword the request?",
  "I didn't catch what you meant. Can you restate it?",
  "Sorry, I don't understand. Can you say it another way?",
  "I'm not sure what you're saying. Could you clarify your question?",
  "I don't understand. Can you repeat it in different words?",
  "Could you clarify the last thing you said?",
  "I'm confused—can you explain your question differently?",
  "I didn't understand. Can you clarify what you mean by that statement?",
  "Sorry, I'm not sure I follow. Could you restate it?",
  "I'm not following. Can you clarify your request?",
  "I don't understand. Can you explain in a different way?",
  "Could you rephrase that more clearly?",
  "I'm confused. Could you clarify the details?",
  "I didn't understand your message. Can you repeat it more clearly?",
  "Sorry, could you rephrase that?",
  "I'm not sure what you mean. Can you clarify what you want?",
  "I don't get it. Can you restate your question?",
  "Could you clarify the intent of your message?",
  "I'm confused—can you reword that?",
  "I didn't understand. Could you repeat your request?",
  "Sorry, I'm not following. Can you clarify what you mean?",
  "I'm not sure I understood. Can you explain it another way?",
  "I don't understand. Can you clarify your last request?",
  "Could you restate that question for me?",
  "I'm confused. Could you rephrase that sentence?",
  "I didn't get it. Can you explain what you mean?",
  "Sorry, I'm not sure what you mean. Could you clarify it?",
  "I'm not following. Can you clarify what you're asking?",
  "I don't understand. Could you reword that for clarity?",
  "Could you repeat the message in simpler words?",
  "I'm confused—could you clarify your request?",
  "I didn't understand your question. Could you rephrase it?",
  "Sorry, can you restate what you said?",
  "I'm not sure I understand. Could you clarify your request in detail?",
  "I don't understand. Can you rephrase the question again?",
  "Could you clarify what you're trying to communicate?",
  "I'm confused. Can you reword your question?",
  "I didn't catch that. Could you clarify your meaning?",
  "Sorry, I'm not following. Can you restate your point?",
  "I'm not sure what you mean. Can you clarify what you're asking?",
  "I don't understand. Could you explain more clearly?",
  "Could you rephrase that statement for me?",
  "I'm confused—can you restate it more clearly?",
  "I didn't understand. Could you clarify the question?",
  "Sorry, I'm not sure I understand your request.",
  "I'm not following. Could you clarify what you want to know?",
  "I don't understand. Can you rephrase your question in simpler terms?",
  "Could you restate the last message you sent?",
  "I'm confused. Could you clarify your statement?",
  "I didn't understand that. Can you reword the question?",
  "Sorry, could you explain what you mean by that?",
  "I'm not sure I understand. Could you rephrase what you're asking?",
  "I don't get it. Could you restate your request more clearly?",
  "Could you clarify what you mean, please?",
  "I'm confused—can you rephrase your last message?",
  "I didn't catch that. Can you restate the question?",
  "Sorry, I didn't understand. Could you clarify what you mean?",
  "I'm not sure what you're asking. Can you explain it differently?",
  "I don't understand. Could you restate your question with more detail?",
  "Could you clarify your last message a bit?",
  "I'm confused. Can you reword what you said?",
  "I didn't understand. Could you try explaining it another way?",
  "Sorry, I'm not following. Could you rephrase what you want?",
  "I'm not sure I understand what you're trying to ask.",
  "I don't understand. Can you clarify what you mean exactly?",
  "Could you repeat that in a clearer way?",
  "I'm confused—could you clarify your question?",
  "I didn't get it. Can you rephrase your message?",
  "Sorry, I'm not sure what you mean. Can you restate it?",
  "I'm not following. Could you reword that?",
  "I don't understand. Could you restate it in simpler terms?",
  "Could you clarify the meaning of your message?",
  "I'm confused. Can you repeat your question?",
  "I didn't understand. Could you clarify what you're referring to?",
  "Sorry, could you rephrase your request more clearly?",
  "I'm not sure I understand. Can you clarify your last point?",
  "I don't get what you mean. Can you reword it?",
  "Could you clarify your question, please?",
  "I'm confused—can you explain it another way?",
  "I didn't catch that. Could you rephrase your last message?",
  "Sorry, I didn't understand. Could you repeat the question?",
  "I'm not sure what you mean. Could you clarify your statement?",
  "I don't understand. Can you reword the request for me?",
  "Could you clarify what you're asking in your message?",
  "I'm confused. Could you restate that message?",
  "I didn't understand. Can you clarify what you want me to do?",
  "Sorry, I'm not sure what you mean. Could you explain again?",
  "I'm not following. Can you rephrase your question for me?",
  "I don't get it. Could you clarify your last message?",
  "Could you rephrase that so it's easier to understand?",
  "I'm confused—could you clarify what you're saying?",
  "I didn't understand your question. Can you restate it?",
  "Sorry, can you clarify what you mean in simpler terms?",
  "I'm not sure what you mean. Can you clarify your request?",
  "I don't understand. Could you restate your message in other words?",
  "Could you clarify what you're asking about?",
  "I'm confused. Could you repeat that again?",
  "I didn't catch the meaning. Can you clarify?",
  "Sorry, I'm not following. Can you reword your statement?",
  "I'm not sure I understand. Could you clarify with an example?",
  "I don't understand. Could you rephrase your question one more time?",
  "Could you clarify your intent here?",
  "I'm confused—can you restate your request?",
  "I didn't understand. Can you explain more simply?",
  "Sorry, could you clarify your message again?",
  "I'm not following. Could you rephrase your question in another way?",
  "I don't get what you mean. Could you clarify the request?",
  "Could you clarify what you mean by your last message?",
  "I'm confused. Could you reword that more clearly?",
  "I didn't understand. Can you restate your question differently?",
  "Sorry, I'm not sure what you're asking. Can you clarify it?",
  "I'm not sure I understand. Could you repeat that?",
  "I don't understand. Could you clarify the details of your question?",
  "Could you clarify your message so I can help?",
  "I'm confused—can you explain that again in different words?",
  "I didn't catch that. Could you restate it clearly?",
  "Sorry, I didn't understand. Could you rephrase your request?",
  "I'm not following. Can you clarify what you mean by that?",
  "I don't get it. Could you reword your question for clarity?",
  "Could you clarify what you're trying to say in that message?",
  "I'm confused. Could you clarify what you mean?",
  "I didn't understand your point. Can you rephrase it?",
  "Sorry, I'm not sure I understand. Can you restate it another way?",
  "I'm not following. Could you clarify your last request?",
  "I don't understand. Could you explain it again more clearly?",
  "Could you clarify what you're asking me?",
  "I'm confused—could you rephrase the question in simpler terms?",
  "I didn't understand that. Could you clarify your question again?",
  "Sorry, can you restate your message in other words?",
  "I'm not sure I understand. Can you clarify with more detail?",
  "I don't understand. Could you rephrase what you're saying?",
  "Could you clarify what you mean by that phrase?",
  "I'm confused. Can you restate your question more clearly?",
  "I didn't catch that. Can you clarify what you mean?",
  "Sorry, I didn't understand. Could you reword it?",
  "I'm not following. Could you clarify the question again?",
  "I don't get it. Could you explain what you mean again?",
  "Could you clarify the request in your message?",
  "I'm confused—can you rephrase your statement?",
  "I didn't understand. Can you clarify your question more clearly?",
  "Sorry, I'm not sure what you mean. Could you restate it clearly?",
  "I'm not following. Can you clarify what you're saying?",
  "I don't understand. Could you rephrase your request in a simpler way?",
  "Could you clarify your last question?",
  "I'm confused. Could you clarify what you want me to do?",
  "I didn't understand. Could you restate your request clearly?",
  "Sorry, could you rephrase your question again?",
  "I'm not sure I understand. Can you clarify what you mean by that?",
  "I don't understand. Can you restate it in simpler words?",
  "Could you clarify the question you're asking?",
  "I'm confused—can you repeat that more clearly?",
  "I didn't catch that. Could you clarify what you're asking?",
  "Sorry, I didn't understand. Can you rephrase your message more clearly?",
  "I'm not following. Could you restate it with more clarity?",
  "I don't get it. Can you clarify your intent?",
  "Could you clarify what you mean in this context?",
  "I'm confused. Can you rephrase your question one more time?",
  "I didn't understand. Could you clarify the meaning?",
  "Sorry, I'm not sure I understand your request. Can you rephrase?",
  "I'm not following. Could you clarify your message again?",
  "I don't understand. Could you explain again using different words?",
  "Could you clarify what you mean by your question?",
  "I'm confused—could you restate that more simply?",
  "I didn't understand. Can you rephrase what you're asking?",
  "Sorry, can you clarify what you meant by that?",
  "I'm not sure I understand. Could you clarify the last message?",
  "I don't understand. Can you restate what you want?",
  "Could you clarify what you're requesting?",
  "I'm confused. Could you reword your last message?",
  "I didn't catch that. Can you explain it differently?",
  "Sorry, I didn't understand your request. Could you clarify?",
  "I'm not following. Could you restate your question more directly?",
  "I don't get it. Could you clarify what you mean by that?",
  "Could you clarify what you're saying, please?",
  "I'm confused—can you rephrase that again?",
  "I didn't understand. Can you clarify what you mean in your message?",
  "Sorry, I'm not sure I understand. Could you explain it again?",
  "I'm not following. Could you rephrase that more clearly?",
  "I don't understand. Could you clarify what you meant?",
  "Could you clarify your request so I can respond?",
  "I'm confused. Can you restate your message clearly?",
  "I didn't catch that. Could you clarify your question?",
  "Sorry, I didn't understand. Can you restate it?",
  "I'm not sure I understand. Could you rephrase the last part?",
  "I don't get it. Could you clarify your question for me?",
  "Could you clarify the message you sent?",
  "I'm confused—can you reword what you said?",
  "I didn't understand that. Could you clarify your request one more time?",
  "Sorry, I'm not sure what you're asking. Can you restate it?",
  "I'm not following. Could you clarify your meaning more clearly?",
  "I don't understand. Can you rephrase your question differently?",
  "Could you clarify what you mean by that request?",
  "I'm confused. Could you restate it more clearly?",
  "I didn't catch the point. Can you clarify it?",
  "Sorry, I didn't understand. Could you reword the question?",
  "I'm not sure I understand. Can you clarify what you're asking for?",
  "I don't understand. Could you clarify your last message in more detail?",
  "Could you clarify what you mean in plain terms?",
  "I'm confused—could you rephrase that question?",
  "I didn't understand. Can you restate what you mean?",
  "Sorry, can you clarify what you're requesting?",
  "I'm not following. Can you rephrase your question again?",
  "I don't get it. Could you clarify what you're asking about?",
  "Could you clarify the last statement you made?",
  "I'm confused. Could you reword it with more context?",
  "I didn't understand. Could you explain again more simply?",
  "Sorry, I'm not sure I understand. Could you restate the question?",
  "I'm not following. Could you clarify what you're saying in that message?",
  "I don't understand. Can you rephrase your request with more clarity?",
  "Could you clarify what you mean by that line?",
  "I'm confused—can you repeat your question in other words?",
  "I didn't catch that. Could you clarify your intent again?",
  "Sorry, I didn't understand. Could you restate the request?",
  "I'm not sure I understand. Could you clarify the last message you sent?",
  "I don't understand. Could you reword your request so it's clearer?",
  "Could you clarify what you mean by your last request?",
  "I'm confused. Can you rephrase that request?",
  "I didn't understand. Can you clarify what you want me to do next?",
  "Sorry, I'm not following. Could you explain it again?",
  "I'm not sure what you mean. Can you restate your question clearly?",
  "I don't understand. Could you clarify the question you asked?",
  "Could you clarify your meaning in that message?",
  "I'm confused—could you restate it in simpler words?",
  "I didn't catch that. Can you clarify the request again?",
  "Sorry, I didn't understand. Could you clarify your question in another way?",
  "I'm not following. Could you rephrase what you want to know?",
  "I don't get it. Could you clarify what you're asking for?",
  "Could you clarify that for me, please?",
  "I'm confused. Could you reword the question for clarity?",
  "I didn't understand. Could you clarify the intent of your question?",
  "Sorry, I'm not sure I understand. Can you rephrase again?",
  "I'm not following. Could you clarify what you meant by that statement?",
  "I don't understand. Can you restate what you're asking in different words?",
  "Could you clarify what you mean by your statement?",
  "I'm confused—can you clarify your last point again?",
  "I didn't understand. Could you rephrase the question so it's clear?",
  "Sorry, I'm not sure what you mean. Can you clarify your request again?",
  "I'm not following. Can you restate that with more clarity?",
  "I don't understand. Could you clarify your question once more?",
  "Could you clarify what you're referring to in your question?",
  "I'm confused. Could you rephrase your last message with more detail?",
  "I didn't catch that. Can you restate your request more clearly?",
  "Sorry, I didn't understand. Could you clarify what you mean by that?",
  "I'm not sure I understand. Can you reword your question to be clearer?",
  "I don't understand. Could you clarify what you're asking me to do?",
  "Could you clarify what you mean, in other words?",
  "I'm confused—can you restate the question more simply?",
  "I didn't understand. Could you clarify your request in plain language?",
  "Sorry, I'm not following. Could you rephrase the last message?",
  "I'm not sure I understand. Can you clarify the details of your request?",
  "I don't understand. Could you restate your question in a clearer way?",
  "Could you clarify your message again, please?",
  "I'm confused. Could you explain your request another way?",
  "I didn't catch that. Could you clarify what you're trying to say?",
  "Sorry, I didn't understand. Can you rephrase your request more simply?",
  "I'm not following. Could you clarify your question in simpler terms?",
  "I don't get it. Could you restate your last message for clarity?",
  "Could you clarify what you want me to do with that?",
  "I'm confused—could you reword it again?",
  "I didn't understand. Can you clarify your meaning in a different way?",
  "Sorry, I'm not sure I understand. Could you rephrase the question again?",
  "I'm not following. Could you restate your request in other words?",
  "I don't understand. Can you clarify what you want to ask?",
  "Could you clarify your last message so I understand?",
  "I'm confused. Can you restate what you mean by that?",
  "I didn't catch that. Could you rephrase the question more clearly?",
  "Sorry, I didn't understand. Could you clarify what you're referring to?",
  "I'm not sure I understand. Can you restate your question with more context?",
  "I don't understand. Could you clarify your last question in simpler words?",
  "Could you clarify your request so it makes sense to me?",
  "I'm confused—can you rephrase your message more clearly?",
  "I didn't understand. Could you restate your question again?",
  "Sorry, I'm not following. Could you clarify your question for me again?",
  "I'm not sure what you mean. Can you clarify your request one more time?",
  "I don't understand. Could you reword it so I can follow?",
  "Could you clarify what you mean by that question?",
  "I'm confused. Could you restate your message with more clarity?",
  "I didn't catch that. Could you clarify your message again?",
  "Sorry, I didn't understand. Could you restate it more clearly?",
  "I'm not sure I understand. Can you clarify your question a bit more?",
  "I don't understand. Could you clarify your message in simpler terms?",
  "Could you clarify your request again so I can help?",
  "I'm confused—could you rephrase your request with more detail?",
  "I didn't understand. Can you clarify what you're saying in your question?",
  "Sorry, I'm not sure what you mean. Could you restate it in other words?",
  "I'm not following. Could you clarify the meaning of your last message?",
  "I don't get it. Could you clarify what you mean by that request?",
  "Could you clarify what you're asking me to respond to?",
  "I'm confused. Can you rephrase your request in plain terms?",
  "I didn't understand. Could you clarify what you meant in your message?",
  "Sorry, I'm not following. Can you restate your question with more clarity?"
]

COLORS = {
    "prompt": "\033[34m",
    "input": "\033[31m",
    "countdown": "\033[32m",
    "reset": "\033[0m"
}

COMMANDS = {
    "fill":   ["fill","fill the","fil","fil the",],
    "exit":   ["q","e","exit","terminate","quit","end","save and exit","save and quit","save and end","save and terminate","end game","exit game","quit game","terminate game"],
    "go":     ["go","walk","travel","head"],
    "take":   ["pick up the","take the","get the","grab the","pick the","pickup","pick up","take","get","grab","pick"],
    "read":   ["read the","readthe","read"],
    "open":   ["open up the","unlock the","open the","open up","unlock","open"],
    "yes":    ["yes","y"],
    "no":     ["no","n"],
    "box":    ["minute box","tiny box","small box","box","large box","huge box","box that weighs a ton","stick"],
    "admin":  ["a","ad","admin","administrator","adminm"],
    "delete": ["del","delete","delete acount","del acount"],
    "search": ["search","search the","searchthe","serch","sarch"],
    "info":   ["info","help","INFO","INFORMATION","HELP","COMMANDS","COMMANDS LIST","COMMAND LIST","HELP ME","HELP!","WHAT CAN I DO?","WHAT CAN I DO"],
    "inventory": ["inventory", "stuff i own", "INVENTORY","i","I","stuff"],
    "weapons":["weapons","my weapons","WEAPONS","attackers","killers","killer things"],
    "food":   ["food","my food","FOOD","eaters","eating things"],
    "water":  ["water","my water","WATER","drinkers","drinking things","bottles","bottle"],
    "eat":    ["eat","eat the","devour","devour the","munch","munch the"],
    "drink":  ["drink","drink the","gulp","gulp the","quench","quench the"],
    "stats":  ["stats","STATS","status","player stats","st","s"],
    "deaths": ["death","deaths","my deaths","my death","deth","dath","deths","d"],
    "move":   ["move","move the","move te","move it"],
    "enter":  ["enter","go into","enter the","go into the","enter into","go into the"],
    "climb":  ["climb","clim","climb the","climb up","climb up the"],
    "left":   ["left","leftwards","l"],
    "right":  ["rightwards","right","r"],
    "adminmode": ["adminmode","toggle admin","toggle admin mode","admin mode","change admin mode","toggle adminm","toggle adminm mode","adminm mode","change adminm mode","toggle a","toggle adminm","a mode","at"],
    "on":     ["on","enable","turn on","start"],
    "off":    ["off","disable","turn off","stop","end","terminate","of"],
    "inspect":["inspect","inspect the","look at","look closer at","examine","examine the","check","check the"],
    ""
    "mine":   {"COMMANDS":{
                   "mine":["mine the","whack the","mine","whack","hit the","hit"]},
                "TARGETS":{        
                   "ore":   ["ore","ores","rock","rocks","wall","walls"],
                   "north": ["forwards","forward","north","n"],
                   "south": ["backwards","backward","south","s"],
                   "east":  ["rightwards","rightbound","leftward","right","east","e"],
                   "west":  ["leftwards","leftbound","leftward","left","west","w"],
                   "north/west": ["north west","northwest","north/west","north / west","north/ west","north /west","north\\west","n/w","n / w","n/ w","n /w"]
        }},
}

TARGETS = {
    "north": ["forwards","forward","north","n"],
    "south": ["backwards","backward","south","s"],
    "east": ["rightwards","rightbound","leftward","right","east","e"],
    "west": ["leftwards","leftbound","leftward","left","west","w"],
    "mines":["into mines","mines","the mines","into the mines"],
    "dit"+"ch":["into dit"+"ch","dit"+"ch","the dit"+"ch","into the dit"+"ch","in dit"+"ch","in the dit"+"ch"],
    "rocks":["rocks","the rocks","rock","the rock"],
    "letter":["letter","the letter","note","the note","welcome letter","the welcome letter","welcome to zarckary letter","the welcome to zarckary letter","welcome to zarckary","zarkary","the welcome to zarckary","zarckary letter","the zarckary letter"],
    "starter_food":["starter food pack","the starter food pack","starter pack","the starter pack","starter food","the starter food","pack","the pack","pack of food","the pack of food","pack of starter food","the pack of starter food","food","the food"],
    "water_bottle": ["water bottle","the water bottle","bottle","the bottle","water","the water"],
    "into_mine": ["mine","mines","the mine"],
    "tree":["tall tree","tree","tre","big tree"],
    "barn":["barn","the barn","the small barn","small barn","little barn","the little barn"],
    "barn_door":["barn door","the barn door"],
    "area":["area","the area","surroundings","my surroundings","road","the road","forest","the forest","dense forest","the dense forest","plains","the plains","fields","the fields","barley","the barley","rice","the rice","corn","the corn","wheat","the wheat","field trail","the field trail","mountain","mountains","the mountains","the mountain","valley","the valley"],
}

game_board = {
    "main_board":{
            "-7,-9":"Plains.","-6,-9":"Plains with Road to the East.","-5,-9":"Road with Plains to North/West and Rocky area to the East. The air has a fresh salty smell.","-4,-9":"You fell in the dit"+"ch and cant see anything. The air has a fresh salty smell.","-3,-9":"Rocky area with Road to North/West and sea to South/East.",
            "-7,-8":"Plains.","-5,-8":"Plains with Road to South/East.","-4,-8":"You fell in the dit"+"ch and cant see anything!","-3,-8":"Road with Plains to North/West and a Rocky area to South/East.","-2,-8":"Rocky area with Road to North/West and sea to South/East.",
            "-7,-7":"Plains with Forest to the North.","-6,-7":"Plains with Forest to the North.","-5,-7":"Plains.","-4,-7":"Plains with Road to South/East.","-3,-7":"You fell in the dit"+"ch and cant see anything!","-2,-7":"Road with Plains to North/West and a Rocky area to South/East.","-1,-7":"Rocky area with Road to North/West and sea to South/East.",
            "-7,-6":"Forest with Plains to South/East.","-6,-6":"Forest with Plains to South/East.","-5,-6":"Plains with Forest to North/West.","-4,-6":"Plains with Forest to North/West.","-3,-6":"Plains with Forest to the North.","-2,-6":"You fell in the dit"+"ch and cant see anything!","-1,-6":"Road with Plains to the West and Rocky area to South/East.","0,-6":"Rocky area with Road to North/West, sea to South/East and Fields to North/East.","1,-6":"Rocky area with Fields to the North. To the South some big boulders block your vision.","2,-6":"you are standing on a large boulder and can se far into the distance. To the North Fields stretch on forever. To the South just sea and to North/West Forest stretches on forever over which some tall Mountains can be seen.",
            "-7,-5":"Dense Forest. The trees block all view of the surrounding area.","-6,-5":"Forest. You glimpse some light to South/East.","-5,-5":"Forest with Plains to South/East.","-4,-5":"Plains with Forest to North/West.","-3,-5":"Plains with Forest to North/West.","-2,-5":"Plains with Forest to North/West and Road to South/East.","-1,-5":"Road with Plains to the West and Fields to the East.","0,-5":"Fields with Road to the West and Rocky area to the South. You are on a Field trail.","1,-5":"Fields with Rocky area to the South. You are on a Field trail going West - East.","2,-5":"Fields with Rocky area to the South. You are on a Field trail going West - East.","3,-5":"Fields with Rocky area to South/West. You are on a Field trail going West - East.","4,-5":"Fields. You are on a Field trail going West - East.","5,-5":"Fields. You are on a Field trail going West - East.","6,-5":"Fields. You are at the end of a Field trail going West - East.",
            "-8,-4":"Forest. Congratulations on finding out that the West end of the map is not perfectly straight! Choose between minute box, tiny box, small box, box, large box, huge box, box that weighs a ton or stick.","-7,-4":"Dense Forest. The trees block all view of the surrounding area.","-6,-4":"Dense Forest. The trees block all view of the surrounding area.","-5,-4":"Dense Forest. The trees blocks all view of the surrounding area.","-4,-4":"Dense Forest. You glimpse a light to South/East.","-3,-4":"Forest with Plains to South/East.","-2,-4":"Plains with Forest to North/West.","-1,-4":"You fell in the dit"+"ch and cant see anything!","0,-4":"You fell in the dit"+"ch and cant see anything!","1,-4":"Fields. You are bushwhacking trough Corn.","2,-5":"Fields. You are bushwhacking trough Corn.","3,-4":"Fields. You are bushwhacking trough Corn.","4,-4":"Fields. You are bushwhacking trough Corn.","5,-4":"Fields. You are bushwhacking trough Corn.","6,-4":"Fields. You are bushwhacking trough Corn.",
            "-7,-3":"Dense Forest. The trees blocks all view of the surrounding area.","-6,-3":"Dense Forest. The trees blocks all view of the surrounding area.","-5,-3":"Dense Forest. The trees blocks all view of the surrounding area.","-4,-3":"Dense Forest. The trees blocks all view of the surrounding area.","-3,-3":"Dense Forest with Plains to South/East.","-2,-3":"Forest with Plains to the South.","-1,-3":"Forest with Plains to the South and Road to the East.","0,-3":"Road with Forest to the West, Plains to South/West and Fields to the East.","1,-3":"Fields with Road to the West. You are on a Field trail going West - East.","2,-3":"Fields. You are on a Field trail going West - East.","3,-3":"Fields. You are on a Field trail going West - East.","4,-3":"Fields. You are on a Field trail going West - East.","5,-3":"Fields. You are on a Field trail going West - East.","6,-3":"Fields. You are at the end of a Field trail going West - East.",
            "-7,-2":"Dense Forest. The trees blocks all view of the surrounding area.","-6,-2":"Dense Forest. The trees blocks all view of the surrounding area.","-5,-2":"Dense Forest. The trees blocks all view of the surrounding area.","-4,-2":"Dense Forest. The trees blocks all view of the surrounding area.","-3,-2":"Dense Forest. The trees blocks all view of the surrounding area.","-2,-2":"Dense Forest. The trees blocks all view of the surrounding area.","-1,-2": "Forest with Road to the East.","0,-2":"Road with Forest to the West and Fields to the East.","1,-2":"Fields with Road to the West. You are bushwhacking through Wheat.","2,-2":"Fields. You are bushwhacking through Wheat. The wheat is so thick you cant see you are own feet!","3,-2":"Fields. You are bushwhacking through Wheat.","4,-2":"Fields. You are bushwhacking through Wheat.","5,-2":"Fields. You are bushwhacking through Wheat. You see a small barn to North/East.","6,-2":"Fields. You are bushwhacking through Wheat. You se a small barn to the North.",
            "-7,-1":"Dense Forest. You see a clearing to the North.","-6,-1":"Dense Forest. You glimpse a clearing to North/West.","-5,-1":"Dense Forest. The trees blocks all view of the surrounding area.","-4,-1":"Dense Forest. The trees blocks all view of the surrounding area.","-3,-1":"Dense Forest. The trees blocks all view of the surrounding area.","-2,-1":"Dense Forest. The trees blocks all view of the surrounding area.","-1,-1":"Forest with Road to the East.","0,-1":"Road with Forest to the West and Fields to the East.","1,-1":"Fields with Road to West. You are on a Field trail going West - East.","2,-1":"Fields. You are on a Field trail going West - East.","3,-1":"Fields. You are on a Field trail going West - East.","4,-1":"Fields. You are on a Field trail going West - East.","5,-1":"Fields. You see a small barn to the East. You are on a Field trail going West - East.","6,-1": "Fields. You see a small barn, the red paint peeling off. The front doors are closed. You are on a Field trail going West - East.",
            "-7,0":"you are standing in a clearing. To the North you see a small mound of dirt.","-6,0":"Forest. You se a clearing to North/West.", "-5,0":"Dense Forest. The trees blocks all view of the surrounding area.","-4,0":"Dense Forest. The trees blocks all view of the surrounding area.","-3,0":"Dense Forest. The trees blocks all view of the surrounding area.","-2,0":"Dense Forest. The trees blocks all view of the surrounding area.","-1,0":"Forest with Road to the East.","0,0":"You are standing on the start point.","1,0":"Fields with Road to the West. You are bushwhacking through Barley.","2,0":"Fields. You are bushwhacking through Barley.","3,0":"Fields. You are bushwhacking through Barley.","4,0":"Fields. You are bushwhacking through Barley.","5,0":"Fields. You are bushwhacking through Barley. You see a small barn to South/East.","6,0":"Fields. You are bushwhacking through Barley. You see a small barn to the South.",
            "-7,1":"you are standing in a clearing with woods all around. In front of you is a pile of rocks laying on a small mound of dirt.","-6,1":"Dense Forest with a clearing to the West.","-5,1":"Dense Forest. The trees blocks all view of the surrounding area.","-4,1":"Dense Forest. You see a tall tree to North/East.","-3,1":"Dense Forest. You see a tall tree to the North.","-2,1":"Dense Forest. You see a tall tree to North/West.","-1,1":"Forest with Road to the East.","0,1":"Road with Forest to the West and Fields to the East.","1,1":"Fields with Road to West. You are on a Field trail going West - East.","2,1":"Fields. You are on a Field trail going West - East.","3,1":"Fields. You are on a Field trail going West - East.","4,1":"Fields. You are on a Field trail going West - East.","5,1":"Fields. You are on a Field trail going West - East.","6,1": "Fields. You are at the end of a Field trail going West - East.",
            "-7,2":"Forest with a clearing to the South.","-6,2":"Dense Forest. The trees blocks all view of the surrounding area.","-5,2":"Dense Forest. The trees blocks all view of the surrounding area.","-4,2":"Dense Forest. You see a tall tree to the East.","-3,2":"Dense Forest. A tall tree stands before you. The trees blocks any other view of the surrounding area.","-2,2":"Dense Forest. You see a tall tree to the West.","-1,2":"Forest with Road to the East.","0,2":"Road with Forest to the West and Fields to the East.","1,2":"Fields with Road to West. You are bushwhacking through Canola.","2,2":"Fields. You are bushwhacking through Canola.","3,2":"Fields. You are bushwhacking through Canola.","4,2":"Fields. You are bushwhacking through Canola.","5,2":"Fields. You are bushwhacking through Canola.","6,2":"Fields. You are bushwhacking through Canola.",
            "-7,3":"Dense Forest. The trees blocks all view of the surrounding area.","-6,3":"Dense Forest. The trees blocks all view of the surrounding area.","-5,3":"Dense Forest. The trees blocks all view of the surrounding area.","-4,3":"Dense Forest. You see a tall tree to South/East.","-3,3":"Dense Forest. You see a tall tree to the South.","-2,3":"Dense Forest. You see a tall tree to South/West.","-1,3":"Forest with Road to the East.","0,3":"Road with Forest to the West and Fields to the East.","1,3":"Fields with Road to West. You are on a Field trail going West - East.","2,3":"Fields. You are on a Field trail going West - East.","3,3":"Fields. You are on a Field trail going West - East.","4,3":"Fields. You are on a Field trail going West - East.","5,3":"Fields. You are on a Field trail going West - East.","6,3": "Fields. You are at the end of a Field trail going West - East.",
            "-7,4":"Dense Forest. The trees blocks all view of the surrounding area.","-6,4":"Dense Forest. The trees blocks all view of the surrounding area.","-5,4":"Dense Forest. You glimpse a light to North/East.","-4,4":"Forest with Rocky area to North/East.","-3,4":"Forest with Rocky area to North/East.","-2,4":"Rocky area with Forest to South/West.","-1,4":"You fell in the dit"+"ch and cant see anything!","0,4":"Fields with Road to the West. You are bushwhacking through Rice.","1,4":"Fields. You are bushwhacking through Rice.","2,4":"Fields. You are bushwhacking through Rice.","3,4":"Fields. You are bushwhacking through Rice.","4,4":"Fields. You are bushwhacking through Rice. You see a Boathouse to North/East.","5,4":"Fields. You are bushwhacking through Rice. You see a Boathouse to the North.","6,4":"Fields. You are bushwhacking through Rice. You see a Boathouse to North/West.",
            "-7,5":"Forest with Mountains to North/East.","-6,5":"Forest with Mountains to North/East.","-5,5":"Forest with Mountains to North/East.","-4,5":"Valley with Mountains to the North and Forest to the South.","-3,5":"Valley with Mountains to the North and Forest to the South.","-2,5":"Rocky area with Mountains to North/West and Forest to South/West.","-1,5":"Rocky area.","0,5":"Rocky area with Road to South/East.","1,5":"Road with Rocky area to the West.","2,5":"Light Forest with Road to the West and fields to the South.","3,5":"Light Forest with Fields to the south.","4,5":"Light Forest with Fields to the South and Lake to North/East. You see a Boathouse to the East.","5,5":"Plains with Forest to the West, Fields to the South and Lake to the North. Before you is a Boathouse with no visible means of entry except a boarded up door.","6,5":"Plains with Fields to the South and Lake to North/West. You see a Boathouse to the West",
            "-7,6":"Valley with Forest to the South and Mountains to the North.","-6,6":"Valley with Forest to the South and Mountains to the North.","-5,6":"Valley between a Mountain to the west and another one to the East.","-4,6":"You climbed up a mountain. From here you can see very far into the distance. To the East a wide Rocky area lies. To the South Forest stretches on as far as you can see.","-3,6":"You climbed up a mountain. From here you can see very far into the distance. To the East a wide Rocky area lies. To the South Forest stretches on as far as you can see.","-2,6":"Rocky area with Mountains to the West.","-1,6":"Rocky area.","0,6":"Rocky area with Road to the South/East.","1,6":"You fell in the dit"+"ch and cant see anything!","2,6":"Light Forest with Road to the West.","3,6":"Light Forest with Lake to the East.","4,6":"Lake. Boathouse lies South/East from here.","5,6":"Lake. Boathouse lies to the South.","6,6":"Lake. Boathouse lies South/West from here.",
    },
    "barn_board":{"0,0":"Two big barn doors loom up in front of you. You can not open them, because their locked from the inside.",
                  "0,1":"you are in the south part of the barn. To your left is a manure tunnel. It makes the whole barns stink. To your right you see two small weird holes in the ground. In front of you is a tower of hay. The roof looks lower on the inside then on the outside. Two large barn doors tower upp behind you locked by a huge shiny padlock.",}
}

items = {"weapons_and_items":{"stars":{"owned":0,"damage":20,"chance":0.6545},"za'roc":{"owned":0,"damage":30},"axe":{"owned":0},"shovel":{"owned":0},"pickaxe_bad":{"owned":0},"pickaxe_good":{"owned":0},"pickaxe_perfect":{"owned":0},"rope":{"owned":0},"matches":{"owned":0},"lamp":{"owned":0,"on":False},"kerosene":{"owned":0},"mine_map":{"owned":0,"started":False},"letter": {"owned": 0},"stick":{"owned":0}},
         "food":{"starter_food":{"owned":0},"bread":{"owned":0,"value":40},"apple":{"owned":0,"value":65},"snail_pieces":{"owned":0,"value":"10"}},
         "water":{"0.5l_full_bottle":{"owned":0,"value":50,"%":100},"1l_full_bottle":{"owned":0,"value":100,"%":100},"2l_full_bottle":{"owned":0,"value":200,"%":100},"5l_full_bottle":{"owned":0,"value":500,"%":100},"0.5l_empty_bottle":{"owned":0},"1l_empty_bottle":{"owned":0},"2l_empty_bottle":{"owned":0},"5l_empty_bottle":{"owned":0}}
         }

trespass = 0
base_items = items
x = 0
y = 0
data = {}
attrdict = {"death":{},"barn":False,"attr":[], "searched_ditch":{"-5,-9":False,"-4,-9":False,"-4,-8":False,"-3,-8":False,"-3,-7":False,"-2,-7":False,"-2,-6":False,"-1,-6":False,"-1,-5":False,"-1,-4":False,"0,-3":False,"0,-2":False,"0,-1":False,"0,0":False,"0,1":False,"0,2":False,"0,3":False,"0,4":False,"1,4":False,"1,5":False,"1,6":False,"2,6":False,"2,7":False,"2,9":False},"searched":[],"water_sources":[]}
achieved = []
turns = -1
player_stats = {"health":100,"hunger":100,"thirst":100,"attack":15,"strength":15,"defense":10,"start_time":0,"play_time":0,"xp":{"total":0}}
enter = 5
lastxy = "0,0"
info = ["IMPORTANT - turning off terminal without using the proper exit command will delete your acount!"," ","Informational commands: 'INFO' - shows this message.","'INVENTORY' - shows your whole inventory.","'WEAPONS' - shows your weapons","'FOOD' - shows your food","'WATER' - shows any water bottles you own and their status.","'STATS' - shows your stats.","'ACHIEVEMENTS' - shows your achievements.","'DEATHS' - shows all the ways you have died."," ",""]
typespeed = 0
wait = time.sleep
exit_event = Event()
save_lock = threading.Lock()




class cricket_storm:
    def __init__(self):
        self.health = 60
        self.speed = 3
        self.endurance = 5
        self.attack = 15
        self.strength = 20
        self.defense = 0

class yeti:
    def __init__(self):
        self.health = 350
        self.speed = 7
        self.endurance = 17
        self.attack = 40
        self.strength = 45
        self.defense = 32

class forest_troll:
    def __init__(self):
        self.health = 150
        self.speed = 5
        self.endurance = 10
        self.attack = 30
        self.strength = 35
        self.defense = 20

class goblin:
    def __init__(self):
        self.health = 90
        self.speed = 4
        self.endurance = 7
        self.attack = 25
        self.strength = 25
        self.defense = 15

class giant_snake:
    def __init__(self):
        self.health = 130
        self.speed = 3.5
        self.endurance = 8
        self.attack = 35
        self.strength = 30
        self.defense = 20

class dragon_boss:
    def __init__(self):
        self.health = 500
        self.speed = 10
        self.endurance = 0
        self.attack = 50
        self.strength = 50
        self.defense = 40

class giant_spider:
    def __init__(self):
        self.health = 80
        self.speed = 4.2
        self.endurance = 6
        self.attack = 20
        self.strength = 25
        self.defense = 17

def normalize_stem(word: str) -> str:
    word = re.sub(r"[^a-z]", "", word.lower())

    for suffix in COMMON_SUFFIXES:
        if len(word) > len(suffix) + 2 and word.endswith(suffix):
            if suffix in {"ies", "ied", "ier", "iers", "iest"}:
                return word[: -len(suffix)] + "y"
            return word[: -len(suffix)]

    return word

def build_word_forms(word: str) -> set[str]:
    word = word.lower()
    forms = {word}

    if len(word) < 3:
        return forms

    forms.update(
        {
            f"{word}s",
            f"{word}es",
            f"{word}ed",
            f"{word}ing",
            f"{word}er",
            f"{word}ers",
            f"{word}est",
            f"{word}ly",
            f"{word}ness",
            f"{word}ful",
            f"{word}less",
        }
    )

    if word.endswith("e") and len(word) > 3:
        base = word[:-1]
        forms.update({f"{base}ing", f"{base}er", f"{base}est", f"{base}ed"})

    if word.endswith("y") and len(word) > 3:
        base = word[:-1]
        forms.update({f"{base}ies", f"{base}ied", f"{base}ier", f"{base}iest"})

    return forms

def words_match(token: str, candidate: str) -> bool:
    token = token.lower()
    candidate = candidate.lower()

    if token in build_word_forms(candidate):
        return True

    token_stem = normalize_stem(token)
    candidate_stem = normalize_stem(candidate)

    if token_stem == candidate_stem:
        return True

    if len(token_stem) >= 4 and len(candidate_stem) >= 4:
        return token_stem.startswith(candidate_stem) or candidate_stem.startswith(token_stem)

    return False

def find_match(target: str) -> tuple[str, str] | None:
    tokens = re.findall(r"[a-z']+", target.lower())

    for category, payload in WORDS.items():
        for candidate in payload.get("words", []):
            for token in tokens:
                if words_match(token, candidate):
                    return category, candidate

    return None

def respond_if_match(target: str,flag) -> str | None:
    match = find_match(target)

    if match is None:
        return flag
    else:
        flag = "language"

    category, _matched_word = match
    printz(random.choice(WORDS[category].get("phrases", ["..."])))
    return flag

def line():
    frame = inspect.currentframe().f_back  # go one frame back
    return frame.f_lineno

def Mines():
    printz("The mines are not yet implemented. Check back later for updates.")
    wait(2)
    printz("Sorry for the inconvenience.")
    printz("Exiting mines...")
    return
   
def timez(izoformat):
    izoformat = str(izoformat)

    y = izoformat[0:4]
    m = izoformat[5:7]
    d = izoformat[8:10]
    t = izoformat[14:19]

    return f"{t} {d}/{m}/{y}"

def Game_over():
    key_len = 30
    save_key = ""
    try:
        for f in range(key_len):
            save_key += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
        # save acount if watcher terminates game without reason
        data[username]["save_key"] = {"key":save_key,"data":data[username].copy()}
        # reset
        data[username]["x"] = 0
        data[username]["y"] = 0
        data[username]["items"] = base_items
        data[username]["lastxy"] = "0,0"
        data[username]["player_stats"]["health"] = 100
        data[username]["player_stats"]["attack"] = 15
        data[username]["player_stats"]["strength"] = 15
        data[username]["player_stats"]["defense"] = 10
        data[username]["player_stats"]["thirst"] = 100
        data[username]["player_stats"]["hunger"] = 100
        data[username]["attrdict"]["attr"].append("reset1")
    except KeyError:
        print(f"Error line() {line()}: Could not reset {username} because {username} does not exist.")
        os._exit(0)
    json_dump(data)
    while True:
        start_again = inputz("Do you want to try again?>  ")
        if start_again in COMMANDS["yes"]:
            printz(f"You decided to try again.")
            Start_game(data,x,y,wait,typespeed,lastxy,player_stats,achieved,attrdict,items,trespass)
        elif start_again in COMMANDS["no"]:
            printz(f"You rage quieted and exited.")
            printz(f"Exiting...")
            os._exit(0)
        else:
            printz(f"Invalid input try again.")

def inputz(text):
    sys.stdout.write(COLORS["prompt"] + text)
    sys.stdout.flush()

    sys.stdout.write(COLORS["input"])
    sys.stdout.flush()

    user_input = input()

    sys.stdout.write(COLORS["prompt"])
    sys.stdout.flush()
    return user_input

def Search_ditch():
    printz(f"you are searching the dit"+"ch.")
    wait(2)
    printz(f"This takes 15 seconds.")
    Countdown(15)
    print(" ")
    i = random.randint(1,100)
    if i > 1 and i < 20:
        printz(f"You searched the dit"+"ch but found nothing.")
    elif i >= 20 and i < 30:
        printz(f"You searched the dit"+"ch and found a water bottle! You picked it up.")
        items["water"]["1l_full_bottle"]["owned"] += 1
    elif i >= 30 and i < 40:
        printz(f"You searched the dit"+"ch and found a whole loaf of bread! You picked it up.")
        items["food"]["bread"]["owned"] += 1
    elif i >= 40 and i < 50:
        printz ("You searched the dit"+"ch and found a throwing star! You picked it up.")
        items["weapons_and_items"]["stars"]["owned"] += 1
    elif i >= 50 and i < 80:
        printz(f"You searched the dit"+"ch and found absolutely nothing.") 
    elif i >= 80 and i <= 100:
        printz(f"You searched the dit"+"ch and found an apple! You picked it up.")
        items["food"]["apple"]["owned"] += 1
    else:
        printz(f"You searched the dit"+"ch but found nothing.")

def Search():
    chance = random.randint(0,100)
    if chance <= 10:
        amount = random.randint(1,4)
        printz(f"You found {amount} snail pieces in your surrounding area! They each are worth 10 hunger points, but might give you food poisoning!")
        items["food"]["snail_pieces"]["owned"] += amount
    elif chance >= 90:
        printz("You found a 500 ml bottle of dirty water! It is worth 50 thirst points, but might poison you!")
    else:
        printz("You did not find anything in your surrounding area.")

def bold(text):
    return f"\033[1m{text}\033[22m"

def printz(text,sameline=False):
    cut = False
    if "no_printz" not in attrdict["attr"]:
        i = 0
        times = 0
        while i < len(text):
            if times > 140 and text[i] == " ":
                text = text[:i] + "\n" + text[i+1:]   
                times = 0
            else:
                times += 1
            i += 1
        global typespeed
        if typespeed == 0:
            typespeed = TYPE_SPEED
        for letter in text:
            print(letter, end="", flush=True)
            wait(typespeed)
    elif "no_printz" in attrdict["attr"]:
        print(text)
    else:
        print(f"Error line {line()}: Invalid state for printz function. Check attrdict['attr'] for invalid states.")
    if sameline == True:
        print("\r", end="", flush=True)
    else:
        print(" ")

def Countdown(seconds):
    if "countdown" not in attrdict["attr"]:
        print(COLORS["countdown"], end="", flush=True)
        for f in range(seconds,-1,-1):
            print("\r"+str(f), end="", flush=True)
            wait(1)
            print("\r","                                                                                                            ", end="", flush=True)
        print("\r"+str(0), end="", flush=True)
        print(COLORS["prompt"])
    else:
        print(COLORS["countdown"], end="", flush=True)
        printz(f"Countdown: {seconds} seconds skipped.")
        print(COLORS["prompt"])

def RUN(times, speed):
    try:
        times = int(times)
    except ValueError:
        print("Invalid input, could not turn",times,"into integer!")
        return True
    try:
        speed = int(speed)
    except ValueError:
        print("Invalid input, could not turn",speed,"into integer!")
        return True
        
    while times > 0:
        position = 0
        obstacles = ["Boulder", "Rock", "Tree trunk", "Cliff", "Iceberg", "Sand dune", "Mountain", "Big rock", "Sea", "Giant mushroom", "Large root", "Tree", "Stone monolith", "Glacier", "log", "boulder", "Stone pillar", "House", "Mountain", "Driftwood"]
        (random.randint(3,6))
        rand = random.randint(0,19)
        obstacle = random.randint(1,2)

        if obstacle == 1:
            print(obstacles[rand],"on the left!")
        elif obstacle == 2:
            print(obstacles[rand],"on the right!")
            
        if times == 3:
            print("You just entered the forest.")
        
        start = time.perf_counter()
        lr = inputz("RUN!>  ")
        total = time.perf_counter() - start
        print("total:",total)
        if lr == "left":
            position = 1
        elif lr == "right":
            position = 2
        else:
            print("Invalid operation:",lr+". Type 'left' or 'right'.")

        if total < speed and position != obstacle: 
            print("You made it past a obstacle!")
            times -= 1
            wait(random.randint(1,7))
            continue
        else:
            printz(f"You crashed into {obstacles[rand]}.")
            return False
    return True

def FIGHT(enemy):
    xy = f"{x},{y}"
    your = True
    infight = True
    alive = True
    name = enemy.__class__.__name__.replace("_"," ")
    run = False
    have_weapons = False

    while True:
        y_n = inputz("Do you want to fight the "+name+"? (y/n)>  ")

        # Running away
        if y_n in COMMANDS["no"]:
            printz(f"You decided to try to run away from the {name}.")
            printz(f"Use 'left' and 'right' to dodge obstacles and try to escape the {name}.")
            wait(10)
            run = True
            won = RUN(enemy.endurance,enemy.speed)
            if won == True:
                print(" ")
                printz(f"You successfully ran away from the "+name+"!")
                return 
            elif won == False:
                print(" ")
                printz(f"You failed to run away from the "+name+"!")
                wait(2)
                printz(f"The "+name+" caught up to you and is now attacking you!")
                your = False
                infight = True
                printz(f"You died while trying to run away from the "+name+".")
                wait(4)
                printz(f"Game over.")
                attrdict["death"][xy] = f"You died by {name} while running away from it."
                Game_over()

        # staying and fighting
        elif y_n in COMMANDS["yes"]:
            print(" ")
            printz(f"You decided to fight the "+name+"!")
            print(" ")
            printz(f"You have: {player_stats['health']} hp!")
            printz(f"your enemy has: "+str(int(enemy.health))+" hp!")
            print(" ")


            while infight == True:

                if run == True:
                    printz(f"You decided to run away from the "+name+".")
                    printz(f"Use 'left' and 'right' to dodge obstacles and try to escape the "+name+".")
                    Countdown(10)
                    alive = RUN(enemy.endurance,enemy.speed)
                    infight = False

                elif your == True:
                    for f in items["weapons_and_items"]:
                        try:
                            if items["weapons_and_items"][f]["owned"] > 0 and items["weapons_and_items"][f]["damage"] > 0:
                                have_weapons = True
                                break
                            else:
                                continue
                        except KeyError:
                            continue
                    if have_weapons == False:
                        printz(f"You have no weapons to fight with! You have to try to run away from the "+name+".")
                        run = True
                        continue
                    printz(f"Its your turn.")
                    print(" ")
                    printz(f"your weapons:")
                    print(" ")
                    for weapon in items["weapons_and_items"]:
                        try:
                            if items["weapons_and_items"][weapon]["owned"] > 0 and items["weapons_and_items"][weapon]["damage"] > 0:
                                printz(str(weapon)+" - "+str(items["weapons_and_items"][weapon]["owned"])+" owned.")
                                for f in items["weapons_and_items"][weapon]:
                                    printz(f"   "+str(f)+": "+str(items["weapons_and_items"][weapon][f]))
                                print(" ")
                        except KeyError:
                            continue
                    while True:
                        which_weapon = inputz("Which weapon do you want to use?>  ").replace(" ","_").lower()
                        if which_weapon in items["weapons_and_items"]:
                            try:
                                if items["weapons_and_items"][which_weapon]["damage"] > 0:
                                    if items["weapons_and_items"][which_weapon]["owned"] > 0:
                                        weapon = which_weapon
                                        break
                                    else:
                                        printz(f"You dont own any "+str(which_weapon)+"s! Try again.")
                                        continue
                                else:
                                    printz(f"A "+str(which_weapon)+" does not do damage you doofus! Try again.")
                                    continue
                            except KeyError:
                                printz(f"A "+str(which_weapon)+" does not do damage you doofus! Try again.")
                                continue
                        else:
                            printz(f"Invalid input, "+str(which_weapon)+" is not a weapon you own or does not exist. Try again.")
                            continue
                    attacked_hp, strength = weapon_action(weapon,player_stats)
                    print(" ")
                    if attacked_hp == 0 and strength == 0:
                        printz(f"your attack with "+str(weapon)+" missed and you took 0 hp!")
                    elif strength < enemy.defense:
                        printz(f"You did not have enough strength to penetrate the enemies defenses and took 0 hp!")
                    elif strength >= enemy.defense:
                        enemy.health -= attacked_hp
                        printz(f"your attack with "+str(weapon)+", hit and took "+str(attacked_hp)+" hp from your enemy!")
                        print(" ")
                        printz(f"You have: {player_stats['health']}hp!")
                        printz(f"your enemy has: {enemy.health}hp!")
                    if enemy.health < 1:
                        alive = True
                        infight = False
                        while True:
                            Continue = inputz("Do you want to continue fighting or do you want to try to run away? Continue (y/n)?>  ")
                            if Continue in COMMANDS["yes"]:
                                printz(f"You have: {player_stats['health']}hp!")
                                printz(f"your enemy has: {int(enemy.health)}hp!")
                                your = False
                                break
                            elif Continue in COMMANDS["no"]:
                                run = True
                                break
                            else:
                                print("Invalid input:",Continue+". Type 'y' or 'n'.")
                                continue
                        continue

                    while True:
                        print(" ")
                        Continue = inputz("Do you want to continue fighting or do you want to try to run away? Continue (y/n)?>  ")
                        if Continue in COMMANDS["yes"]:
                            your = False
                            print(" ")
                            printz(f"You have: {player_stats['health']}hp!")
                            printz(f"your enemy has: {enemy.health}hp!")
                            break
                        elif Continue in COMMANDS["no"]:
                            break
                        else:
                            print("Invalid input:",Continue+". Type 'y' or 'n'.")
                            continue
                    continue


                elif your == False:
                    printz(f"Its your enemies turn!")
                    print(" ")
                    if player_stats["defense"] < random.randint(enemy.strength//2, enemy.strength):
                        player_stats["health"] -= enemy.attack
                        printz(f"your enemy took {enemy.attack} hp from you!")
                    else:
                        printz(f"your enemy did not have enough strength to penetrate your defenses and took 0 hp!")
                    if player_stats["health"] < 1:
                        alive = False
                        infight = False
                    else:
                        your = True
                        continue
                    print(" ")
                    printz(f"You have: {player_stats['health']}hp!")
                    printz(f"your enemy has: {enemy.health}hp!")

            if alive == True and run == False:
                printz(f"You defeated the "+name+"! Congratulations!")
                return True
            elif alive == False and run == False:
                printz(f"You were defeated by the "+name+".")
                wait(4)
                printz(f"Game over.")
                attrdict["death"][xy] = f"You died while fighting {name}."
                Game_over()
            elif alive == True and run == True:
                printz(f"You successfully ran away from the "+name+"!")
                return False
            elif alive == False and run == True:
                printz(f"You failed to run away from the "+name+"!")
                printz(f"The "+name+" caught up to you and is now attacking you!")
                printz(f"You died while trying to run away from the "+name+".")
                wait(4)
                printz(f"Game over.")
                attrdict["death"][xy] = f"You died by {name} while running away from it."
                Game_over()
        else:
            print("Invalid input:",y_n+". Type 'y' or 'n'.")
            continue

def weapon_action(weapon,player_stats):
    if items["weapons_and_items"][weapon]["owned"] < 1:
        printz(f"Error in weapon action line() {line()}: You dont own any "+str(weapon)+"s!")
        os._exit(0)
    try:
        if items["weapons_and_items"][weapon]["disposable"] == True:
            items["weapons_and_items"][weapon]["owned"] -= 1
    except KeyError:
        pass
    
    if "chance" not in items["weapons_and_items"][weapon]:
        chance = 1
    else:
        chance = items["weapons_and_items"][weapon]["chance"]
    if random.random() < chance:
        total_damage = items["weapons_and_items"][weapon]["damage"] + player_stats["attack"]
        total_strength = random.randint(player_stats["strength"]//2, player_stats["strength"]) - items["weapons_and_items"][weapon]["strength"] if "strength" in items["weapons_and_items"][weapon] else random.randint(player_stats["strength"]//2, player_stats["strength"])
        return total_damage, total_strength
    else:
        return 0, 0

def angry_farmer(crop,data,username,x,y):
    xy = f"{x},{y}"
    printz(f"Oh, no. A farmer saw you bushwhacking his "+crop+" and does not like it!")
    wait(3)
    printz(f"The farmer points a pitchfork at you and yells 'GET AWAY FROM MY "+crop.upper()+"!!!!'.")
    wait(3)
    printz(f"The farmer starts running at you, brandishing his pitchfork at you.")
    wait(3)
    printz(f"You get very scared, so you start running away from the farmer. You dont think about that you could fight him.")
    wait(2)
    printz(f"Help your character by typing 'left' or 'right' when there comes a obstacle!")
    wait(1)

    Countdown(15)

    print("Go!")

    survived = RUN(6,2.89)
    if survived == False:
        wait(4)
        printz(f"The farmer raises the pitchfork over your head.")
        wait(4)
        printz(f"He says 'THU SHALL NEVER BUSHWHACK MY "+crop.upper()+" AGAIN! Smash.")
        wait(4)
        printz(f"You died by a pitchfork to the head.")
        del data[username]
        json_dump(data)
        wait(4)
        printz(f"your user has been deleted.")
        wait(4)
        printz(f"Better luck (and skills) next time.")
        attrdict["death"][xy] = "You died by a pitchfork to the head"
        Game_over()

    printz(f"You made it past all the obstacles and escaped the farmer! Congratulations!")
    wait(3)
    printz(f"The strain of running away from the farmer was too much for you, and you collapsed on the ground, unconscious for 20 seconds.")
    Countdown(20)
    printz(f"You woke up and can now continue your adventure.")
    wait(3)

    i = 5

    while i > 0:
        lost_input = inputz(">  ").strip().lower()
        if lost_input[0:2] == "go" and lost_input[3:] != "":
            printz(f"Which way is",lost_input[3:]+"?")
            i -= 1
        elif lost_input == "that way" or lost_input == "that way!":
            printz(f"Which way?")
        elif "direction" in lost_input or "direction!" in lost_input:
            printz(f"Which direction?")
        else:
            printz(f"Invalid operation: '"+lost_input+"'. Try 'go 'direction''.")
    printz(f"Oh, no!") 
    wait(2)
    printz(f"You dont know where your, where West is, where East is, where North is, and where South is!")
    wait(4)
    printz(f"The only thing you realize is that your in a forest.")
    wait(3)
    printz(f"How are you going to get back?")

    while True:
        evening = False
        lost_input = inputz("lost!>  ").lower().replace(" ","")
        if lost_input == "waitsunset":
            printz(f"Waiting until sun set")
            evening = True
            wait(20)
            printz(f"Evening.")
        elif lost_input == "sun position" or lost_input == "the sun position":
            if evening == True:
                printz(f"You found the suns setting position.")
                wait(3)
                printz(f"You seem to remember that the sun setts to the north!")
                wait(4)
                printz(f"You can now use command 'go'!")
                break
            else:
                printz(f"The sun is in the middle of the sky!")
        else:
            print("Invalid operation: '"+lost_input+"'. Try 'wait 'time_argument''.")
        
    while True:
        i = 30
        directional_input = inputz(">  ").lower().replace(" ","")
        if directional_input[0:2] == "go":
            if directional_input[2:] == "west":
                printz(f"You decided to go West.")
                wait(1)
                Countdown(i)
                printz(f"your journey West brings you past a large lake and to a tall mountain range.")
                wait(3)
                printz(f"You dont recognize the surroundings and cant get past the mountain range.")
                wait(3)
                printz(f"You walk back to the point you started at.")
                wait(2)
                Countdown(i)
            elif directional_input[2:] == "east":
                printz(f"You decided to go East.")
                wait(1)
                Countdown(i)
                printz(f"your journey East brought you into familiar territory")
                wait(3)
                printz(f"Now your actually back in the game,")
                wait(3)
                printz(f"but you dont know where on the board your!")
                break
            elif directional_input[2:] == "south":
                print("You decided to go South.")
                wait(1)
                Countdown(i)
                printz(f"your journey South brings you past a wide river and you end up by the sea.")
                wait(3)
                printz(f"You dont recognize your surroundings and cant get past the sea.")
                wait(3)
                printz(f"You walk back to the point you started at.")
                Countdown(i)
            elif directional_input[2:] == "north":
                printz(f"You decided to go North.")
                wait(1)
                Countdown(i)
                printz(f"your journey North brings you past a range of mountains and end at a wide plain, stretching on forever!")
                wait(3)
                printz(f"You dont recognize your surroundings and dont want to embark the plain.")
                wait(3)
                printz(f"You walk back.")
                Countdown(i)
            else:
                print("Invalid operation: '"+directional_input+"'.")
    x = random.randint(-5,9)
    y = random.randint(-7,6)

    return data,x,y

def Turns(turns,x,y,data,username):
    seaxy = {-4:-9,-2:-8,-1:-7,0:-6,1:-6,2:-6}
    turns += 1
    print("turns: " + str(turns))
    try:
        if seaxy[x] == y:
            if turns != 0 and 5 % turns:
                SWIM(data,username)
    except KeyError:
        None

def SWIM(data,username):
        xy = f"{x},{y}"
        i = 15
        speed = 1.25
        printz(f"A huge wave crashes over you.")
        wait(3)
        printz(f"You got pulled over the edge of the cliff and fall into the sea.")
        wait(3)
        printz(f"The cold water momentarily renders you unconscious for 15 second while you read the minigame instructions.")
        wait(4)
        printz(f"Read fast!")
        wait(2)
        printz(f"You have to type the word 'swim' as fast as you can until you either reach the shore or drown.")
        printz(f"You will drown if points becomes 30 and survive if points becomes 0")
        printz(f"You might end up at the same place that you started from, but there is a chance that you will end up somewhere else.")
        printz(f"Swim fast!")
        Countdown(15)
        printz(f"Go!")
        wait(1)
        i = 15
        survived = None
        while True:
            start = time.perf_counter()
            swim = inputz("SWIM! > ").lower().replace(" ","")
            elapsed = time.perf_counter() - start
            if swim == "swim":
                if elapsed >= speed:
                    i += 1
                else:
                    i -= 1
                print("Points", i)
                if i == 0:
                    survived = True
                    break
                elif i == 30:
                    survived = False
                    break
            else:
                print("Input", swim, "is not 'swim'")
        if survived == False:
            printz(f"You drowned!")
            printz(f"User "+username+" has been deleted.")
            printz(f"Better luck next time! :)")
            attrdict["death"][xy] = "You drowned"
            Game_over()
        elif survived == True:
            printz(f"You survived!")
            printz(f"Your back at the same place you started from and did not drift away.")

def json_pack(username,x,y):
        data[username] = {"password": password, "x": x, "y": y, "items": items, "achieved": achieved,"turns":turns,"trespass":trespass,"player_stats":player_stats,"lastxy":lastxy,"attrdict":attrdict}
        return data

def json_unpack(username,data):
        return data[username]["x"], data[username]["y"], data[username]["items"], data[username].get("achieved", []), data[username]["turns"],data[username]["trespass"],data[username]["player_stats"],data[username]["lastxy"],data[username]["attrdict"]

def json_dump(data):
        with save_lock:
            data = Zcryptv1.base64_encode1(data,JSON_ENCODED)
            data = Zcryptv1.ceasar_self_encode(data,10,JSON_ENCODED_KEY,JSON_ENCODED)
            with open("zark.json", "w") as f:
                json.dump(data, f, indent=4,sort_keys=True)

def json_load():
        with save_lock:
            try:
                with open("zark.json", "r") as f:
                    raw = json.load(f)
            except FileNotFoundError:
                return {}
            except json.JSONDecodeError:
                return {}

        if isinstance(raw, dict):
            return raw

        try:
            data = Zcryptv1.ceasar_self_decode(raw,10,JSON_ENCODED_KEY,JSON_ENCODED)
            data = Zcryptv1.base64_decode1(data,JSON_ENCODED)
            return data if isinstance(data, dict) else {}
        except Exception:
            return {}

def fill():
    for f in items["water"]:
        type = None
        bottle = items["water"][f]
        if bottle["owned"] > 0:
            try:
                if bottle["%"] == 0:
                    pass
            except KeyError:
                if f[0:1] == "0":
                    type = "0.5l_full_bottle"
                elif f[0:1] == "1":
                    type = "1l_full_bottle"
                elif f[0:1] == "2":
                    type = "2l_full_bottle"
                elif f[0:1] == "5":
                    type = "5l_full_bottle"
                
                if type == None:
                    printz(f"Error on line {line()}: water bottle failed to be recognized.")
                    os._exit(0)
                
                printz(f"opening bottle.",sameline=True)
                wait(5)
                print("                              ")
                printz(f"Leaning down.",sameline=True)
                wait(5)
                print("                              ")
                printz(f"Filling up bottle.",sameline=True)
                wait(5)
                print("                              ")
                Countdown(items["water"][type]["value"]//6)
                printz(f"{type} filled up.")

                items["water"][type]["owned"] += 1
                items["water"][f]["owned"] -= 1
                continue
                
def check_operations(command,target,user_input,raw_input,x,y,turns,username,data,enter):
        xy = f"{x},{y}"
        flag = None

        # Reload reseated data
        try:
            if user_input == data[username]["save_key"]["key"]:
                flag = "resave"
                printz(f"Reloading data...")
                wait(2)
                data[username] = data[username]["save_key"]["data"].copy()
                printz(f"Data reloaded!")
                print(" ")
                if "save_key" in data[username]:
                    del data[username]["save_key"]
                x,y,lastxy,position_flag = print_position(x,y,"none",data,username)
        except KeyError:
            None

        # special ops
        if raw_input == "zackary is the best!":
            flag = "admin"
            printz(f"You like me?")
            Countdown(1000)
            like = inputz("Do you still like me?>  ")
            if like in COMMANDS["yes"]:
                printz(f"Aww, thanks! I like you too!")
                wait(3)
                printz(f"I hope you enjoy the game! :)")
                wait(3)
                printz(f"Guess what? You just unlocked a secret achievement! Congratulations!")
                wait(3)
                printz(f"Its called 'admin'!")
                if "admin" not in attrdict["attr"]:
                    attrdict["attr"].append("admin")
                    printz(f"lucky you! You have unlocked the secret achievement 'admin'! You can now use the command 'admin' to access a secret menu with some fun options! Try it out!")
                else:
                    wait(3)
                    printz(f"You already unlocked the 'admin' achievement! Who are you trying to trick?")
                    wait(3)
                    printz(f"{username}! Your trying to trick me! I know you already unlocked the 'admin' achievement! Stop trying to trick me!")
                    wait(3)
                    printz(f"I hope you still enjoy the game, even if you dont like me. :)")
                    if username == "z":
                        printz()
            elif like in COMMANDS["no"]:
                printz(f"Oh, thats sad. I thought we had something special. I guess I was wrong.")
                wait(3)
                printz(f"I hope you still enjoy the game, even if you dont like me. :)")
            else:
                printz(f"Invalid input. I guess you dont like me, but thats ok. I hope you still enjoy the game! :)")
        
        # inspect (object) Finish
        elif command in COMMANDS["inspect"]:
            if xy == "barn,?" and target in TARGETS["barn_door"]:
                pass
            else:
                printz(f"You cant examine a {target}")

        # barn
        elif x == 6 and y == -1 and "inspected_barn_door" in attrdict["attr"]:
            flag = "barn"
            if command in COMMANDS["go"]:
                barn_target = target.split(" ")
                try:
                    barn_target.remove("of")
                    barn_target.remove("off")
                except ValueError:
                    None
                try:
                    if barn_target[0] in (TARGETS["north"],TARGETS["south"],TARGETS["east"],TARGETS["west"]):
                        if barn_target[1] in TARGETS["barn"]:
                            None

                except IndexError:
                    None
        
        # West side of map not perfectly straight (box)
        elif command in COMMANDS["box"] or target in COMMANDS["box"]:
            if "box" not in attrdict["attr"]:
                if x == -8 and y == -4:
                    if command in COMMANDS["take"]:
                        command = target.replace(" ","").lower()
                    else:
                        command = user_input.replace(" ","").lower()
                    flag = "box"
                    s_wait = 3
                    if command == "minutebox":
                        printz(f"You picked up minute box.")
                        wait(s_wait)
                        printz(f"Oh, no. You dropped minute box and can`t find it because its so small.")
                        attrdict["attr"].append("box")
                    elif command == "tinybox":
                        printz(f"You picked up tiny box.")
                        wait(s_wait)
                        printz(f"Oh, no. You put tiny box in your pocket and it slipped trough a hole! You can`t find it.")
                        attrdict["attr"].append("box")
                    elif command == "smallbox":
                        printz(f"You picked up small box. It makes a weird sloshy sound when you shake it.")
                        wait(s_wait)
                        printz(f"Oh, no. The box was full of water. It all spilled out and wrecked the box!")
                        attrdict["attr"].append("box")
                    elif command == "box":
                        printz(f"You picked up box.")
                        wait(s_wait)
                        printz(f"Oh, no. You slipped, fell and broke the box and its content with it.")
                        attrdict["attr"].append("box")
                    elif command == "largebox":
                        printz(f"You picked up large box.")
                        wait(s_wait)
                        printz(f"Oh, no. The large box was empty!")
                        attrdict["attr"].append("box")
                    elif command == "hugebox":
                        printz(f"You tried to pick up huge box but failed, because it is bolted to the ground!")
                        attrdict["attr"].append("box")
                    elif command == "boxthatweighsaton":
                        printz(f"You tried to pick up box that weighs a ton but failed miserably.")
                        printz(f"It weighs to much! You were neither able to open it up.")
                        attrdict["attr"].append("box")
                    elif command == "stick":
                        printz(f"You picked up stick. Could it be used as a weapon or as leverage to move something?")
                        items["weapons_and_items"]["stick"]["owned"] = True
                        attrdict["attr"].append("stick")
                        attrdict["attr"].append("box")
                    Turns(turns,x,y,data,username)
                else:
                    printz(f"You dont se a "+command+"!")
            elif "stick" in attrdict["attr"]:
                printz(f"You already picked up stick! Who are you trying to trick?")
                return x,y,flag,turns,data,enter
            elif "box" in attrdict["attr"]:
                printz(f"You sneaky little trickster, you already opened a box! Get out of town!")

        # Picking upp items
        elif command in COMMANDS["take"]:
            flag = "item"
            if target == "letter":
                if x == 0 and y == 0:
                    if items["weapons_and_items"]["letter"]["owned"] == 0:
                        printz(f"You picked up letter.")
                        items["weapons_and_items"]["letter"]["owned"] = 1
                    else:
                        printz(f"You already picked up the letter.")
                else:
                    printz(f"You dont see a letter.")
            elif target in TARGETS["starter_food"]:
                if x == 0 and y == 0:
                    if items["food"]["starter_food"]["owned"] == 0:
                        printz(f"You picked up starter food pack.")
                        items["food"]["starter_food"]["owned"] = 1
                    else:
                        printz(f"You already picked up starter food pack! Who are you trying to trick?")
                else:
                    printz(f"You dont see a starter food pack.")
            else:
                printz(f"You cant see a {target} to pick up!")

        # Reading items
        elif command in COMMANDS["read"]:
            flag = "read"
            if target in TARGETS["letter"]:
                if items["weapons_and_items"]["letter"]["owned"] == 1:
                    for f in LETTER:
                        printz(f)
                else:
                    printz(f"You cant read letter because you have not picked up letter.")
            else:
                printz(f"You cant read a "+target+"!")
        
        # Opening closed items
        elif command in COMMANDS["open"]:
            flag = "open"
            if target in TARGETS["starter_food"]:
                if items["food"]["starter_food"]["owned"] == 1:
                    printz(f"You opened starter food pack and found bottles of water, bread and 5 throwing stars. You put the water, bread and throwing stars in your inventory.")
                    items["water"]["0.5l_full_bottle"]["owned"] += 3
                    items["food"]["bread"]["owned"] += 3
                    items["weapons_and_items"]["stars"]["owned"] += 5
                    items["food"]["starter_food"]["owned"] = 0
                else:
                    printz(f"You dont have a starter food pack!")
            else:
                printz(f"You cant open a "+target+"!")
        
        # eating
        elif command in COMMANDS["eat"]:
            flag = "eat"
            if target.lower().strip() in items["food"]:
                if items["food"][target]["owned"] > 0:
                    hunger = player_stats["hunger"]
                    if items["food"][target]["value"] > 100 - hunger:
                        printz(f"Are you sure you want to eat {target}? You will waste food as it has {items["food"][target]["value"] - (100 - hunger)} hunger points more then the hunger you have.")
                        wait(2)
                        while True:
                            y_n = inputz("(y/n) >  ")
                            if y_n in COMMANDS["yes"]:
                                break
                            elif y_n in COMMANDS["no"]:
                                printz(f"You decided to not eat {target}.")
                                return x,y,flag,turns,data,enter
                            else:
                                printz(f"Invalid input: '{y_n}'. Type 'y' or 'n'.")
                    printz(f"You ate the {target} and increased your hunger by {items["food"][target]["value"]} points!")
                    player_stats["hunger"] += items["food"][target]["value"]
                    items["food"][target]["owned"] -= 1
                else:
                    printz(f"You dont have any {target} to eat!")
            else:
                printz(f"You cant eat a "+target+"!")

        # drinking
        elif command in COMMANDS["drink"]:
            flag = "drink"
            if target in TARGETS["water_bottle"]:
                drinkable = []
                for bottle_name in items["water"]:
                    bottle_data = items["water"][bottle_name]
                    if bottle_name.endswith("_full_bottle") and bottle_data.get("owned", 0) > 0 and "value" in bottle_data and "%" in bottle_data:
                        drinkable.append(bottle_name)

                if len(drinkable) == 0:
                    printz(f"You dont have any water bottles to drink from!")
                elif player_stats["thirst"] >= 100:
                    printz(f"Your not thirsty right now.")
                else:
                    printz("Choose a water bottle to drink from:")
                    for i, bottle_name in enumerate(drinkable, start=1):
                        bottle_data = items["water"][bottle_name]
                        total_ml = bottle_data["value"] * 10
                        current_ml = int((total_ml * bottle_data["%"])/100)
                        printz(f"{i}. {bottle_name} - {bottle_data['owned']} owned, {bottle_data['%']}% full ({current_ml}/{total_ml} ml).")

                    while True:
                        choice = inputz("Drink from which bottle? (number)>  ").strip()
                        try:
                            choice = int(choice)
                            if choice < 1 or choice > len(drinkable):
                                printz(f"Invalid choice. Pick a number between 1 and {len(drinkable)}.")
                                continue
                            break
                        except ValueError:
                            printz(f"Invalid input: '{choice}'. Enter a number.")

                    selected_key = drinkable[choice - 1]
                    selected = items["water"][selected_key]

                    if selected["%"] <= 0 and selected["owned"] > 0:
                        selected["%"] = 100


                    current_amount = (selected["value"] * selected["%"]) / 100
                    available_thirst = current_amount
                    missing_thirst = 100 - player_stats["thirst"]
                    gained_thirst = min(available_thirst, missing_thirst)

                    if gained_thirst <= 0:
                        printz(f"That bottle is empty.")
                    else:
                        remaining_amount = current_amount - gained_thirst
                        new_percent = (remaining_amount / selected["value"]) * 100
                        if new_percent < 0:
                            new_percent = 0
                        elif new_percent > 100:
                            new_percent = 100

                        player_stats["thirst"] += gained_thirst
                        if player_stats["thirst"] > 100:
                            player_stats["thirst"] = 100

                        if int(player_stats["thirst"]) == player_stats["thirst"]:
                            player_stats["thirst"] = int(player_stats["thirst"])

                        if int(gained_thirst) == gained_thirst:
                            gained_text = int(gained_thirst)
                        else:
                            gained_text = round(gained_thirst, 2)

                        printz(f"You drank from {selected_key} and gained {gained_text} thirst.")
                        selected["%"] = round(new_percent, 2)


                        if selected["%"] <= 0:
                            selected["owned"] -= 1
                            bottle_size = selected_key.split("_")[0]
                            empty_key = f"{bottle_size}_empty_bottle"
                            if empty_key in items["water"]:
                                items["water"][empty_key]["owned"] += 1
                            if selected["owned"] > 0:
                                selected["%"] = 100
                            else:
                                selected["%"] = 0
                            printz(f"your {selected_key} is now empty. It has been moved to {empty_key}.")
            else:
                printz(f"You cant drink a {target}!")
        
        # Fill upp water bottles
        elif command in COMMANDS["fill"]:
            flag = "fill"
            if target in TARGETS["water_bottle"]:
                i = False
                for f in items["water"]:
                    if items["water"][f]["owned"] > 0:
                        try:
                            if items["water"][f]["%"] == 0:
                                pass
                        except KeyError:
                            i = True
                if i == True:
                    i = False
                    if xy in attrdict["searched_ditch"]:
                        printz("You are filling up your water bottles in a ditch!")
                        wait(2)
                        printz("This might poison you!")
                        i = True
                    elif xy in attrdict["water_sources"]:
                        printz("You are filling upp your water bottles in clean fresh water!")
                        wait(2)
                        printz("This probably wont get poisoned")
                        i = True
                    if i == True:
                        fill()
                    else:
                        printz("You cant fill upp your water bottles here, there is no freshwater!")
                else:
                    printz(f"You dont have any {target}'s to fill up!")
            else:
                printz(f"You cant fill up a {target}!")

        # Search (area)
        elif command in COMMANDS["search"]:
            flag = "search"
            if target in TARGETS["dit"+"ch"]:
                if not attrdict["searched_ditch"].get(f"{x},{y}", False):
                    Search_ditch()
                    attrdict["searched_ditch"][f"{x},{y}"] = True
                else:
                    printz(f"You already searched the dit"+"ch here. You do not find anything new.")
            elif target in TARGETS["area"]:
                if xy not in attrdict["searched"]:
                    printz("You are searching your surrounding area.")
                    Countdown(random.randint(5,15))
                    Search()
                    attrdict["searched"].append(xy)
                else:
                    printz("You already searched this area and did not find anything new.")
            else:
                printz("You did not assign anything to search.")
        
        # move items
        elif command in COMMANDS["move"]:
            flag = "move"
            if target in TARGETS["rocks"]:
                if x == -7 and y == 1:
                    if "moved_mine_rocks" not in attrdict["attr"]:
                        if items["weapons_and_items"]["stick"]["owned"] > 0:
                            printz(f"You used stick as leverage to move the rocks.")
                            printz(f"You see an entrance to a mine.")
                            attrdict["attr"].append("moved_mine_rocks")
                        else:
                            printz(f"The rocks are too heavy to move with your bare hands. You need to find something to use as leverage.")
                    else:
                        printz(f"You already moved the rocks and revealed the mine entrance!")
                else:
                    printz(f"You dont see any rocks to move.")
            else:
                printz(f"You cant move a "+target+"! Use 'go' to travel.")
        
        # Entering places
        elif command in COMMANDS["enter"]:
            flag = "enter"
            if target in TARGETS["into_mine"]:
                if x == -7 and y == 1:
                    if "moved_mine_rocks" in attrdict["attr"]:
                        if items["weapons_and_items"]["lamp"]["owned"] == True:
                            if items["weapons_and_items"]["lamp"]["on"] == True:
                                if items["weapons_and_items"]["mine_map"]["owned"] == True:
                                    if items["weapons_and_items"]["mine_map"]["started"] == True:
                                        Mines()
                                    else:
                                        printz(f"You need to start sketching the mine map!")
                                else:
                                    printz(f"You need a mine map!")
                            else:
                                printz(f"You need to turn the lamp on.")
                        else:
                            printz(f"Its pitch black. You need a lamp.")
                    else:
                        printz(f"The entrance is blocked. You have to move the rocks.")
                else:
                    printz(f"You dont see any mines to enter.")
            else:
                printz(f"You cant enter a "+target+"!")

        # climbing
        elif command in COMMANDS["climb"]:
            flag = "climb"
            if x == -3 and y == 2:
                if target in TARGETS["tree"]:
                    printz(f"Your climbing the tall tree!")
                    wait(2)
                    printz(f"This takes time.")
                    Countdown(10)
                    printz(f"You see the top of the tree, ")
                    wait(1)
                    printz(f"But the branches are getting thinner!")
                    climb = inputz("Do you want to continue?>  ")
                    if climb in COMMANDS["yes"]:
                        printz(f"You continued climbing")
                        Countdown(10)
                        printz(f"You made it to the top of the tree and can see the whole area around you!")
                        wait(3)
                        printz(f"This would be a good place to start sketching a map of the area!")
                        attrdict["attr"].append("climbed_tree")
                        climb = inputz("Do you want to start sketching a map?>  ")
                        if climb in COMMANDS["yes"]:
                            if "started_mine_map" not in attrdict["attr"]:
                                if items["weapons_and_items"]["mine_map"]["owned"] == True:
                                    printz(f"You started sketching a map of the area.")
                                    attrdict["attr"].append("started_mine_map")
                                    wait(3)
                                    printz(f"You can now use the map to navigate the area!")
                                    wait(3)
                                    printz(f"You can also use the map to find your way in the mines!")
                                else:
                                    printz(f"You need a mine map to start sketching!")
                            else:
                                printz(f"You already started sketching a map!")
                        elif climb in COMMANDS["no"]:
                            printz(f"You decided to not sketch a map and just enjoy the view.")
                            wait(3)
                            printz(f"You climb down.")
                            Countdown(10)
                            printz(f"You climbed down the tree.")
                            wait(3)
                            printz(f"You can now continue your adventure.")
                    elif climb in COMMANDS["no"]:
                        printz(f"You decided to stop climbing and climb down.")
                        Countdown(10)
                        printz(f"Oh, no! You slipped and fell down from the tree and hit your head on a rock!.")
                        wait(3)
                        player_stats["health"] -= 20
                        printz(f"You lost 20 hp from the fall and have {player_stats['health']} hp left!")
                        if player_stats["health"] <= 0:
                            printz(f"You died from the fall!")
                            attrdict["death"][xy] = "You died by falling down from a tree."
                            Game_over()
                        else:
                            printz(f"You can now continue your adventure.")
                else:
                    printz(f"You cant climb a {target}!")
            else:
                printz(f"You dont see anything to climb here!")

        # Movement
        elif command == "go":
            flag = "go"
            if target in TARGETS["north"]:
                y += 1
            elif target in TARGETS["south"]:
                y -= 1
            elif target in TARGETS["east"]:
                x += 1
            elif target in TARGETS["west"]:
                x -= 1
            else:
                printz(f"Invalid directional command: "+target+".")
                return x,y,flag,turns,data,enter

            turns += 1

            if f"{x},{y}" not in game_board["main_board"]:
                printz(f"Cliff ahead, cant go there.")
                flag += "cliff"
                if target in TARGETS["north"]:
                    y -= 1
                elif target in TARGETS["south"]:
                    y += 1 
                elif target in TARGETS["east"]:
                    x -= 1
                elif target in TARGETS["west"]:
                    x += 1
                turns -= 1


            # mines
        
        # Mines
        elif target in TARGETS["mines"]:
                if x == -7 and y == 1:
                    if "moved_mine_rocks" in attrdict["attr"]:
                        if items["weapons_and_items"]["lamp"]["owned"] == True:
                            if items["weapons_and_items"]["lamp"]["on"] == True:
                                if items["weapons_and_items"]["mine_map"]["owned"] == True:
                                    if items["weapons_and_items"]["mine_map"]["started"] == True:
                                        Mines()
                                    else:
                                        printz(f"You need to start sketching the mine map!")
                                else:
                                    printz(f"You need a mine map!")
                            else:
                                printz(f"You need to turn the lamp off.")
                        else:
                            printz(f"Its pitch black. You need a lamp.")
                    else:
                        printz(f"The entrance is blocked. You have to move the rocks.")
                else:
                    printz(f"You dont see any mines.")  
                Turns(turns,x,y,data,username)
                x,y,lastxy,position_flag = print_position(x,y,flag,data,username)

        # Exiting and saving
        elif command in COMMANDS["exit"]:
            flag = "exit"
            exit_event.set()
            printz(user_input.replace(" ", "")+"ing")
            player_stats["play_time"] += (datetime.now() - datetime.fromisoformat(player_stats["start_time"])).total_seconds()
            data = json_pack(username,x,y)
            json_dump(data)
            wait(1)
            os._exit(0)
        
        #INFO command
        elif command in COMMANDS["info"]:
            flag = "info"
            global typespeed
            if inputz("Are you totally sure you need it?>  ") in COMMANDS["yes"]:
                print(" ")
                if inputz("Do you really want it?>  ") in COMMANDS["yes"]:
                    print(" ")
                    if inputz("Totally sure you want INFO?>  ") in COMMANDS["yes"]:
                        print(" ")
                        if inputz("Do you REEALLLY need help?>  ") in COMMANDS["yes"]:
                            print(" ")
                            if inputz("Why are you pressing yes all the time?>  ") in COMMANDS["yes"]:
                                print(" ")
                                printz(f"Fine you can have your help,")
                                wait(4)
                                if inputz("But are you totally sure?>  ") in COMMANDS["yes"]:
                                    if inputz("Quite totally sure?>  ") in COMMANDS["yes"]:
                                        print(" ")
                                        printz(f"Here comes help!")
                                        print(" ")
                                        wait(4)
                                        typespeed = 1
                                        i = 0
                                        for f in info:
                                            printz(f)

                                            if i > 0:
                                                i -= 1
                                            else:
                                                break
                                        printz(f"No thats too slow!")
                                        wait(4)
                                        printz(f"Here we go again")
                                        typespeed = 0.005
                                        i = 1
                                        for f in info:
                                            printz(f)

                                            if i > 0:
                                                i -= 1
                                            else:
                                                break
                                        wait(2)
                                        printz(f"No thats too fast.")
                                        wait(4)
                                        printz(f"Lets try one last time")
                                        typespeed = 0
                                        for f in info:
                                            printz(f)
                                        wait(2)
                                        printz(f"Now thats better!")
                                        wait(5)
                                        printz(f"Goodbye.                                                                                                                                                                                                                           ")
                                        wait(10)
                                    else:
                                        printz(f"Okay, its your loss!")
                                else:
                                    printz(f"Okay, its your loss!")
                            else:
                                printz(f"Okay, its your loss!")
                        else:
                            printz(f"Okay, its your loss!")
                    else:
                        printz(f"Okay, its your loss!")
                else:
                    printz(f"Okay, its your loss!")
            else:
                printz(f"Okay, its your loss!")
                
        # INVENTORY command
        elif user_input in COMMANDS["inventory"]:
            flag = "inventory"
            check = ""
            for f in items:
                for d in items[f]:
                    if items[f][d]["owned"] > 0:
                        print(" ")
                        printz(d.upper()+" STATS: ")
                        for c in items[f][d]:
                            printz(str(c)+": "+str(items[f][d][c]))
                            check += str(c)
            if check == "":
                printz(f"your inventory is empty!") 

        # WEAPONS command
        elif user_input in COMMANDS["weapons"]:
            flag = "weapons"
            check = ""
            weapons = items["weapons_and_items"]
            for f in weapons:
                if weapons[f]["owned"] > 0:
                    print(" ")
                    printz(f.upper()+" STATS: ")
                    for d in weapons[f]:
                        printz(str(d)+": "+str(weapons[f][d]))
                        check += str(d)
            if check == "":
                printz(f"You dont have any weapons!")

        # FOOD command
        elif user_input in COMMANDS["food"]:
            flag = "food"
            check = ""
            food = items["food"]
            for f in food:
                if food[f]["owned"] > 0:
                    print(" ")
                    printz(f.upper()+" STATS: ")
                    for d in food[f]:
                        printz(str(d)+": "+str(food[f][d]))
                        check += str(d)
            if check == "":
                printz(f"You dont have any food!")

        # WATER command
        elif user_input in COMMANDS["water"]:
            flag = "water"
            check = ""
            water = items["water"]
            for f in water:
                if water[f]["owned"] > 0:
                    print(" ")                    
                    printz(f.upper()+" STATS: ")
                    for d in water[f]:
                        printz(str(d)+": "+str(water[f][d]))
                        check += str(d)
            if check == "":
                printz(f"You dont have any water!")
        
        # STATS command
        elif user_input in COMMANDS["stats"]:
            flag = "stats"
            player_stats["play_time"] += (datetime.now() - datetime.fromisoformat(attrdict["divide_time"])).total_seconds()
            printz(f"Player stats: ")
            print(" ")
            for f in player_stats:
                if f == "play_time":
                    printz(f"play time(s): "+str(player_stats[f].__int__()))
                elif f == "start_time":
                    printz(f"current run start time: "+timez(player_stats[f]))
                else:
                    printz(f+": "+str(player_stats[f]))
            attrdict["divide_time"] = datetime.now().isoformat()
        
        # DEATHS command
        elif user_input in COMMANDS["deaths"]:
            flag = "deaths"
            printz("This is a list of all the ways you have died.")
            print(" ")
            printz("You have:")
            for xy in attrdict["death"]:
                print(" ")
                printz(attrdict["death"][xy][4:])
            if len(attrdict["death"]) == 0:
                printz("You have not died yet!")

        # Admin
        elif command in COMMANDS["admin"]:
            FUNCTIONS = {
                "search_ditch": Search_ditch,
                "angry_farmer": angry_farmer,
                "fight": FIGHT,
                "run": RUN,
                "countdown": Countdown,
                "printz": printz,
                "bold": bold,
                "timez": timez,
                "inputz": inputz,
                "game_over": Game_over,
                "mines": Mines
            }
            flag = "admin"

            if "admin" not in attrdict["attr"]:
                printz(f"You don't have admin privileges! Who are you trying to trick?")
                return x,y,flag,turns,data,enter
            
            admin_inputz = inputz("Admin > ").lower().strip()
            if not admin_inputz:
                printz(f"You entered an empty command. Please enter a valid admin command.")
                print("Available admin commands: xy, items, debug, run, toggle countdown (tc)")
                return x,y,flag,turns,data,enter

            admin_input = admin_inputz.split(",")


            if admin_input[0] == "xy":
                if len(admin_input) == 1:
                    print(f"({x},{y})")
                elif len(admin_input) == 3:
                    try:
                        x = int(admin_input[1])
                        print(f"Successfully assigned '{admin_input[1]}' to x.")
                    except ValueError:
                        print(f"Could not assign '{admin_input[1]}' to x")
                    try:
                        y = int(admin_input[2])
                        print(f"Successfully assigned '{admin_input[2]}' to y.")
                    except ValueError:
                        print(f"Could not assign '{admin_input[2]}' to y")
                    x, y, lastxy, position_flag = print_position(x, y, "none", data, username)
                    if position_flag:
                        print(f"({x},{y})")
                else:
                    print("Invalid input for xy. Usage: xy (to print) or xy,x_value,y_value (to assign)")


            elif admin_input[0] == "items":
                itemsz = items  
                length = len(admin_input)

                if length == 1:
                    print("You did not assign a target for items")
                    print("Usage: items, item_name, item_stat, value")
                    print(itemsz)
                elif length == 2:
                    print(f"KeyError line() {line()}: {itemsz.get(admin_input[1])}")
                elif length == 3:
                    target = itemsz.get(admin_input[1])
                    if target is None:
                        print(f"KeyError line() {line()}: {admin_input[1]}")
                    else:
                        print(target.get(admin_input[2], f"KeyError line() {line()}: {admin_input[2]}"))
                elif length == 4:
                    val = admin_input[3].lower()
                    if val == "true":
                        val = True
                    elif val == "false":
                        val = False
                    else:
                        try:
                            val = int(admin_input[3])
                        except ValueError:
                            pass
                    print(val)
                    try:
                        itemsz[admin_input[1]][admin_input[2]] = val
                        print(itemsz[admin_input[1]])
                    except KeyError:
                        print(f"KeyError line() {line()}: Failed to assign {val} to {admin_input[1]},{admin_input[2]}")


            elif admin_input[0] == "debug":
                COM = []
                for command_key, aliases in COMMANDS.items():
                    if command_key not in ("exit", "admin"):
                        COM.extend(aliases)
                print(",".join(COM))


            elif admin_input[0] == "run":
                if len(admin_input) == 1:
                    print("You did not assign a function to run.")
                    print("Usage: run,function_name,arg1,arg2,...")
                    print("Available functions:", ", ".join(FUNCTIONS.keys()))
                else:
                    func_name = admin_input[1]
                    func = FUNCTIONS.get(func_name)
                    if not func:
                        print(f"Function '{func_name}' does not exist. Available functions:", ", ".join(FUNCTIONS.keys()))
                    else:

                        params = inspect.signature(func).parameters
                        param_names = list(params.keys())
                        print(f"Function '{func_name}' requires parameters:", ", ".join(param_names))

                        given_args = admin_input[2:]
                        if len(given_args) != len(param_names):
                            print(f"Incorrect number of arguments. Expected {len(param_names)}, got {len(given_args)}")
                        else:
                            try:
                                func(*given_args)
                            except Exception as e:
                                print(f"Error running '{func_name}': {e} on line() {line()}")


            elif admin_input[0] in ("toggle countdown", "tc", "ct"):
                if "countdown" in attrdict["attr"]:
                    attrdict["attr"].remove("countdown")
                    print("Countdown toggled on.")
                else:
                    attrdict["attr"].append("countdown")
                    print("Countdown toggled off.")

            
            elif admin_input[0] in ("toggle printz", "tp", "pt"):
                if "no_printz" in attrdict["attr"]:
                    attrdict["attr"].remove("no_printz")
                    print("printz toggled on.")
                else:
                    attrdict["attr"].append("no_printz")
                    print("printz toggled off.")


            elif admin_input[0] == "fight":
                c = cricket_storm()
                FIGHT(c)


            else:
                print(f"Input '{admin_inputz}' is not a valid admin command.")
                print("Available admin commands: xy, items, debug, run, toggle countdown (tc)")

        # Admin command to toggle countdown on and off
        elif command in COMMANDS["adminmode"]:
            flag = "adminmode"
            if "admin" in attrdict["attr"] or "a" in attrdict["attr"]:
                while True:
                    on_off_admin = inputz("Turn admin mode on or off? (on/off)>  ")
                    if on_off_admin in COMMANDS["off"]:
                        if "a" not in attrdict["attr"]:
                            attrdict["attr"].append("a")
                            attrdict["attr"].remove("admin")
                            printz(f"Admin mode turned off!")
                            break
                        else:
                            printz(f"Admin mode is already off!")
                            break
                    elif on_off_admin in COMMANDS["on"]:
                        if "a" in attrdict["attr"]:
                            attrdict["attr"].remove("a")
                            attrdict["attr"].append("admin")
                            printz(f"Admin mode turned on!")
                            break
                        else:
                            printz(f"Admin mode is already on!")
                            break
                    else:
                        printz(f"Invalid input. Please enter 'on' or 'off'.")
                        continue
            else:
                printz(f"You don't have admin privileges! Who are you trying to trick?")

        # Delete acount
        elif command in COMMANDS["delete"]:
            flag = "delete"
            while True:
                delete = inputz("Delete acount? (y/n)>  ")
                if delete in COMMANDS["yes"]:
                    del data[username]
                    printz(f"your acount has been deleted.")
                    printz(f"Exiting...")
                    json_dump(data)
                    exit_event.set()
                    os._exit(0)
                elif delete in COMMANDS["no"]:
                    printz(f"You decided not to delete your acount.")
                    break
                else:
                    printz(f"Invalid input. Please enter 'y' or 'n'.")
                    continue
                
        # Punishing people who press enter without any context
        elif user_input == "":
            flag = "enter"
            if enter > 8:
                printz(f"Thu shall not press enter for "+str(enter)+" seconds")
            elif enter < 8:
                printz(f"Thu press enter on me. Thu wait "+str(enter)+" seconds.")
            elif enter == 8:
                printz(f"You press enter 4 times! You die.")
                wait(4)
                printz(f"your user has been deleted.")
                wait(3)
                printz(f"Dont press enter next time!")
                printz(f"Exiting...")
                total = 0
                start = time.perf_counter()
                print(COLORS["reset"])
                while total < 20:
                    trick = input("zackary@Zackarys-MacBook-Air Python_test % ")
                    total = time.perf_counter() - start
                print(COLORS["prompt"])
                print(" ")
                printz(f"Ha ha, you fell for it didn't you!")
                wait(2)
                printz(f"your user has not been deleted.")
                while True:
                    scared = input("Did i scare you? (y/n)>  ").lower().replace(" ","")
                    if scared in COMMANDS["yes"]:
                        achieved.append("Scardycat")
                        printz(f"You got achievement 'Scardycat'")
                        break
                    if scared in COMMANDS["no"]:
                        achieved.append("Enter dumb")
                        printz(f"You got achievement 'Enter dumb'")
                        break
                printz(f"Wait "+str(enter)+" seconds.")
            Countdown(enter)
            enter += 1
        
        # smart statements
        elif flag == None:
            flag = respond_if_match(user_input.lower(),flag)

        # Invalid operation detection
        if flag == None:
            i = random.randint(0,len(RANDOM_FEEDBACK)-1)
            printz(RANDOM_FEEDBACK[i])

        return x,y,flag,turns,data,enter
        
def print_position(x,y,flag,data,username):
        global trespass
        global lastxy

        xy = f"{x},{y}"

        try:
            if attrdict["barn"] == True:
                position = game_board["barn_board"][xy]
            else:
                position = game_board["main_board"][xy]
        except KeyError:
            print(f"{xy} is not on the game board!")
            x,y = int(lastxy.split(",")[0]),int(lastxy.split(",")[1])
            return x,y,lastxy,False
        
        # enemy spawn?
        if position[0:6] == "Fields":
            if player_stats["xp"]["total"] > random.uniform(ENEMY_SPAWN_CHANCE["fields"][0],ENEMY_SPAWN_CHANCE["fields"][1]):
                FIGHT(cricket_storm())

        elif position[0:6] == "Forest":
            if player_stats["xp"]["total"] > random.uniform(ENEMY_SPAWN_CHANCE["forest"][0],ENEMY_SPAWN_CHANCE["forest"][1]):
                FIGHT(goblin())
        
        elif position[0:5] == "Dense":
            if player_stats["xp"]["total"] > random.uniform(ENEMY_SPAWN_CHANCE["dense_forest"][0],ENEMY_SPAWN_CHANCE["dense_forest"][1]):
                FIGHT(forest_troll())

        elif position[0:6] == "Valley" or position[0:8] == "Mountain":
            if player_stats["xp"]["total"] > random.uniform(ENEMY_SPAWN_CHANCE["valley_and_hills"][0],ENEMY_SPAWN_CHANCE["valley_and_hills"][1]):
                FIGHT(yeti())
        
        elif position[0:5] == "Rocky":
            if player_stats["xp"]["total"] > random.uniform(ENEMY_SPAWN_CHANCE["rocky_area"][0],ENEMY_SPAWN_CHANCE["rocky_area"][1]):
                FIGHT(giant_snake())
        
        elif position[0:6] == "Plains":
            if player_stats["xp"]["total"] > random.uniform(ENEMY_SPAWN_CHANCE["plains"][0],ENEMY_SPAWN_CHANCE["plains"][1]):
                FIGHT(dragon_boss())
        
        elif position[0:4] == "Road":
            if player_stats["xp"]["total"] > random.uniform(ENEMY_SPAWN_CHANCE["road"][0],ENEMY_SPAWN_CHANCE["road"][1]):
                FIGHT(giant_spider())
        
        if "cant_move" in attrdict["attr"]:
            printz(f"Your unable to move because of hunger.")
            printz(position)
            return x,y,lastxy,True
        
        elif "move_slowly" in attrdict["attr"]:
            printz(f"Your moving slowly because of hunger.")
            wait(2)
            printz(f"Wait until the countdown finishes.")
            i = random.randint(10,20)
            Countdown(i)



        if position[16:21] == "dit"+"ch":
            printz(f"You are walking back out of the slippery dit"+"ch. This takes time!")
            wait(2)
            printz(f"Wait until the countdown finishes.")
            i = random.randint(10,20)
            Countdown(i)

        elif position[0:5] == "Dense":
            printz(f"You are walking through dense forest. Doing this takes time.")
            wait(2)
            printz(f"Wait until the countdown finishes.")
            i = random.randint(5,15)
            Countdown(i)

        elif position[13:25] == "bushwhacking":
            crop = "crop"
            if position[34:36] == "Co":
                crop = "corn"
            elif position[34:36] == "Ca":
                crop = "canola"
            elif position[34:36] == "Wh":
                crop = "wheat"
            elif position[34:36] == "Ba":
                crop = "barley"
            elif position[34:36] == "Ri":
                crop = "rice"
            trespass += 1
            i = random.randint(2,6)
            if i < trespass:
                trespass = 0
                x,y = angry_farmer(crop,data,username,x,y)
        
        if "blind" not in attrdict["attr"]:
            if xy == "-4,6":
                while True:
                    printz(f"You see a tall mountain in front of you. It is called mount Zarckmore.")
                    wait(2)
                    printz(f"You are at the base of the trail that leads to the top of the mountain.")
                    wait(2)
                    print(" ")
                    printz(f"Do you want to climb mount Zarckmore?")
                    climb = inputz("Climbing mountains is a tedious dangerous thing in this game! (y/n) >  ")
                    if climb in COMMANDS["yes"]:
                        print(" ")
                        printz(f"You decided to climb the mountain.")
                        wait(2)
                        print(" ")
                        printz(f"You started hiking.")
                        Countdown(10)
                        printz(f"You cant see where the path goes anymore because it very worn down.")
                        print(" ")
                        wait(2)
                        while True:
                            climb = inputz("left or right? > ")
                            if climb in COMMANDS["left"]:
                                printz(f"You decided to walk left.")
                                print(" ")
                                wait(2)
                                printz(f"The path leads you through a thick mist.")
                                Countdown(10)
                                print(" ")
                                printz(f"You still cant see anything from the mist.")
                                wait(2)
                                print(" ")
                                printz(f"Oh, no. You did not see the ledge in the mist and fell down 10 meters.")
                                wait(2)
                                printz(f"You are unable to move your legs, but wait for the mist to go away.")
                                Countdown(15)
                                print(" ")
                                printz(f"You died from infection in your legs.")
                                printz(f"Dont fall off the ledge next time!")
                                attrdict["death"][xy] = "You died from infection in your legs."
                                Game_over()
                            elif climb in COMMANDS["right"]:
                                printz(f"You decided to go right.")
                                Countdown(10)
                                print(" ")
                                printz(f"It has started raining!")
                                Countdown(5)
                                print(" ")
                                printz(f"The rain has made it impossible to see anything.")
                                wait(2)
                                print(" ")
                                printz(f"You cant see where the trail goes!")
                                print(" ")
                                while True:
                                    climb = inputz("left or right? >  ")
                                    if climb in COMMANDS["left"]:
                                        printz(f"You decided to go left.")
                                        print(" ")
                                        Countdown(10)
                                        printz(f"The rain has just gotten heavier! You are drenched")
                                        wait(3)
                                        print(" ")
                                        printz(f"Large streams are flowing down the mountain.")
                                        wait(2)
                                        print(" ")
                                        printz(f"Oh, no. The water has loosened some rocks over you!")
                                        wait(2)
                                        print(" ")
                                        printz(f"They come down in a large rockslide!")
                                        wait(2)
                                        print(" ")
                                        printz(f"You get caught in the rocks and get buried!")
                                        wait(2)
                                        print(" ")
                                        printz(f"You died by rockslide!")
                                        print(" ")
                                        attrdict["death"][xy] = "You died by a rockslide, but hey you got a burial to be proud of!"
                                        Game_over()
                                    elif climb in COMMANDS["right"]:
                                        printz(f"You decided to go right.")
                                        print(" ")
                                        Countdown(10)
                                        printz(f"The rain has stopped!")
                                        wait(2)
                                        print(" ")
                                        printz(f"The mist has cleared up!")
                                        wait(2)
                                        printz(f"You see the top of the mountain!")
                                        wait(2)
                                        print(" ")
                                        printz(f"You made it to the top of the mountain and can see the whole area around you!")
                                        wait(3)
                                        print(" ")
                                        printz(f"You also find a skeleton of a hiker who did not make it to the top. You search through his belongings and find a kerosene lamp.")
                                        items["weapons_and_items"]["lamp"]["owned"] = 1
                                        wait(3)
                                        print(" ")
                                        printz(f"You can now use the lamp to see in dark places.")
                                        wait(3)
                                        printz(f"You climb back down the mountain.")
                                        Countdown(30)
                                        print(" ")
                                        printz(f"You climbed down the mountain.")
                                    else:
                                        printz(f"Thats not a valid command.")
                                        print(" ")
                                        continue
                            else:
                                printz(f"Thats not a valid command.")
                                print(" ")
                                continue

                    elif climb in COMMANDS["no"]:
                        printz(f"You decided not to climb the mountain.")
                        xy = lastxy
                        break

                    else:
                        printz(f"Thats not a valid command.")
                        continue
            if xy in attrdict["death"]:
                printz(f"Here {attrdict["death"][xy].lower()}")
                print(" ")

            if position[0:5] not in attrdict["attr"]:
                attrdict["attr"].append(position[0:5])
                position = bold(position)
            else:
                position = position

            if flag[2:] != "cliff":
                if "admin" in attrdict["attr"]:
                    printz(f"You are at '"+position+"' ("+xy+")")
                else:
                    print(" ")
                    if xy == "-7,1" and "moved_mine_rocks" not in attrdict["attr"]:
                        printz("You are standing in a clearing with woods all around. In front of you is a hole going down into the ground supported by wooden beams.")
                    else:
                        printz(position)
        else:
            printz(f"You can't see anything because of dehydration. This also slows you down a lot.")
            wait(2)
            printz(f"Wait until the countdown finishes.")
            i = random.randint(20,40)
            Countdown(i)

        x,y = int(xy.split(",")[0]),int(xy.split(",")[1])
        lastxy = xy

        return x,y,lastxy,True

def parser(constants):
        return sorted(constants, key=len, reverse=True)

def parse_command_fragment(fragment):
        text = fragment.strip().lower()
        for command_key, aliases in COMMANDS.items():
            for alias in sorted(aliases, key=len, reverse=True):
                alias_text = alias.strip().lower()
                if text == alias_text:
                    return command_key, ""
                if text.startswith(alias_text + " "):
                    return command_key, text[len(alias_text):].strip()
        return None, None

def Start_game(data,x,y,wait,typespeed,lastxy,player_stats,achieved,attrdict,items,trespass):
    global turns
    global enter


    json_dump(data)
    x,y,lastxy,position_flag = print_position(x,y,"none",data,username)


    while True:
        # formatting
        print(" ")
        print(" ")

        # get input
        raw_input = inputz(">  ").strip()
        print(" ")

        # format input and parse command
        flag = False
        for f in raw_input:
            if f.upper() != f:
                user_input = raw_input
                flag = True
                break
        if flag == False:
            user_input = raw_input.lower()
        user_input = user_input.split(",")
        command = None
        target = None
        for f in user_input:
            command, target = parse_command_fragment(f)
            x,y,flag,turns,data,enter = check_operations(command,target,f,raw_input,x,y,turns,username,data,enter)
        
        # update xp
        Update()

        # save after every command
        data = json_pack(username,x,y,)
        json_dump(data)

def Tick_update():
    gtick = {"tick": 0,"exit": False}
    wtick = 0
    SAFE_GUARD = 3
    W_TICK_FILE = "wtick.json"
    G_TICK_FILE = "gtick.json"
    last = 0
    current = 0
    s = SAFE_GUARD
    save_key = "save_key_"
    key_len = 30
    while True:

        # check if game wants to exit
        if exit_event.is_set():
            gtick["exit"] = True
            with open(G_TICK_FILE, "w") as f:
                json.dump(gtick, f)
        
        # update game alive
        gtick["tick"] += 1

        # dump tick
        with open(G_TICK_FILE, "w") as f:
            json.dump(gtick, f)

        # get updated tick 
        try:
            with open(W_TICK_FILE,"r") as f:
                wtick = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            wtick = 0
        current = wtick

        # check watcher alive
        if current == last:
            s -= 1
        else:
            s = SAFE_GUARD

        if s < 1:
            for f in range(key_len):
                save_key += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
            print(f"Error line() {line()}: Game terminated without reason. Use the following save key to restore your account: {save_key}")

            data = json_load()
            if username in data:
                if "admin" in data[username]["attrdict"]["attr"]:
                    print("As an admin you have been spared from the punishment of having your acount reset. If you read this message, a problem with the watcher has occurred. Please report this to the creator of the game so it can be fixed. Thank you!")
                    os._exit(0)
                # save acount if watcher terminates game without reason
                data[username]["save_key"] = {"key":save_key,"data":data[username].copy()}
                # reset
                data[username]["x"] = 0
                data[username]["y"] = 0
                data[username]["items"] = base_items
                data[username]["lastxy"] = "0,0"
                data[username]["player_stats"]["health"] = 100
                data[username]["player_stats"]["attack"] = 15
                data[username]["player_stats"]["strength"] = 15
                data[username]["player_stats"]["defense"] = 10
                data[username]["attrdict"]["attr"].append("reset1")
            else:
                print(f"Error line() {line()}: Could not reset account because account does not exist.")
                os._exit(0)
            json_dump(data)
            os._exit(0)

        last = current
        time.sleep(1)

def Update():
    xy = f"{x},{y}"
    ## XP ##

    # time xp
    xp = player_stats["xp"]
    player_stats["play_time"] += (datetime.now() - datetime.fromisoformat(attrdict["divide_time"])).total_seconds()
    attrdict["divide_time"] = datetime.now().isoformat()
    xp["play_time"] = int(player_stats["play_time"]//10)

    # turns xp
    xp["turns"] = turns

    # total xp
    xp["total"] = 0
    for f in xp:
        xp["total"] += int(xp[f])
    
    player_stats["xp"] = xp
    
    ## FOOD AND WATER ##

    # food
    player_stats["hunger"] -= 100 // 21

    # water
    player_stats["thirst"] -= 100 // 16

    # Check hunger

    if player_stats["hunger"] <= 0:
        print(" ")
        printz("You died of hunger!")
        attrdict["death"][xy] = "You died of hunger."
        Game_over()
    elif player_stats["hunger"] <= 10:
        print(" ")
        printz("You are extremely hungry and can not move!")
        attrdict["attr"].append("cant_move")
    elif player_stats["hunger"] <= 20:
        print(" ")
        printz("You are very hungry and start to move slower because of it.")
        attrdict["attr"].append("move_slowly")
        try:
            attrdict["attr"].remove("cant_move")
            printz("You are not extremely hungry anymore and can now move again (but only slowly).")
            while True:
                attrdict["attr"].remove("cant_move")
        except ValueError:
            pass
    elif player_stats["hunger"] <= 30:
        print(" ")
        printz("You are very hungry.")
        try:
            attrdict["attr"].remove("cant_move")
            printz("You are not extremely hungry anymore and can now move again.")
            while True:
                attrdict["attr"].remove("cant_move")
        except ValueError:
            pass
        try:
            attrdict["attr"].remove("move_slowly")
            printz("You are not very hungry anymore and can now move at normal speed again.")
            while True:
                attrdict["attr"].remove("move_slowly")
        except ValueError:
            pass
    elif player_stats["hunger"] <= 50:
        print(" ")
        printz("You are starting to get hungry.")
        try:
            attrdict["attr"].remove("cant_move")
            printz("You are not extremely hungry anymore and can now move again.")
            while True:
                attrdict["attr"].remove("cant_move")
        except ValueError:
            pass
        try:
            attrdict["attr"].remove("move_slowly")
            printz("You are not very hungry anymore and can now move at normal speed again.")
            while True:
                attrdict["attr"].remove("move_slowly")
        except ValueError:
            pass
    else:
        try:
            attrdict["attr"].remove("cant_move")
            printz("You are not extremely hungry anymore and can now move again.")
            while True:
                attrdict["attr"].remove("cant_move")
        except ValueError:
            pass
        try:
            attrdict["attr"].remove("move_slowly")
            printz("You are not very hungry anymore and can now move at normal speed again.")
            while True:
                attrdict["attr"].remove("move_slowly")
        except ValueError:
            pass

    
    # Check thirst
    if player_stats["thirst"] <= 0:
        printz("You died of dehydration!")
        attrdict["death"][xy] = "You died of dehydration"
        Game_over()
    elif player_stats["thirst"] <= 15:
        printz("You are so extremely dehydrated you lost your sight!")
        attrdict["attr"].append("blind")
    elif player_stats["thirst"] <= 25:
        printz("You are very dehydrated and start to lose your sight because of it.")
        try:
            attrdict["attr"].remove("blind")
            printz("You are not extremely dehydrated anymore and can now see again.")
            while True:
                attrdict["attr"].remove("blind")
        except ValueError:
            pass
    elif player_stats["thirst"] <= 35:
        printz("You are very dehydrated. Make sure to drink water soon!")
        try:
            attrdict["attr"].remove("blind")
            printz("You are not extremely dehydrated anymore and can now see again.")
            while True:
                attrdict["attr"].remove("blind")
        except ValueError:
            pass
    elif player_stats["thirst"] <= 50:
        printz("You are starting to get dehydrated. Make sure to drink water soon!")
        try:
            attrdict["attr"].remove("blind")
            printz("You are not extremely dehydrated anymore and can now see again.")
            while True:
                attrdict["attr"].remove("blind")
        except ValueError:
            pass
    else:
        try:
            attrdict["attr"].remove("blind")
            printz("You are not extremely dehydrated anymore and can now see again.")
            while True:
                attrdict["attr"].remove("blind")
        except ValueError:
            pass
    
    # update health
    if player_stats["thirst"] >= 60 and player_stats["hunger"] >= 60:
        player_stats["health"] += 15
        
    if player_stats["health"] > 100:
        player_stats["health"] = 100

    if player_stats["hunger"] > 100:
        player_stats["hunger"] = 100
    
    if player_stats["thirst"] > 100:
        player_stats["thirst"] = 100
    

print(COLORS["prompt"])

COMMAND = []

for f in COMMANDS:
    COMMAND.append(COMMANDS[f])

    COMMAND = parser(COMMAND)

print("Checking game board...")

data = json_load() or {}

# Login or create user
while True:
    loginorcreate = inputz("Do you have a user? (y/n)>  ").lower().replace(" ","")
        

    if loginorcreate in COMMANDS["yes"]:
        username = inputz("Type your username: ").lower().replace(" ","")
        if username in data:
            password = inputz("Type your password: ").lower().replace(" ","")
            if data[username]["password"] != password:
                print("Incorrect password for user",username)
                continue
            elif data[username]["password"] == password:
                if "reset1" in data[username]["attrdict"]["attr"]:
                    print(" ")
                    printz(f"Not so much welcome back you dirty little cheater! your acount has been reset as a punishment for trying to cheat by terminating the watcher! Did you really think you could get away with it? You should be ashamed of yourself! Dont do it again, i will not allow it!")
                    del data[username]["attrdict"]["attr"][data[username]["attrdict"]["attr"].index("reset1")]
                elif "reset2" in data[username]["attrdict"]["attr"]:
                    print(" ")
                    printz(f"You terminated your terminal without using the proper exit command! I am sorry but your acount has been reset because of it. Make sure you dont do it again!")
                    del data[username]["attrdict"]["attr"][data[username]["attrdict"]["attr"].index("reset2")]
                if username == "z":
                    print(" ")
                    printz(f"Welcome back Zackary!")
                    print(" ")
                    attrdict["attr"].append("admin")
                elif username == "ois":
                    attrdict["attr"].append("a")
                    print(" ")
                    printz(f"Welcome back to Zarckary "+str(username))
                else:
                    print(" ")
                    printz(f"Welcome back to Zarckary "+str(username))
                x, y, items, achieved, turns, trespass, player_stats,lastxy,attrdict = json_unpack(username, data)
                attrdict["divide_time"] = datetime.now().isoformat()                 
                break
            else:
                print("Wrong password for user",username)
                continue
        else:
            print(f"Username '{username}' does not exist.")
            continue
    if loginorcreate in COMMANDS["no"]:
        username = inputz("Type a username: ").lower().replace(" ","")
        if username not in data:
            password = inputz("Type a password: ").lower().replace(" ","")
            attrdict["attr"] = []
            if username == "z":
                    attrdict["attr"].append("admin")
                    print(" ")
                    printz(f"Welcome back, Zackary! As the creator of this game you have admin privileges. Type 'a' to access admin commands.")
                    print(" ")
            elif username == "ois":
                    attrdict["attr"].append("a")
            print(" ")
            printz(f"IMPORTANT - turning off terminal without using the proper exit command will delete your acount!")
            print(" ")
            printz(f"Your standing on a road, with a forest to the west and fields to the east.")
            printz(f"The road bends a few kilometers ahead. Beside lies a lake that is partially obscured by a hill.")
            printz(f"The dit"+"ch on the side of the road is very wet and muddy.")
            print(" ")
            printz(f"A car drives past and a letter tied to a starter food pack flies off and lands by your feet.")
            printz(f"On the letter it says 'Welcome to Zarckary'.")
            print(" ") 
            player_stats["start_time"] = datetime.now().isoformat()
            attrdict["divide_time"] = datetime.now().isoformat()
            data[username] = {"password": password, "x": x, "y": y, "items": items, "achieved": achieved,"turns":turns,"trespass":trespass,"player_stats":player_stats,"lastxy":lastxy,"attrdict":attrdict}
            break
        else:
            printz(f"Username "+username+" already exist!")
    else:
        print("Invalid input, type yes or no")


LETTER = ["IMPORTANT - turning off terminal without using the proper exit command will delete your acount!"," ","Welcome to Zarckary " + username + "! a insanely irritating version of Zork."," ","Firstly some background information. Zarckary is a spinoff from zork.","Up through the times it has gone all the way from its original name 'Zark',","to Zarck and eventually to Zarckary because of some amazing input from my mom.","As this is a spinoff from Zork i have to name the original creators of Zork,","so a big thanks to Tim Anderson, Marc Blank, Bruce Daniels, and Dave Lebling. Back to the explanation"," ","I can guarantee that you will get VERY ANNOYED!","Programmed by Zackary."," "," ","A mysterious text-based adventure awaits you...", "Navigate the world using directional commands and explore what lies beyond.", "Be careful where you venture - not all places are welcoming to travelers.", "", "Pay close attention to you are surroundings and the descriptions of each location.", "They often hold clues about what dangers or treasures await nearby.", "Some discoveries can only be made through careful exploration and experimentation.", "", "The world is full of surprises - dense forests hide secrets, abandoned structures conceal mysteries.", "Rumors speak of old mines deep within the mountains and woods where forgotten treasures may still rest.", "But venture there at you are own peril - danger lurks in the darkness below.", "", "you are actions have consequences - choose wisely and think before you act!", "If you find you areself in a difficult situation, stay calm and remember: quick reflexes can save you are life.", "", "Secrets are hidden throughout the game - will you find them all?", "Good luck, adventurer. May you are journey through Zarckary be memorable and brave..."," "]


# Start alive
thread = threading.Thread(target=Tick_update, daemon=True)
thread.start()


# Start watcher separate
watcher_script = os.path.join(os.path.dirname(os.path.abspath(__file__)), "zarckary_watcher.py")
subprocess.Popen(
    [sys.executable, watcher_script, username, "1" if JSON_ENCODED else "0"],
    start_new_session=True,
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL,
    stdin=subprocess.DEVNULL
)

# Start the game
Start_game(data,x,y,wait,typespeed,lastxy,player_stats,achieved,attrdict,items,trespass)
