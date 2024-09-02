BIN = basics6-protobuf-python
PROTO_DIR = proto

run:
	generage
	python3 main.py

generate:
	protoc -I=$(PROTO_DIR) --python_out=$(PROTO_DIR) $(PROTO_DIR)/*.proto

clear:
	rm $(PROTO_DIR)/*_pb2.py