import proto.simple_pb2 as simple
import proto.complex_pb2 as complex_proto
import proto.enum_pb2 as enum_proto


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


if __name__ == '__main__':
    # print(get_simple())
    # get_complex()
    print(get_enum())
