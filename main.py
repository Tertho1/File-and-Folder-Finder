import os
import fnmatch


def find_items(name, start_paths=None, search_type="both", file_extension=None):

    if start_paths is None or len(start_paths) == 0:
        start_paths = []
        if os.name == "nt":
            start_paths = [
                f"{chr(65 + i)}:/"
                for i in range(26)
                if os.path.exists(f"{chr(65 + i)}:/")
            ]
        else:
            start_paths = ["/"]

    results = []
    print(start_paths)
    for path in start_paths:
        for root, dirs, files in os.walk(path, onerror=lambda e: None):

            search_items = []
            if search_type in ("file", "both"):
                search_items.extend(files)
            if search_type in ("folder", "both"):
                search_items.extend(dirs)

            for item in search_items:
                item_path = os.path.join(root, item)

                if (
                    fnmatch.fnmatch(item, name)
                    or (file_extension and item.endswith(file_extension))
                    or (not file_extension and item.startswith(name))
                ):
                    results.append(item_path)

    return results


if __name__ == "__main__":
    search_name = input(
        "Enter the file or folder name (wildcards allowed, e.g., '*.txt'): "
    )
    search_paths = (
        input(
            "Enter starting path (comma-separated e.g. C:/, E:/Games, leave blank for system-wide): "
        )
        .strip()
        .split(",")
    )
    print(search_paths)
    search_paths = [path.strip() for path in search_paths if path.strip()]
    print(search_paths)
    if not search_paths:
        search_paths = None

    search_type = (
        input("Search for 'file', 'folder', or 'both' (default: both): ")
        .strip()
        .lower()
        or "both"
    )
    file_ext = (
        input(
            "Filter by file extension (e.g., .txt, leave blank for all types): "
        ).strip()
        or None
    )

    print("\nSearching... This may take some time.")
    found_items = find_items(search_name, search_paths, search_type, file_ext)

    if found_items:
        print("\nItems found:")
        for item_path in found_items:
            print(item_path)
    else:
        print("\nNo items found matching the criteria.")
