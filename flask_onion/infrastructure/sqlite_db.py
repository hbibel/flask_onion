import sqlite3
from typing import IO, Callable


class SqliteDb:
    def __init__(self, db_path: str, open_init_script: Callable[[], IO[str]]) -> None:
        self._connection = sqlite3.connect(db_path, detect_types=sqlite3.PARSE_DECLTYPES, check_same_thread=False)
        self._connection.row_factory = sqlite3.Row
        self._open_init_script = open_init_script

    @property
    def connection(self) -> sqlite3.Connection:
        return self._connection

    def init_db(self):
        with self._open_init_script() as f:
            self.connection.executescript(f.read().decode("utf8"))
