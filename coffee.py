class Coffee:
    """Represents a coffee item with a name."""

    def __init__(self, name: str):
        """Initialize a Coffee instance with a name."""
        self.name = name

    @property
    def name(self) -> str:
        """Get the coffee name."""
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """Set the coffee name with validation."""
        # Validate type
        if not isinstance(value, str):
            raise TypeError("Coffee name must be a string.")
        # Validate minimum length (3+ chars)
        if len(value) < 3:
            raise ValueError("Coffee name must be at least 3 characters.")
        self._name = value
