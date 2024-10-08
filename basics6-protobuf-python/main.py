import proto.simple_pb2 as simple
import proto.complex_pb2 as complex_proto
import proto.enum_pb2 as enum_proto
import proto.one_of_pb2 as one_of
import proto.map_pb2 as map_proto


def get_simple():
    return simple.Simple(
        id=1,
        is_simple=True,
        name="Name",
        numbers=[1, 2, 3]
    )


def get_complex():
    cmplx = complex_proto.Complex()
    cmplx.dummy.id = 1
    cmplx.dummy.name = "Blabla"
    cmplx.dummies.add(id=2, name="Name 2")
    cmplx.dummies.add(id=3, name="Name 3")
    print(cmplx)


def get_enum():
    return enum_proto.EyeColor(eye_color=enum_proto.EYE_COLOR_GREEN)


def get_one_of():
    var = one_of.OneOf(id=1)
    var.message = "message"
    return var


def get_map():
    var = map_proto.TestMap()
    var.key_value_map[1] = "test1"
    var.key_value_map[2] = "test2"
    return var


if __name__ == '__main__':
    # print(get_simple())
    # get_complex()
    # print(get_enum())
    # print(get_one_of())
    print(get_map())
