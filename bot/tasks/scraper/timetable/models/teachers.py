from .teacher import Teacher

class Teachers:
    def __init__(self, teachers_path: str):
        self._teachers_path = teachers_path
        self.teachers = []
        self.teachers_from_abbreviation = {}
        self.teachers_from_name = {}
        self._load_teachers()

    def _load_teachers(self) -> None:
        """Loads teachers from the file and saves them to [teachers]."""
        # Opens the .txt file from which informations about teachers are loaded.
        data = None
        with open(self._teachers_path) as data_file:
            data = data_file.readlines()
        self.teachers.clear()
        # Fills the teachers' array.
        for line in data:
            split_line = line.split()
            full_name = " ".join([split_line[1], split_line[0]])
            phone = " ".join([split_line[4], split_line[5], split_line[6]])
            self.teachers.append(Teacher(
                first_name=split_line[1],
                second_name=split_line[0],
                full_name=full_name,
                abbreviation=split_line[8],
                email=split_line[3],
                phone=phone,
                room=split_line[7],
                url=split_line[9]))
        # Fills the dictionary.
        for teacher in self.teachers:
            self.teachers_from_abbreviation[teacher.abbreviation] = teacher
            self.teachers_from_name[teacher.full_name] = teacher

