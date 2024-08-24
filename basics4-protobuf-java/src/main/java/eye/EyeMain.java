package eye;

import example.eye.Enums;

public class EyeMain {
    public static void main(String[] args) {
        Enums.Eye message = Enums.Eye
            .newBuilder()
//            .setColorValue(2)
            .setColor(Enums.EyeColor.EYE_COLOR_BLUE)
            .build();

        System.out.println(message);
    }
}
