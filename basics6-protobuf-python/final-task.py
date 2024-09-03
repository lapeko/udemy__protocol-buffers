from google.protobuf.json_format import Parse, MessageToJson
import proto.address_book_pb2 as address_book

FILE_NAME = "address_book"
BIN_PATH = f"{FILE_NAME}.bin"
JSON_PATH = f"{FILE_NAME}.json"


def serialize_bin(message: address_book.AddressBook):
    with open(BIN_PATH, "wb") as f:
        f.write(message.SerializeToString())


def deserialize_bin():
    with open(BIN_PATH, "rb") as f:
        m = address_book.AddressBook()
        m.ParseFromString(f.read())
        return m


def serialize_json(message: address_book.AddressBook):
    with open(JSON_PATH, "w") as f:
        f.write(MessageToJson(message))


def deserialize_json():
    with open(JSON_PATH, "r") as f:
        return Parse(f.read(), address_book.AddressBook())


if __name__ == "__main__":
    book = address_book.AddressBook(people=[
        address_book.Person(id=1, name="Mariam", email="mariam@mail.com", phones=[
            address_book.Person.PhoneNumber(number="123456", type=address_book.Person.PhoneType.HOME),
            address_book.Person.PhoneNumber(number="+123456789", type=address_book.Person.PhoneType.MOBILE)
        ]),
        address_book.Person(id=2, name="Daria", email="daria@mail.com", phones=[
            address_book.Person.PhoneNumber(number="+111222333", type=address_book.Person.PhoneType.MOBILE)
        ]),
    ])
    serialize_bin(book)
    print(deserialize_bin())
    serialize_json(book)
    print(deserialize_json())
