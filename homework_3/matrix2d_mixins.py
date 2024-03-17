import numpy as np
import numbers


class GetterSetterMixin(object):
    def __init__(self):
        self._value = None
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = np.asarray(value)

    @value.deleter
    def value(self):
        del self._value


class StrMixin(object):
    def __str__(self) -> str:
        s = "\n          ".join([str(row) for row in self._value])
        return f'Matrix2D([{s}])'


class WriteToFileMixin(object):
    def write_to_file(self, filename: str):
        with open(filename, 'w') as f:
            f.write(str(self))


class Matrix2DMixins(np.lib.mixins.NDArrayOperatorsMixin, WriteToFileMixin, StrMixin, GetterSetterMixin):
    def __init__(self, value):
        self._value = np.asarray(value)

    _HANDLED_TYPES = (np.ndarray, numbers.Number)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        out = kwargs.get('out', ())
        for x in inputs + out:
            if not isinstance(x, self._HANDLED_TYPES + (Matrix2DMixins,)):
                return NotImplemented

        inputs = tuple(x._value if isinstance(x, Matrix2DMixins) else x for x in inputs)
        if out:
            kwargs['out'] = tuple(
                x._value if isinstance(x, Matrix2DMixins) else x
                for x in out)
        result = getattr(ufunc, method)(*inputs, **kwargs)

        if type(result) is tuple:
            return tuple(type(self)(x) for x in result)
        elif method == 'at':
            return None
        else:
            return type(self)(result)
