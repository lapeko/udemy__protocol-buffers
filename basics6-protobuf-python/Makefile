BIN = basics6-protobuf-python
PROTO_DIR = proto

run: generate
	python3 main.py

generate:
	protoc -I=$(PROTO_DIR) --python_out=$(PROTO_DIR) --pyi_out=$(PROTO_DIR) $(PROTO_DIR)/*.proto

clear:
ifeq ($(OS),Windows_NT)
	del $(PROTO_DIR)\*_pb2.py $(PROTO_DIR)\*.pyi
else
	rm $(PROTO_DIR)/*_pb2.py $(PROTO_DIR)/*.pyi
endif