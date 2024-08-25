package serializer_json;

import com.google.protobuf.InvalidProtocolBufferException;
import com.google.protobuf.util.JsonFormat;
import example.map.Maps;

public class SerializerJsonMain {
    private static String toJson(Maps.KeyIdMap message) throws InvalidProtocolBufferException {
        return JsonFormat.printer()
                .omittingInsignificantWhitespace()
                .print(message);
    }

    private static Maps.KeyIdMap fromJson(String json) throws InvalidProtocolBufferException {
        Maps.KeyIdMap.Builder builder = Maps.KeyIdMap.newBuilder();

        JsonFormat.parser().merge(json, builder);
        return builder.build();
    }

    public static void main(String[] args) throws InvalidProtocolBufferException {
        Maps.KeyIdMap message = Maps.KeyIdMap.newBuilder()
                .putKeyId("Name 1", 1)
                .putKeyId("Name 2", 2)
                .putKeyId("Name 3", 3)
                .build();

        String json = toJson(message);
        System.out.println(json);

        message = fromJson(json);
        System.out.println(message);
    }
}
