import uuid
from datetime import datetime


class BaseModel:
    """A class that defines all common attributes for other
        classes and takes various methods"""

    def __init__(self):
        """initialzation of the class"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """function that returns the class sttributes as a string"""

        return f"[{self.__class__.__name__}] [{self.id}] {self.__dict__}"

    def save(self):
        """function to update the public instance updated_at"""

        self.updated_at = datetime.now()
        return (self.updated_at)

    def to_dict(self):
        """function to return a dictionary showing key value """

        work_obj = self.__dict__.copy()
        work_obj['updated_at'] = self.updated_at.isoformat()
        work_obj['created_at'] = self.created_at.isoformat()
        work_obj['__class__'] = self.__class__.__name__
        return work_obj

    def __init__(self, *args, **kwargs):
        """Initializes a BaseModel

        Args:
            *args: Tuple containing arguments
            **Kwargs: Keyword arguments.
        Raises: ValueError if __class__ is present iin kwargs
        """

        if __class__ in kwargs:
            raise ValueError("__class__ key present in **kwargs")

        if kwargs is None or not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

        else:
            if 'created_at' in kwargs:
                kwargs["created_at"] = datetime.now()
            if 'updated_at' in kwargs:
                kwargs["updated_at"] = datetime.now()

        self.__dict__.update(kwargs)
