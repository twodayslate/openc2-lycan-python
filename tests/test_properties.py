import openc2
import pytest
import json
import sys
import stix2.exceptions


def test_args_custom_invalid_property():

    with pytest.raises(stix2.exceptions.PropertyPresenceError):

        @openc2.properties.CustomProperty(
            "x-custom-property", [("type", stix2.properties.StringProperty())]
        )
        class MyCustomProp(object):
            pass


def test_args_custom_embed_property():
    @openc2.properties.CustomProperty(
        "x-custom-property-inner", [("value", stix2.properties.StringProperty())]
    )
    class MyCustomPropInner(object):
        pass

    @openc2.properties.CustomProperty(
        "x-custom-property",
        [("value", stix2.properties.ListProperty(MyCustomPropInner))],
    )
    class MyCustomProp(object):
        pass

    foo = MyCustomProp(value=[{"value": "my_value"}])
    assert foo != None
    assert len(foo.value) > 0
    assert foo.value[0] != None
    assert foo.value[0].value == "my_value"

    foo = MyCustomProp(value=[MyCustomPropInner(value="my_value")])
    assert foo != None
    assert len(foo.value) > 0
    assert foo.value[0] != None
    assert foo.value[0].value == "my_value"

    @openc2.CustomArgs(
        "x-custom", [("value", stix2.properties.ListProperty(MyCustomProp))]
    )
    class MyCustomArgs(object):
        pass

    print("bfoo", foo.serialize())
    foo = MyCustomArgs(value=[foo])
    print("foo", foo.serialize())
    assert foo != None
    assert len(foo.value) > 0
    assert foo.value[0] != None
    assert len(foo.value[0].value) > 0
    assert foo.value[0].value[0] != None
    assert foo.value[0].value[0].value == "my_value"
