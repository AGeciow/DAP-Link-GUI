class ProgrammerBackend:
    def list_probes(self):
        raise NotImplementedError

    def connect(self, probe_uid=None):
        raise NotImplementedError

    def flash(self, firmware):
        raise NotImplementedError

    def erase(self, mode="chip"):
        raise NotImplementedError

    def reset(self):
        raise NotImplementedError

    def disconnect(self):
        raise NotImplementedError
