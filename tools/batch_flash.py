from concurrent.futures import ThreadPoolExecutor
from backend.pyocd_backend import PyOCDBackend


def flash_one(uid, fw):
    b = PyOCDBackend()
    b.connect(uid)
    b.flash(fw)
    b.reset()
    b.disconnect()
    print(f"{uid} flashed")


def main():
    fw = "firmware.hex"
    uids = PyOCDBackend().list_probes()

    with ThreadPoolExecutor() as ex:
        for uid in uids:
            ex.submit(flash_one, uid, fw)


if __name__ == "__main__":
    main()
