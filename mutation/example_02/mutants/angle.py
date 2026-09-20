
from inspect import signature as _mutmut_signature

def _mutmut_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[mutant_name](*args, **kwargs)
    return result


from inspect import signature as _mutmut_signature

def _mutmut_yield_from_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result


def x_hours_hand__mutmut_orig(hour, minutes):
    base = (hour % 12 ) * (360 // 12)
    correction = int((minutes / 60) * (360 // 12))
    return base + correction
def x_hours_hand__mutmut_1(hour, minutes):
    base = (hour / 12 ) * (360 // 12)
    correction = int((minutes / 60) * (360 // 12))
    return base + correction
def x_hours_hand__mutmut_2(hour, minutes):
    base = (hour % 13 ) * (360 // 12)
    correction = int((minutes / 60) * (360 // 12))
    return base + correction
def x_hours_hand__mutmut_3(hour, minutes):
    base = (hour % 12 ) / (360 // 12)
    correction = int((minutes / 60) * (360 // 12))
    return base + correction
def x_hours_hand__mutmut_4(hour, minutes):
    base = (hour % 12 ) * (361 // 12)
    correction = int((minutes / 60) * (360 // 12))
    return base + correction
def x_hours_hand__mutmut_5(hour, minutes):
    base = (hour % 12 ) * (360 / 12)
    correction = int((minutes / 60) * (360 // 12))
    return base + correction
def x_hours_hand__mutmut_6(hour, minutes):
    base = (hour % 12 ) * (360 // 13)
    correction = int((minutes / 60) * (360 // 12))
    return base + correction
def x_hours_hand__mutmut_7(hour, minutes):
    base = None
    correction = int((minutes / 60) * (360 // 12))
    return base + correction
def x_hours_hand__mutmut_8(hour, minutes):
    base = (hour % 12 ) * (360 // 12)
    correction = int((minutes * 60) * (360 // 12))
    return base + correction
def x_hours_hand__mutmut_9(hour, minutes):
    base = (hour % 12 ) * (360 // 12)
    correction = int((minutes / 61) * (360 // 12))
    return base + correction
def x_hours_hand__mutmut_10(hour, minutes):
    base = (hour % 12 ) * (360 // 12)
    correction = int((minutes / 60) / (360 // 12))
    return base + correction
def x_hours_hand__mutmut_11(hour, minutes):
    base = (hour % 12 ) * (360 // 12)
    correction = int((minutes / 60) * (361 // 12))
    return base + correction
def x_hours_hand__mutmut_12(hour, minutes):
    base = (hour % 12 ) * (360 // 12)
    correction = int((minutes / 60) * (360 / 12))
    return base + correction
def x_hours_hand__mutmut_13(hour, minutes):
    base = (hour % 12 ) * (360 // 12)
    correction = int((minutes / 60) * (360 // 13))
    return base + correction
def x_hours_hand__mutmut_14(hour, minutes):
    base = (hour % 12 ) * (360 // 12)
    correction = None
    return base + correction
def x_hours_hand__mutmut_15(hour, minutes):
    base = (hour % 12 ) * (360 // 12)
    correction = int((minutes / 60) * (360 // 12))
    return base - correction

x_hours_hand__mutmut_mutants = {
'x_hours_hand__mutmut_1': x_hours_hand__mutmut_1, 
    'x_hours_hand__mutmut_2': x_hours_hand__mutmut_2, 
    'x_hours_hand__mutmut_3': x_hours_hand__mutmut_3, 
    'x_hours_hand__mutmut_4': x_hours_hand__mutmut_4, 
    'x_hours_hand__mutmut_5': x_hours_hand__mutmut_5, 
    'x_hours_hand__mutmut_6': x_hours_hand__mutmut_6, 
    'x_hours_hand__mutmut_7': x_hours_hand__mutmut_7, 
    'x_hours_hand__mutmut_8': x_hours_hand__mutmut_8, 
    'x_hours_hand__mutmut_9': x_hours_hand__mutmut_9, 
    'x_hours_hand__mutmut_10': x_hours_hand__mutmut_10, 
    'x_hours_hand__mutmut_11': x_hours_hand__mutmut_11, 
    'x_hours_hand__mutmut_12': x_hours_hand__mutmut_12, 
    'x_hours_hand__mutmut_13': x_hours_hand__mutmut_13, 
    'x_hours_hand__mutmut_14': x_hours_hand__mutmut_14, 
    'x_hours_hand__mutmut_15': x_hours_hand__mutmut_15
}

def hours_hand(*args, **kwargs):
    result = _mutmut_trampoline(x_hours_hand__mutmut_orig, x_hours_hand__mutmut_mutants, *args, **kwargs)
    return result 

hours_hand.__signature__ = _mutmut_signature(x_hours_hand__mutmut_orig)
x_hours_hand__mutmut_orig.__name__ = 'x_hours_hand'



def x_minutes_hand__mutmut_orig(hour, minutes):
    return minutes * (360 // 60)

def x_minutes_hand__mutmut_1(hour, minutes):
    return minutes / (360 // 60)

def x_minutes_hand__mutmut_2(hour, minutes):
    return minutes * (361 // 60)

def x_minutes_hand__mutmut_3(hour, minutes):
    return minutes * (360 / 60)

def x_minutes_hand__mutmut_4(hour, minutes):
    return minutes * (360 // 61)

x_minutes_hand__mutmut_mutants = {
'x_minutes_hand__mutmut_1': x_minutes_hand__mutmut_1, 
    'x_minutes_hand__mutmut_2': x_minutes_hand__mutmut_2, 
    'x_minutes_hand__mutmut_3': x_minutes_hand__mutmut_3, 
    'x_minutes_hand__mutmut_4': x_minutes_hand__mutmut_4
}

def minutes_hand(*args, **kwargs):
    result = _mutmut_trampoline(x_minutes_hand__mutmut_orig, x_minutes_hand__mutmut_mutants, *args, **kwargs)
    return result 

minutes_hand.__signature__ = _mutmut_signature(x_minutes_hand__mutmut_orig)
x_minutes_hand__mutmut_orig.__name__ = 'x_minutes_hand'



def x_between__mutmut_orig(hour, minutes):
    return abs(hours_hand(hour, minutes) - minutes_hand(hour, minutes))

def x_between__mutmut_1(hour, minutes):
    return abs(hours_hand(None, minutes) - minutes_hand(hour, minutes))

def x_between__mutmut_2(hour, minutes):
    return abs(hours_hand(hour, None) - minutes_hand(hour, minutes))

def x_between__mutmut_3(hour, minutes):
    return abs(hours_hand( minutes) - minutes_hand(hour, minutes))

def x_between__mutmut_4(hour, minutes):
    return abs(hours_hand(hour,) - minutes_hand(hour, minutes))

def x_between__mutmut_5(hour, minutes):
    return abs(hours_hand(hour, minutes) + minutes_hand(hour, minutes))

def x_between__mutmut_6(hour, minutes):
    return abs(hours_hand(hour, minutes) - minutes_hand(None, minutes))

def x_between__mutmut_7(hour, minutes):
    return abs(hours_hand(hour, minutes) - minutes_hand(hour, None))

def x_between__mutmut_8(hour, minutes):
    return abs(hours_hand(hour, minutes) - minutes_hand( minutes))

def x_between__mutmut_9(hour, minutes):
    return abs(hours_hand(hour, minutes) - minutes_hand(hour,))

x_between__mutmut_mutants = {
'x_between__mutmut_1': x_between__mutmut_1, 
    'x_between__mutmut_2': x_between__mutmut_2, 
    'x_between__mutmut_3': x_between__mutmut_3, 
    'x_between__mutmut_4': x_between__mutmut_4, 
    'x_between__mutmut_5': x_between__mutmut_5, 
    'x_between__mutmut_6': x_between__mutmut_6, 
    'x_between__mutmut_7': x_between__mutmut_7, 
    'x_between__mutmut_8': x_between__mutmut_8, 
    'x_between__mutmut_9': x_between__mutmut_9
}

def between(*args, **kwargs):
    result = _mutmut_trampoline(x_between__mutmut_orig, x_between__mutmut_mutants, *args, **kwargs)
    return result 

between.__signature__ = _mutmut_signature(x_between__mutmut_orig)
x_between__mutmut_orig.__name__ = 'x_between'


