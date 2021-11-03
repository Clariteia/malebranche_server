from __future__ import (
    annotations,
)

from datetime import (
    datetime,
)
from enum import (
    Enum,
)

from minos.common import (
    Aggregate,
    uuid,
)


class LogLevel(Enum):
    pass


class Log(Aggregate):
    id: uuid
    sublog_id: uuid
    level: LogLevel
    timestamp: datetime
    content: str
