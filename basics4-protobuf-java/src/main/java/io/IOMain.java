package io;

import example.map.Maps;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class IOMain {
    private static void writeToFile(Maps.KeyIdMap message)  throws IOException {
        FileOutputStream fos = new FileOutputStream("kei_id_map.bin");
        message.writeTo(fos);
    }

    private static Maps.KeyIdMap readFromFile() throws IOException {
        FileInputStream fis = new FileInputStream("kei_id_map.bin");
        return Maps.KeyIdMap.parseFrom(fis);
    }

    public static void main(String[] args) throws IOException {
        Maps.KeyIdMap message = Maps.KeyIdMap
                .newBuilder()
                .putKeyId("Name 1", 1)
                .putKeyId("Name 2", 2)
                .putKeyId("Name 3", 3)
                .build();
        writeToFile(message);
        message = readFromFile();
        System.out.println(message);
    }
}
