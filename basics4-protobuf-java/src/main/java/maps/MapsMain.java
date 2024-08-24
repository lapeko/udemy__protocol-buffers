package maps;

import example.map.Maps;

public class MapsMain {
    public static void main(String[] args) {
        Maps.KeyIdMap message = Maps.KeyIdMap
                .newBuilder()
                .putKeyId("My key", 1)
                .putKeyId("My key 2", 100500)
                .build();

        System.out.println(message);
    }
}
