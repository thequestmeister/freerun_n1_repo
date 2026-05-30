import os
import random
import hashlib


class TuringTerminal:

    def __init__(self):
        self.reset()

    def reset(self):
        self.session = hashlib.sha256(
            str(random.random()).encode()
        ).hexdigest()[:16]

    def load_key(self):

        rotor_files = [
            "data/rotor_a.dat",
            "data/rotor_b.dat",
            "data/rotor_c.dat"
        ]

        values = []

        for rotor in rotor_files:

            with open(rotor, "r") as f:

                nums = f.read().strip().split()

                values.extend(
                    chr(int(x))
                    for x in nums
                )

        return "".join(values)

    def banner(self):

        print("=" * 55)
        print("TURING CRYPTANALYSIS TERMINAL")
        print("=" * 55)
        print(f"Rotor Session: {self.session}")
        print()

    def challenge(self):

        print("Encrypted rotor groups discovered:")
        print()

        for rotor in [
            "data/rotor_a.dat",
            "data/rotor_b.dat",
            "data/rotor_c.dat"
        ]:

            with open(rotor) as f:
                print(f.read().strip())

        print()
        print("Historical note:")
        print("Recovered from wartime cryptanalysis archive.")
        print()

    def validate(self, candidate):

        expected = self.load_key()

        if candidate.strip().upper() == expected:

            print()
            print("[+] ACCESS GRANTED")
            print("[+] Historical archive unlocked")
            print()
            return True

        print()
        print("[-] INVALID ROTOR CONFIGURATION")
        print("[-] Session regenerated")
        print()

        self.reset()

        return False


def main():

    terminal = TuringTerminal()

    while True:

        terminal.banner()

        terminal.challenge()

        answer = input(
            "Enter reconstruction result: "
        )

        if terminal.validate(answer):
            break


if __name__ == "__main__":
    main()