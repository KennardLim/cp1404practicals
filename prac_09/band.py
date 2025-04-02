from prac_09.musician import Musician

class Band:

    def __init__(self, name=""):
        self.name = name
        self.members = []

    def __str__(self):
        return f"{self.name} ({", ".join([str(member) for member in self.members])})"

    def add(self, new_member):
        self.members.append(new_member)

    def play(self):
        return "\n".join([member.play() for member in self.members])
