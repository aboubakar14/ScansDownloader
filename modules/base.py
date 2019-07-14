from abc import ABC, abstractmethod


class Base(ABC):
    """ Base class for modules. """

    @abstractmethod
    def download(self):
        """ Downloads scans method. This method must be defined. """
        pass
