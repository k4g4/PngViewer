from io import BufferedReader


HEADER: bytes = b"\x89PNG\r\n\x1a\n"

CHUNK_LENGTH_LEN: int = 4
CHUNK_TYPE_LEN: int = 4


class PngReaderException(Exception):
    """An error occurred while reading the PNG file."""
    pass


class PngReader:
    """Reads and parses a PNG image file."""

    def __init__(self, png_file: str) -> None:
        self._png: BufferedReader = open(png_file, "rb")

        header: bytes = self._png.read(len(HEADER))
        if header != HEADER:
            raise PngReaderException("Improper header in file.")

        self._chunks: dict[str, bytes] = {}


    @property
    def width(self) -> int:
        return 0


    @property
    def height(self) -> int:
        return 0


    def _read(self, size: int) -> bytes:
        b: bytes = self._png.read(size)
        if 0 < len(b) < size:
            raise PngReaderException(f"Failed to read {size} bytes from file. Only {len(b)} bytes read.")


    def _read_chunk(self) -> bool:
        """Reads a chunk and adds its contents to the _chunks dict.
           Returns False if there is no data left to read."""
        chunk_length_field: bytes = self._read(CHUNK_LENGTH_LEN)
        if not chunk_length_field:
            return False
        chunk_length: int = int.from_bytes(chunk_length_field, "big")

        chunk_type_field: bytes = self._read(CHUNK_TYPE_LEN)
        if not chunk_type_field.isalpha():
            raise PngReaderException("Found improper bytes in chunk type.")
        chunk_type: str = chunk_type_field.decode()

        chunk_data: bytes = self._read(chunk_length)
        
        self._chunks[chunk_type] = chunk_data

        return True