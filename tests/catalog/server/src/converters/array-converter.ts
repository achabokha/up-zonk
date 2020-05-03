import {
    Converter,
    IConverter,
    IDeserializer,
    ISerializer,
} from "@tsed/common";
import { isArrayOrArrayClass } from "@tsed/core";

///
///     This converter is taken just right from tsed
///     it invokes automatically if a method returns an array that
///     there is on need to decorate the method with @ReturnType.
///     not a biggie but nice --
///
@Converter(Array)
export class ArrayConverter implements IConverter {
    deserialize<T>(
        data: any[],
        target: any,
        baseType: T,
        deserializer: IDeserializer
    ): T[] {
        if (isArrayOrArrayClass(data)) {
            return (data as Array<any>).map((item) =>
                deserializer(item, baseType)
            );
        }

        return <any>[data];
    }

    serialize(data: any[], serializer: ISerializer) {
        return (data as Array<any>).map((item) => serializer(item));
    }
}
