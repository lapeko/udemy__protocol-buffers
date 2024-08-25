package address_book;

import com.example.tutorial.protos.AddressBook;
import com.example.tutorial.protos.Person;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.Arrays;


public class AddressBookMain {
    private static final String filePath = "address_book.bin";

    private static void writeToFile(AddressBook message) throws IOException {
        FileOutputStream fos = new FileOutputStream(filePath);
        message.writeTo(fos);
    }

    private static AddressBook readFromFile() throws IOException {
        FileInputStream fis = new FileInputStream(filePath);
        return AddressBook.parseFrom(fis);
    }

    private static Person createPerson(String name, int id, String email, Person.PhoneNumber ...phones) {
        return Person
                .newBuilder()
                .setName(name)
                .setId(id)
                .setEmail(email)
                .addAllPhones(Arrays.asList(phones))
                .build();
    }

    private static Person.PhoneNumber createPhone(String phoneNumber, Person.PhoneType type) {
        return Person.PhoneNumber.newBuilder().setNumber(phoneNumber).setType(type).build();
    }

    public static void main(String[] args) throws IOException {
        Person person1 = createPerson(
                "Alena",
                1,
                "alena@mail.com",
                createPhone("911", Person.PhoneType.WORK),
                createPhone("100500", Person.PhoneType.HOME)
        );
        Person person2 = createPerson(
                "Maks",
                2,
                "maks@tut.by"
        );
        AddressBook addressBook = AddressBook
                .newBuilder()
                .addAllPeople(Arrays.asList(
                        person1,
                        person2
                ))
                .build();

        System.out.println(addressBook);
        writeToFile(addressBook);
        addressBook = readFromFile();
        System.out.println(addressBook);
    }
}
