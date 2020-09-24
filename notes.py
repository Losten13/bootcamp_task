class NoteManager:
    """
    A class for work with notes about author

    Attributes
    file_name : str
        name of files that contains notes
    notes: list of dict
        list of notes
    """

    def __init__(self, file_name):
        self.file_name = file_name
        self.notes = []
        self.read_notes()

    @staticmethod
    def create_note(author_name: str, note: str, rating: float) -> dict:
        """
        Create dict for note
        :param author_name: str
        :param note: str
        :param rating: str
        :return: dict
        """
        if rating > 1 or rating < 0:
            rating = 0.0
        return {'author_name': author_name, 'note': note, 'rating': rating}

    def __write_notes(self):
        """
        Write notes to file
        """
        with open(self.file_name, 'w') as f:
            for note in self.notes:
                for val in note.values():
                    f.write(f'{val},')
                f.write('\n')

    def add_note(self, author_name: str, note: str, rating: float) :
        """
        Add note to notes attribute
        :param author_name: str
        :param note: str
        :param rating: str
        """
        note = self.create_note(author_name, note, rating)
        self.notes.append(note)
        self.__write_notes()

    def read_notes(self) :
        """
        Read notes from target file
        """
        with open(self.file_name) as f:
            for line in f:
                data = line.split(',')
                note = self.create_note(data[0], data[1], float(data[2]))
                self.notes.append(note)
        f.close()

    def print_all(self):
        """
        Print all notes
        """
        for note in self.notes:
            for val in note.values():
                print(val)

    def get_highest_rating_author(self) -> str:
        """
        Get highest rating author name
        :return: highest rating author name
        """
        return max(self.notes, key=lambda note: note['rating'])['author_name']

    def get_lowest_rating_author(self) -> str:
        """
        Get lowest rating author name
        :return: highest rating author name
        """
        return min(self.notes, key=lambda note: note['rating'])['author_name']

    def get_average_authors_rating(self) -> float:
        """
        Get average rating of authors
        :return: average rating of authors
        """
        return sum([note['rating'] for note in self.notes]) / len(self.notes)
