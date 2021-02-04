import json
from os.path import join as join_path
from posixpath import join as join_url
from shutil import copyfileobj
from typing import List, NamedTuple

import requests
from dateutil.parser import parse as parse_datetime


class Attachment(NamedTuple):
    id_: str
    name: str


class Message(NamedTuple):
    attachments: List[Attachment]
    sender: str
    text: str
    time_sent: float
    title: str


class Homework(NamedTuple):
    attachments: List[Attachment]
    content: str
    id_: str
    subject: str
    teacher: str
    time_start: float
    time_end: float


class Mark(NamedTuple):
    subject: str
    value: str
    weight: int
    type_: str
    caption: str
    time_added: float


def get_refresh_token(website: str, username: str, password: str) -> str:
    response = requests.post(
        join_url(website, "api/login"),
        data={
            "client_id": "ANDR",
            "grant_type": "password",
            "username": username,
            "password": password,
        },
    )
    data = json.loads(response.text)
    return data["refresh_token"]


def get_access_token(website: str, username: str, password: str) -> str:
    response = requests.post(
        join_url(website, "api/login"),
        data={
            "client_id": "ANDR",
            "grant_type": "password",
            "username": username,
            "password": password,
        },
    )
    data = json.loads(response.text)
    return data["access_token"]


def get_access_token_from_refresh_token(website: str, refresh_token: str) -> str:
    response = requests.post(
        join_url(website, "api/login"),
        data={
            "client_id": "ANDR",
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
        },
    )
    data = json.loads(response.text)
    return data["access_token"]


def get_messages(website: str, access_token: str, as_dicts=False) -> List[Message]:
    response = requests.post(
        join_url(website, "api/3/komens/messages/received"),
        headers={"Authorization": "Bearer " + access_token},
    )
    data = json.loads(response.text)
    if as_dicts:
        return data
    return [
        Message(
            title=message["Title"],
            sender=message["Sender"]["Name"],
            text=message["Text"],
            time_sent=parse_datetime(message["SentDate"]).timestamp(),
        )
        for message in data["Messages"]
    ]


def get_notices(website: str, access_token: str, as_dicts=False) -> List[Message]:
    response = requests.post(
        join_url(website, "api/3/komens/messages/noticeboard"),
        headers={"Authorization": "Bearer " + access_token},
    )
    data = json.loads(response.text)
    if as_dicts:
        return data
    return [
        Message(
            title=message["Title"],
            sender=message["Sender"]["Name"],
            text=message["Text"],
            time_sent=parse_datetime(message["SentDate"]).timestamp(),
            attachments=[
                Attachment(id_=attachment["Id"], name=attachment["Name"])
                for attachment in message["Attachments"]
            ],
        )
        for message in data["Messages"]
    ]


def get_homework(website: str, access_token: str, as_dicts=False) -> List[Homework]:
    response = requests.get(
        join_url(website, "api/3/homeworks"),
        headers={"Authorization": "Bearer " + access_token},
    )
    data = json.loads(response.text)
    if as_dicts:
        return data
    return [
        Homework(
            id_=homework["ID"],
            subject=homework["Subject"]["Name"],
            teacher=homework["Teacher"],
            content=homework["Content"],
            time_start=parse_datetime(homework["DateStart"]).timestamp(),
            time_end=parse_datetime(homework["DateEnd"]).timestamp(),
            attachments=[
                Attachment(id_=attachment["Id"], name=attachment["Name"])
                for attachment in homework["Attachments"]
            ],
        )
        for homework in data["Homeworks"]
    ]


def get_marks(website: str, access_token: str, as_dicts=False) -> List[Mark]:
    response = requests.get(
        join_url(website, "api/3/marks"),
        headers={"Authorization": "Bearer " + access_token},
    )
    data = json.loads(response.text)
    if as_dicts:
        return data
    return [
        Mark(
            subject=subject["Subject"]["Name"],
            value=mark["MarkText"],
            weight=mark["Weight"],
            type_=mark["TypeNote"],
            caption=mark["Caption"],
            time_added=parse_datetime(mark["EditDate"]).timestamp(),
        )
        for subject in data["Subjects"] for mark in subject["Marks"]
    ]


def get_attachment(website: str, access_token: str, attachment: Attachment) -> str:
    response = requests.get(
        join_url(website, "api/3/komens/attachment", attachment.id_),
        headers={"Authorization": "Bearer " + access_token},
        stream=True,
    )
    file_name = join_path(".attachments", attachment.name)
    with open(file_name, "wb") as file:
        copyfileobj(response.raw, file)
    return file_name
