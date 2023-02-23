from telnetlib import Telnet

class ON4KST:
    def __init__(self) -> None:
        self.username 

with Telnet('www.on4kst.info',23000) as on4kst:
    try:
        on4kst.read_until(b"Login:")
        on4kst.write(b"LY2EN\n")

        on4kst.read_until(b"Password:")
        on4kst.write(b"\n")

        response = on4kst.expect(b"Your choice           :", 1)
        if response[0] < 0:
            raise RuntimeError("Did not login")
        else:
            on4kst.write(b"2\n") 

    except:
        print("Unable to login")

    on4kst.interact()
