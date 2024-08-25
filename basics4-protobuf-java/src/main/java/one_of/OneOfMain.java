package one_of;

import example.oneof.OneOfOuterClass;

public class OneOfMain {
    public static void main(String[] args) {
        OneOfOuterClass.OneOf message = OneOfOuterClass.OneOf
                .newBuilder()
                .setId(1)
                .setName("Id 1")
                .build();

        System.out.println("Has ID: " + message.hasId());
        System.out.println("Has Name: " + message.hasName());
        System.out.println(message);

        message = OneOfOuterClass.OneOf
                .newBuilder()
                .setId(2)
                .setName("Id 2")
                .setId(2)
                .build();

        System.out.println("Has ID: " + message.hasId());
        System.out.println("Has Name: " + message.hasName());
        System.out.println(message);
    }
}
