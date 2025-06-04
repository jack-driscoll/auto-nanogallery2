# auto-nanogallery2
Automatically generate thumbnails, add image information, slugify files, and create gallery.json.

# Donations?

Did I save you a whole bunch of time?  Time is $$ and I am poor.  Please contribute if you are able https://ko-fi.com/s/364cd6b5af

# Instructions

Does what it says on the tin.  If you don't specify anything on the CLI, it will assume: 

- 300x300px thumbs
- location of images: ./images/
- location for thumbs: ./thumbs/
- adds image # for description, and `00-filename` for title
- output JSON file ./gallery.json

```
usage: make-slugged-gallery.py [-h] [--images IMAGES] [--thumbs THUMBS]
                               [--output OUTPUT] [--size WIDTH HEIGHT]

Generate a nanogallery2-compatible gallery.json with thumbnails.

options:
  -h, --help           show this help message and exit
  --images IMAGES      Directory containing input images (default: images)
  --thumbs THUMBS      Directory to save thumbnails (default: thumbs)
  --output OUTPUT      Output JSON file (default: gallery.json)
  --size WIDTH HEIGHT  Thumbnail size as WIDTH HEIGHT (default: 300 300)

USE: python make-slugged-gallery.py [--images DIR] [--thumbs DIR] [--output
FILE] [--size WIDTH HEIGHT]
```
