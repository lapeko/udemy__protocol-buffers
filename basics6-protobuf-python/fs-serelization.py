import proto.simple_pb2 as simple


FILE_NAME = "simple.bin"


def serialize_and_save(proto_obj: simple.Simple):
    with open(FILE_NAME, "wb") as f:
        f.write(proto_obj.SerializeToString())


def deserialize_from_file():
    s = simple.Simple()
    try:
        with open(FILE_NAME, "rb") as f:
            s.ParseFromString(f.read())
            return s
    except IOError:
        print("Could not open file: " + FILE_NAME)


if __name__ == "__main__":
    smpl = simple.Simple(id=2, is_simple=True, name="Some name", numbers=[1, 2, 3, 5])
    serialize_and_save(smpl)
    print(deserialize_from_file())


