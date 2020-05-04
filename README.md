# Generate protocol buffers
sudo apt installsudo protobuf-compiler

protoc -i=. --python_out=generated message.proto


# Run in docker compose
docker-compose up 


# Run on kubernetes
kubectl kudo init
kubectl kudo install zookeeper
kubectl kudo install kafka

kubectl kudo install kafka --instance=kafka-instance --namespace=default -p METRICS_ENABLED=true -p DEFAULT_REPLICATION_FACTOR=3 -p BROKER_COUNT=3 p BROKER_CPUS=512m BROKER_MEM=512m 

## Config of kafka in kudo
kubectl kudo install kafka \
    --instance=kafka-instance --namespace=kudo-kafka -p ZOOKEEPER_URI=$ZOOKEEPER_URI \
    -p BROKER_CPUS=2000m \
    -p BROKER_COUNT=5 \
    -p BROKER_MEM=4096m \
    -p DISK_SIZE=100Gi \
    -p NUM_RECOVERY_THREADS_PER_DATA_DIR=3 \
    -p DEFAULT_REPLICATION_FACTOR=3 \
    -p MIN_INSYNC_REPLICAS=2 \
    -p NUM_NETWORK_THREADS=10 \
    -p NUM_PARTITIONS=3 \
    -p QUEUED_MAX_REQUESTS=1000 

# kubernetes
kubectl apply -f deployment.yaml

kubectl logs -f -l