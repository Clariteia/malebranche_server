import datetime
from typing import (
    Any,
)
from uuid import (
    UUID,
)

from minos.common import (
    ModelType,
)
from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    MetaData,
    Numeric,
    Table,
    Text,
    text,
)
from sqlalchemy.dialects.postgresql import (
    JSONB,
)
from sqlalchemy.dialects.postgresql import UUID as UUID_PG

META = MetaData()
LOG_TABLE = Table(
    "log",
    META,
    Column("uuid", UUID_PG(as_uuid=True), primary_key=True),
    Column("sublog_id", UUID_PG(as_uuid=True)),
    Column("total_amount", Numeric, nullable=False),
    Column("level", Text, nullable=False),
    Column("timestamp", DateTime),
    Column("content", Text),
)
