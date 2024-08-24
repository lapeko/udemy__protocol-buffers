package simple;

import example.simple.SimpleOuterClass;

import java.util.Arrays;

public class SimpleMain {
    public static void main(String[] args) {
        SimpleOuterClass.Simple simple = SimpleOuterClass.Simple.newBuilder()
                .setId(1)
                .setName("Name 1")
                .setIsSimple(true)
                .addSampleList(1)
                .addSampleList(2)
                .addSampleList(3)
                .addAllSampleList(Arrays.asList(4, 5, 6))
                .build();

        System.out.println(simple);
    }
}
