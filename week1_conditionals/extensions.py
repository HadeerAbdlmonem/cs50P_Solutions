"""Guess a file's MIME type from its extension."""

EXTENSION_TO_MEDIA_TYPE = {
    (".jpg", ".jpeg"): "image/jpeg",
    (".pdf",): "application/pdf",
    (".zip",): "application/zip",
    (".gif",): "image/gif",
    (".png",): "image/png",
}


def main():
    filename = input("Enter the name of your file: ").lower().strip()
    print(get_media_type(filename))


def get_media_type(filename):
    for extensions, media_type in EXTENSION_TO_MEDIA_TYPE.items():
        if filename.endswith(extensions):
            return media_type
    return "application/octet-stream"


if __name__ == "__main__":
    main()
