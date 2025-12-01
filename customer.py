class Customer:
    def __init__(self, name: str):
        self.name = name  # triggers setter validation

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        # Validate type
        if not isinstance(value, str):
            raise TypeError("Customer name must be a string.")
        # Validate length (1-15 chars)
        if not (1 <= len(value) <= 15):
            raise ValueError("Customer name must be between 1 and 15 characters.")
        self._name = value
