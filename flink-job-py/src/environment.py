from __future__ import annotations

import os
from typing import Any, Dict

class Environment():    
    # KAFKA
    KAFKA_HOST: str = os.getenv(key="KAFKA_HOST", default="localhost")
    KAFKA_PORT: int = os.getenv(key="KAFKA_PORT", default=9092)

    DATA_TOPIC: str = os.getenv(key="DATA_TOPIC", default="livetransactions")
    ALERTS_TOPIC: str = os.getenv(key="ALERTS_TOPIC", default="alerts")
    RULES_TOPIC: str = os.getenv(key="RULES_TOPIC", default="rules")
    LATENCY_TOPIC: str = os.getenv(key="LATENCY_TOPIC", default="latency")
    RULES_EXPORT_TOPIC: str = os.getenv(key="CURRENT_RULES_TOPIC", default="current-rules")

    OFFSET: str = os.getenv(key="OFFSET", default="latest")

    # General
    RULES_SOURCE: str = os.getenv(key="RULES_SOURCE", default="KAFKA") # SOCKET, PUB/SUB, KAFKA 선택하는옵션, 버려

    TRANSACTIONS_SOURCE: str = os.getenv(key="DATA_SOURCE", default="GENERATOR")
    ALERTS_SINK: str = os.getenv(key="ALERTS_SINK", default="STDOUT")
    LATENCY_SINK: str = os.getenv(key="LATENCY_SINK", default="STDOUT")
    RULES_EXPORT_SINK: str = os.getenv(key="RULES_EXPORT_SINK", default="STDOUT")

    RECORDS_PER_SECOND: int = os.getenv(key="RECORDS_PER_SECOND", default=2)

    LOCAL_EXECUTION: bool = os.getenv(key="LOCAL_EXECUTION", default=False)

    SOURCE_PARALLELISM: int = os.getenv(key="SOURCE_PARALLELISM", default=2)

    ENABLE_CHECKPOINTS: bool = os.getenv(key="ENABLE_CHECKPOINTS", default=False)

    CHECKPOINT_INTERVAL: int = os.getenv(key="CHECKPOINT_INTERVAL", default=60)
    MIN_PAUSE_BETWEEN_CHECKPOINTS: int = os.getenv(key="MIN_PAUSE_BETWEEN_CHECKPOINTS", default=10000)
    OUT_OF_ORDERNESS: int = os.getenv(key="OUT_OF_ORDERNESS", default=500)
