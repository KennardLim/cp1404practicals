class Band:
    """A Band class consisting of musicians."""

    def __init__(self, name=""):
        """Construct a Band with a name and empty list of members."""
        self.name = name
        self.members = []

    def __str__(self):
        """Return a string representation of a Band."""
        return f"{self.name} ({", ".join([str(member) for member in self.members])})"

    def add(self, new_member):
        """Add a member to the band."""
        self.members.append(new_member)

    def play(self):
        """Returns a multi line string showing the members laying their first (or no) instrument."""
        return "\n".join([member.play() for member in self.members])
