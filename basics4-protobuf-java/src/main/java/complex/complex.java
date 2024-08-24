package complex;

import example.complex.ComplexOuterClass;

import java.util.Arrays;

public class complex {
    public static void main(String[] args) {
        ComplexOuterClass.Complex message = ComplexOuterClass.Complex
            .newBuilder()
            .setDummy(genDummy(1, "Name 1"))
            .addAllDummies(Arrays.asList(
                genDummy(2, "Name 2"),
                genDummy(3, "Name 3"),
                genDummy(4, "Name 4")
            ))
            .build();

        System.out.println(message);
    }

    private static ComplexOuterClass.Dummy genDummy(int id, String name) {
        return ComplexOuterClass.Dummy
            .newBuilder()
            .setId(id)
            .setName(name)
            .build();
    }
}
