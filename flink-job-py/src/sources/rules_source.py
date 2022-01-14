from __future__ import annotations

from typing import Any, Dict

import kafka_utils
from environment import Environment
from pyflink.common.serialization import SimpleStringSchema
from pyflink.datastream import DataStream, SourceFunction
from pyflink.datastream.connectors import FlinkKafkaConsumer

# https://github.com/moonsub-kim/fraud-detection-demo/blob/4603ba37725695630bf93caa50486c69c1c982a7/flink-job/src/main/java/com/ververica/field/dynamicrules/sources/RulesSource.java#L47
def create_rules_source() -> SourceFunction:
    kafka_properties: Dict[str, Any] = kafka_utils.init_consumer_properties()
    rules_topic: str = Environment.RULES_TOPIC
    consumer: FlinkKafkaConsumer = FlinkKafkaConsumer(rules_topic, SimpleStringSchema(), kafka_properties)
    consumer.set_start_from_latest()
    return consumer

# https://github.com/moonsub-kim/fraud-detection-demo/blob/4603ba37725695630bf93caa50486c69c1c982a7/flink-job/src/main/java/com/ververica/field/dynamicrules/sources/RulesSource.java#L74
def strings_stream_to_rules(rules_strings: DataStream) -> DataStream:
    return rules_strings \
        .flat_map()
    # TODO implement
