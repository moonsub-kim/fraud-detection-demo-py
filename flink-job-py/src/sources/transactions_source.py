from __future__ import annotations

from typing import Any, Dict

from environment import Environment
from kafka_utils import init_consumer_properties
from pyflink.common.serialization import SimpleStringSchema
from pyflink.datastream import DataStream, SourceFunction
from pyflink.datastream.connectors import FlinkKafkaConsumer

# https://github.com/moonsub-kim/fraud-detection-demo/blob/4603ba37725695630bf93caa50486c69c1c982a7/flink-job/src/main/java/com/ververica/field/dynamicrules/sources/TransactionsSource.java#L40
def create_transactions_source() -> SourceFunction:
    kafka_properties: Dict[str, Any] = init_consumer_properties()
    topic: str = Environment.DATA_TOPIC
    consumer: FlinkKafkaConsumer = FlinkKafkaConsumer(topic, SimpleStringSchema(), kafka_properties)
    consumer.set_start_from_latest()
    return consumer

# https://github.com/moonsub-kim/fraud-detection-demo/blob/4603ba37725695630bf93caa50486c69c1c982a7/flink-job/src/main/java/com/ververica/field/dynamicrules/sources/TransactionsSource.java#L61
def strings_stream_to_transactions(transaction_strings: DataStream) -> DataStream:
    return transaction_strings \
        .flat_map()