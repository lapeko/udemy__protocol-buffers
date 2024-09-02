import proto.simple_pb2 as simple


def get_simple():
    return simple.Simple(
        id=1,
        is_simple=True,
        name="Name",
        numbers=[1, 2, 3]
    )


if __name__ == '__main__':
    print(get_simple())
