#!/usr/bin/python3
<<<<<<< HEAD
def magic_calculation(a, b):
    result = 0
=======


def magic_calculation(a, b):
    result = 0

>>>>>>> 1061a5e1e9e3c972dd915bb55c72e7fb06847607
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
<<<<<<< HEAD
            result += a ** b / i
        except Exception:
            result = b + a
            break
=======

            result += a ** b / i
        except:
            result = b + a
            break

>>>>>>> 1061a5e1e9e3c972dd915bb55c72e7fb06847607
    return result
