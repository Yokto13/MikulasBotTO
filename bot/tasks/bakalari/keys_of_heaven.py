"""
Whatever you bind on earth shall be bound in heaven, and whatever you
loose on earth shall be loosed in heaven.

Matthew 16:19

And as the keys of heaven give saint Peter the power to bind the
godly with our world this script allows him to bind the powers of
Bakalari with ordinary men using the MikulasBot.

Kudos to the mighty and powerfull Adamator for providing as with an
amazing script to communicate with Bakalari.
"""

import json
from os.path import join as join_path
from posixpath import join as join_url
from shutil import copyfileobj
from typing import List, NamedTuple
import requests
import re
from dateutil.parser import parse as parse_datetime
from datetime import datetime
from .mark import Mark
from .message import Message


website = "https://bakalari.mikulasske.cz/"


def get_access_token(username: str, password: str) -> str:
    """ 
    Returns string that can be used as an access token for the user
    with the given credentials.
    """
    response = requests.post(
            join_url(website, "api/login"),
            data={
                "client_id": "ANDR",
                "grant_type": "password",
                "username": username,
                "password": password
            },
        )
    data = json.loads(response.text)
    try:
        data["access_token"]
    except KeyError:
        return None
    if token_valid(data["access_token"]):
        return data["access_token"]
    return None


def _days_difference_ok(ts1, ts2, n_of_days):
    return ((ts1 - ts2) / 3600 / 24) <= n_of_days


def get_marks(access_token: str, number_of_days: int = 7):
    """
    Returns list of marks (Mark objects) that are not older than the
    number of days.
    """
    response = requests.get(
            join_url(website, "api/3/marks"),
            headers={"Authorization": f"Bearer {access_token}"},
        )
    data = json.loads(response.text)
    current = datetime.now()
    current = datetime.timestamp(current)
    return [
            Mark(
                subject=subject["Subject"]["Name"],
                value=mark["MarkText"],
                weight=mark["Weight"],
                type_=mark["TypeNote"],
                caption=mark["Caption"],
                time_added=parse_datetime(mark["EditDate"]).timestamp(),
            )
            for subject in data["Subjects"] 
            for mark in subject["Marks"] 
            if _days_difference_ok(
                current,parse_datetime(mark["EditDate"]).timestamp(),number_of_days
                )
        ]


def timestamp_to_datetime(ts):
    return datetime.fromtimestamp(ts)


def _remove_html_tags(text: str) -> str:
    """Removes html tags in the given text."""
    text = re.sub("<.*?>", "", text)
    return re.sub("&.*?;", "", text)


def get_last_message(access_token: str):
    """ Returns the last recieved message on the access token. """
    messages = get_messages(access_token)
    best = 0
    best_i = -1
    for i, message in enumerate(messages):
        if message.time_sent > best:
            best = message.time_sent
            best_i = i
    return messages[best_i]


def get_messages(access_token: str) -> List[Message]:
    """ Given the access token returns list of all messages. """
    response = requests.post(
        join_url(website, "api/3/komens/messages/received"),
        headers={"Authorization": "Bearer " + access_token},
    )
    data = json.loads(response.text)
    return [
        Message(
            title=_remove_html_tags(message["Title"]),
            sender=_remove_html_tags(message["Sender"]["Name"]),
            text=_remove_html_tags(message["Text"]),
            time_sent=parse_datetime(message["SentDate"]).timestamp(),
        )
        for message in data["Messages"]
    ]


def token_valid(access_token: str) -> bool:
    """ Checks the validity of the token.

        It does so by sending a request and based on the 
        result determines if the token was valid.
    """
    response = requests.get(
            join_url(website, "api/3/marks"),
            headers={"Authorization": f"Bearer {access_token}"},
        )
    return response.ok
