import enum
RED = "red"
YELLOW = "yellow"
GREEN = "green"

class ColorEnum(enum.Enum):
    RED = "red"
    YELLOW = "yellow"
    GREEN = "green"

def take_enum_action(light):
    match light:
        case ColorEnum.RED:
            print("Stop")
        case ColorEnum.YELLOW:
            print("Caution")
        case ColorEnum.GREEN:
            print("Go")
        case _:
            raise RuntimeError

def take_truncated_action(light):
    match light:
        case RED:
            print("Stop")

def take_debug_action(light):
    match light:
        case RED: 
            print(f"{RED=}, {light=}")

def take_unpacking_action(light):
    try:
        (RED,) = (light,)
    except TypeError:
        print(f"TypeError: cannot unpack {light=}")
    else:
        print(f"{RED=}, {light=}")

take_truncated_action(GREEN)
take_debug_action(GREEN)
#take_unpacking_action(GREEN)