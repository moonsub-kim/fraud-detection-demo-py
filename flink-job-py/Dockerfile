FROM apache/flink:1.14.2-java11
ENV FLINK_VERSION=1.14.2
ENV PYTHON_VERSION=3.8.12

# https://nightlies.apache.org/flink/flink-docs-master/docs/deployment/resource-providers/standalone/docker/#enabling-python
# install python3: it has updated Python to 3.9 in Debian 11 and so install Python 3.7 from source
# it currently only supports Python 3.6, 3.7 and 3.8 in PyFlink officially.
RUN apt-get update -y && \
    apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev libffi-dev && \
    wget https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz && \
    tar -xvf Python-${PYTHON_VERSION}.tgz && \
    cd Python-${PYTHON_VERSION} && \
    ./configure --without-tests --enable-shared --enable-optimizations && \
    make -j6 && \
    make install && \
    ldconfig /usr/local/lib && \
    cd .. && rm -f Python-${PYTHON_VERSION}.tgz && rm -rf Python-${PYTHON_VERSION} && \
    ln -s /usr/local/bin/python3 /usr/local/bin/python && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip3 install -r requirements.txt

# https://mvnrepository.com/artifact/org.apache.flink/flink-connector-kafka_2.12/1.14.2
COPY jar_dependency.txt .
RUN set -ex && \
    for jar_file in $(cat jar_dependency.txt | envsubst); do \
        echo "download $jar_file"; \
        wget -P /opt/flink/lib/ $jar_file; \
    done

COPY docker-entrypoint.sh /
COPY . .

USER flink
EXPOSE 8081 6123
ENTRYPOINT ["/docker-entrypoint.sh"]
