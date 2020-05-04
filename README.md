# Generate protocol buffers
sudo apt installsudo protobuf-compiler

protoc -i=. --python_out=generated message.proto
