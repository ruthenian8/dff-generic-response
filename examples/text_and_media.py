#!/usr/bin/env python3

from df_engine.core.keywords import RESPONSE, TRANSITIONS, GLOBAL
from df_engine.core import Context, Actor
from df_engine import conditions as cnd

from dff_generics.dff_generics import Attachments, Image, Response


plot = {
    GLOBAL: {TRANSITIONS: {("pics", "ask_picture"): cnd.true()}},
    "root": {
        "start": {RESPONSE: "", TRANSITIONS: {("pics", "ask_picture"): cnd.true()}},
        "fallback": {
            RESPONSE: "Final node reached, send any message to restart.",
            TRANSITIONS: {("pics", "ask_picture"): cnd.true()},
        },
    },
    "pics": {
        "ask_picture": {
            RESPONSE: "Send me a picture",
            TRANSITIONS: {
                ("pics", "send_one", 1.1): cnd.regexp("^http.+\.png$"),
                ("pics", "send_many", 1.0): cnd.regexp("^http.+\.jpg$"),
                ("pics", "repeat", 0.9): cnd.true(),
            },
        },
        "send_one": {
            RESPONSE: Response(text="here's my picture!", image=Image(source="examples/kitten.jpg")),
            TRANSITIONS: {("root", "fallback"): cnd.true()},
        },
        "send_many": {
            RESPONSE: Response(text="Look at my pictures", gallery=Attachments(files=["examples/kitten.jpg"] * 10)),
            TRANSITIONS: {("root", "fallback"): cnd.true()},
        },
        "repeat": {
            RESPONSE: "I cannot find the picture. Please, try again.",
            TRANSITIONS: {
                ("pics", "send_one", 1.1): cnd.regexp("^http.+\.png$"),
                ("pics", "send_many", 1.0): cnd.regexp("^http.+\.jpg$"),
                ("pics", "repeat", 0.9): cnd.true(),
            },
        },
    },
}

actor = Actor(plot=plot)
