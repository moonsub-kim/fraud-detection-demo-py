from __future__ import annotations

from pyflink.datastream.functions import SourceFunction

from environment import Environment
from pyflink.common import WatermarkStrategy, Duration, ExecutionConfig
from pyflink.datastream import DataStream, StreamExecutionEnvironment
from pyflink.datastream.time_characteristic import TimeCharacteristic
from sources.rules_source import create_rules_source
from sources.transactions_source import create_transactions_source

class RulesEvaluator():
    def __init__(self: RulesEvaluator) -> None:
        pass

    # https://github.com/moonsub-kim/fraud-detection-demo/blob/9b94a3b5464b22982f480f6b695784ed213eed12/flink-job/src/main/java/com/ververica/field/dynamicrules/RulesEvaluator.java#L66
    def run(self: RulesEvaluator) -> None:
        is_local: bool = Environment.LOCAL_EXECUTION
        enable_checkpoints: bool = Environment.ENABLE_CHECKPOINTS
        checkpoint_interval: int = Environment.CHECKPOINT_INTERVAL
        min_pause_between_checkpoints: int = Environment.CHECKPOINT_INTERVAL

        env: StreamExecutionEnvironment = self.configure_stream_execution_environment()

        if enable_checkpoints:
            env.enable_checkpointing(checkpoint_interval)
            env.get_checkpoint_config().set_min_pause_between_checkpoints(min_pause_between_checkpoints)

        transactions: DataStream = self.get_transactions_stream(env)
        transactions.print()
        
        res = env.execute("Frand Detection Engine")
        print(res)

    # https://github.com/moonsub-kim/fraud-detection-demo/blob/9b94a3b5464b22982f480f6b695784ed213eed12/flink-job/src/main/java/com/ververica/field/dynamicrules/RulesEvaluator.java#L164
    def configure_stream_execution_environment(self: RulesEvaluator) -> StreamExecutionEnvironment:
        stream_execution_env: StreamExecutionEnvironment = StreamExecutionEnvironment.get_execution_environment()
        stream_execution_env.set_stream_time_characteristic(TimeCharacteristic.EventTime)
        stream_execution_env.add_classpaths("file:///opt/flink/lib/flink-connector-kafka_2.12-1.14.2.jar")
        stream_execution_env.add_jars("file:///opt/flink/lib/flink-connector-kafka_2.12-1.14.2.jar")
        stream_execution_env \
            .get_checkpoint_config() \
            .set_checkpoint_interval(Environment.CHECKPOINT_INTERVAL) \
            .set_min_pause_between_checkpoints(Environment.MIN_PAUSE_BETWEEN_CHECKPOINTS)

        # configureRestartStrategy()
        return stream_execution_env

    # https://github.com/moonsub-kim/fraud-detection-demo/blob/9b94a3b5464b22982f480f6b695784ed213eed12/flink-job/src/main/java/com/ververica/field/dynamicrules/RulesEvaluator.java#L149
    def get_rules_update_stream(self: RulesEvaluator, env: StreamExecutionEnvironment) -> None:
        rules_source: SourceFunction = create_rules_source()
        rules_strings: DataStream = env.add_source(rules_source).name('Kafka').set_parallelism(1)
        # TODO implement

    # https://github.com/moonsub-kim/fraud-detection-demo/blob/9b94a3b5464b22982f480f6b695784ed213eed12/flink-job/src/main/java/com/ververica/field/dynamicrules/RulesEvaluator.java#L135
    def get_transactions_stream(self: RulesEvaluator, env: StreamExecutionEnvironment) -> None:
        transactions_source: SourceFunction = create_transactions_source()
        parallelism: int = Environment.SOURCE_PARALLELISM
        transactions_strings_stream: DataStream = env \
            .add_source(transactions_source) \
            .name('Transactions Source') \
            .set_parallelism(parallelism)

        # transactions_stream: DataStream = transactions_source
        return transactions_strings_stream
