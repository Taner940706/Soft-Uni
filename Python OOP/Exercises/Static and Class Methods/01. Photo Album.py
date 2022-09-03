from math import ceil


class PhotoAlbum:

    PHOTOS_PER_PAGES = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = self.__build_photos()

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = ceil(photos_count / PhotoAlbum.PHOTOS_PER_PAGES)
        return cls(pages)

    def add_photo(self, label: str):
        for row_idx in range(len(self.photos)):
            row = self.photos[row_idx]
            if len(row) < PhotoAlbum.PHOTOS_PER_PAGES:
                self.photos[row_idx].append(label)
                return f"{label} photo added successfully on page {row_idx + 1} slot {len(self.photos[row_idx])}"
        return "No more free slots"

    def display(self):
        separator = '-' * 11
        result = separator + '\n'
        for row in self.photos:
            result += ' '.join('[]' for _ in row) + '\n'
            result += separator + '\n'
        return result.strip()



    def __build_photos(self):
        result = []
        for _ in range(self.pages):
            result.append([])
        return result