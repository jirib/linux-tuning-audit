# scrape/models.py

import re
from dataclasses import dataclass

SYSCTL_PREFIXES = ("fs", "net", "vm", "sunrpc", "kernel")

SYSCTL_NAME_RE = re.compile(
    rf"^({'|'.join(map(re.escape, SYSCTL_PREFIXES))})(\.[a-zA-Z0-9_-]+)+$"
)

SYSCTL_VALUE_RE = re.compile(r"^[^\n\r\x00]+$")


@dataclass(frozen=True)
class SysctlName:
    """
    Represents the name of a sysctl setting, e.g. "net.ipv4.tcp_syncookies".
    """
    value: str

    def __post_init__(self) -> None:
        if not SYSCTL_NAME_RE.fullmatch(self.value):
            raise ValueError(f"Invalid sysctl name: {self.value!r}")


@dataclass(frozen=True)
class SysctlValue:
    """
    Represents the value of a sysctl setting.
    """
    value: str  # it's a string because it can a digit or a sequence of numbers

    def __post_init__(self) -> None:
        if not self.value:
            raise ValueError("Empty sysctl value")

        if not SYSCTL_VALUE_RE.fullmatch(self.value):
            raise ValueError(f"Invalid sysctl value: {self.value!r}")


@dataclass(frozen=True)
class SysctlSetting:
    """
    Represents a sysctl setting recommendation extracted from a scrape plugin.
    """
    name: SysctlName
    value: SysctlValue


@dataclass(frozen=True)
class ScrapedRecommendation:
    """
    Represents a scraped recommendation containing multiple sysctl settings.
    """
    source: str
    url: str
    title: str
    settings: tuple[SysctlSetting]