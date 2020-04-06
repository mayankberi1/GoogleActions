class Extension(dict):
    """
    {
        "@type": string,
        field1: ...,
        ...
    }
    """

    def __init__(self, extension_type: str, **fields):
        super().__init__()

        if extension_type is not None:
            self['@type'] = extension_type

        self.add_fields(**fields)

    def add_fields(self, **kwargs) -> dict:
        self.update(kwargs)

        return self
