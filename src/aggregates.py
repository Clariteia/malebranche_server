from __future__ import (
    annotations,
)

from enum import (
    Enum,
)
from typing import (
    Optional,
)

from minos.common import Aggregate
from minos.common import uuid


class LogLevel(Enum):
    pass


class Log(Aggregate):
    message: str
    name: str
    args: list[str]
    levelname: str
    levelno: int
    pathname: str
    filename: str
    module: str
    exc_info: Optional[str]
    exc_text: Optional[str]
    stack_info: Optional[str]
    lineno: int
    funcName: str
    created: float
    msecs: float
    relativeCreated: float
    thread: int
    threadName: str
    processName: str
    process: str
    parent: str
