import abc
import Exciepcions

class AbstractValidator(object):
    __metaclass__  = abc.ABCMeta
    @abc.abstractmethod
    def validate(self, to_be_validated):
        """validate the input"""


class InputDataValidator(AbstractValidator):

    def validate(self, arg1, arg2, type_of_equation):
        if self._is_string(arg1) or self._is_string(arg2):
            raise Exciepcions.NotANumber
        if type_of_equation == 'divide':
            if arg2 == 0:
                raise ZeroDivisionError
        if type_of_equation == 'derivative':
            pass





    def _is_string(self, arg):
        return isinstance(arg, str)