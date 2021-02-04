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
from dateutil.parser import parse as parse_datetime
from datetime import datetime
from mark import Mark


website = "https://bakalari.mikulasske.cz/"


def get_access_token(username: str, password: str) -> str:
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
    return data["access_token"]


def _days_difference_ok(ts1, ts2, n_of_days):
    return ((ts1 - ts2) / 3600 / 24) <= n_of_days


def get_marks(access_token: str, number_of_days: int = 7):
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


