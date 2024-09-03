from google.protobuf.json_format import MessageToJson, Parse
import proto.simple_pb2 as simple


FILE_NAME = "simple"
BIN_EXT = "bin"
JSON_EXT = "json"


def serialize_bin(message: simple.Simple):
    with open(f"{FILE_NAME}.{BIN_EXT}", "wb") as f:
        f.write(message.SerializeToString())


def deserialize_bin():
    with open(f"{FILE_NAME}.{BIN_EXT}", "rb") as f:
        s = simple.Simple()
        s.ParseFromString(f.read())
        return s


def serialize_json(message: simple.Simple):
    with open(f"{FILE_NAME}.{JSON_EXT}", "w") as f:
        f.write(MessageToJson(message))


def deserialize_json():
    with open(f"{FILE_NAME}.{JSON_EXT}", "r") as f:
        return Parse(f.read(), simple.Simple())


if __name__ == "__main__":
    smpl = simple.Simple(id=2, is_simple=True, name="Some name", numbers=[1, 2, 3, 5])
    serialize_bin(smpl)
    smpl = deserialize_bin()
    print(smpl)
    serialize_json(smpl)
    smpl = deserialize_json()
    print(smpl)
