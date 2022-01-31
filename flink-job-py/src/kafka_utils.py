from __future__ import annotations

from typing import Any, Dict

from environment import Environment

def init_consumer_properties() -> Dict[str, Any]:
    properties: Dict[str, Any] = init_properties()
    properties["auto.offset.reset"] = Environment.OFFSET
    properties["group.id"] = Environment.GROUP_ID
    return properties


def init_producer_properties() -> Dict[str, Any]:
    return init_properties()


def init_properties() -> Dict[str, Any]:
    print(Environment.KAFKA_HOST)
    return {
        "bootstrap.servers": f"{Environment.KAFKA_HOST}:{Environment.KAFKA_PORT}",
    }
