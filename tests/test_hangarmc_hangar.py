from hangarmc_hangar import __version__
from hangarmc_hangar.hangar import Hangar


def test_version():
    assert __version__ == '0.1.0'


def test_project():
    hangar = Hangar()
    print(hangar.get_project("OskarsMC-Plugins", "message"))
