from collections import OrderedDict

class ArtGalleryDisplay:
    def __init__(self, capacity):
        """
        Initialize the ArtGalleryDisplay with a given capacity.
        """
        self.capacity = capacity
        self.artworks = OrderedDict()  # To maintain insertion order and handle duplicates efficiently

    def add_artwork(self, artwork):
        """
        Add an artwork to the gallery. If the artwork already exists,
        move it to the end (most recent). If the capacity is exceeded,
        remove the oldest artwork.
        """
        if artwork in self.artworks:
            # Move the existing artwork to the end
            self.artworks.move_to_end(artwork)
        else:
            if len(self.artworks) == self.capacity:
                # Remove the oldest artwork
                removed_artwork = self.artworks.popitem(last=False)
                print(f"Removed artwork: {removed_artwork[0]}")
            # Add the new artwork
            self.artworks[artwork] = True

    def display_artworks(self):
        """
        Display the artworks currently in the gallery.
        """
        if not self.artworks:
            print("The gallery is empty.")
        else:
            print("Artworks on display:")
            for artwork in self.artworks.keys():
                print(f"- {artwork}")


# Driver Code
art_gallery_display = ArtGalleryDisplay(capacity=6)
artworks = [
    "Sunset Over the Lake",
    "Abstract Dreams",
    "Cityscape at Dusk",
    "Portrait of the Artist",
    "Golden Fields",
    "Mystic Mountains",
    "Abstract Dreams",
    "Twilight Reflections",
    "Sunset Over the Lake",
    "Harmony in Blue"
]

for artwork in artworks:
    art_gallery_display.add_artwork(artwork)

art_gallery_display.display_artworks()
