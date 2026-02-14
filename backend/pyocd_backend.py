from pyocd.core.helpers import ConnectHelper
from pyocd.flash.file_programmer import FileProgrammer
from .backend import ProgrammerBackend


class PyOCDBackend(ProgrammerBackend):

    def __init__(self):
        self.session = None
        self.target = None

    def list_probes(self):
        probes = ConnectHelper.get_all_connected_probes()
        return [p.unique_id for p in probes]

    def connect(self, probe_uid=None):
        self.session = ConnectHelper.session_with_chosen_probe(
            unique_id=probe_uid       
        )

        if self.session is None:
            raise RuntimeError("No probe found")

        self.session.open()
        self.target = self.session.target

    def flash(self, firmware):
        FileProgrammer(self.session).program(firmware)

    def erase(self, mode="chip"):
        self.target.mass_erase()

    def reset(self):
        self.target.reset()

    def disconnect(self):
        if self.session:
            self.session.close()
            self.session = None
            self.target = None

