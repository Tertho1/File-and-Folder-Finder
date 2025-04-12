# File and Folder Finder

A Python command line utility to search for files and folders across your system.

## Description

This tool allows you to search for files and folders on your computer by name, file extension, or both. It provides flexibility in where to search and what to search for, making it easy to locate misplaced files or explore your system.

## Features

- Search for files, folders, or both
- Search across multiple drives/paths
- Use wildcards in search patterns (e.g., `*.txt`)
- Filter search results by file extension
- Default to system-wide search if no path is specified

## Usage

1. Run the script:

   ```
   python searcher.py
   ```

2. Enter search criteria when prompted:

   - File or folder name (supports wildcards like `*.txt` or `document*`)
   - Starting search paths (comma-separated, e.g., `C:/Users, D:/Documents`)
   - Search type (`file`, `folder`, or `both`)
   - File extension filter (e.g., `.pdf`, `.docx`)

3. Wait for search results to appear.

## Examples

- Find all Python files: Enter `*.py` as the file name
- Find a specific document: Enter part of the file name like `budget`
- Find all text files in a specific folder: Enter `*.txt` as the name and specify the path

## Implementation Details

The script utilizes Python's built-in `os` module for filesystem navigation and `fnmatch` for efficient pattern matching. The implementation is platform-agnostic, supporting both Windows and Unix-like operating systems with consistent behavior.

## Requirements

- Python 3.x
- No external dependencies

## Installation

### Method 1: Clone the Repository

```bash
git clone https://github.com/yourusername/file-and-folder-finder.git
cd file-and-folder-finder
```

### Method 2: Download Source Directly

1. Download the source code from the repository
2. Extract the files to your preferred location
3. Navigate to the directory containing the script

### Running the Script

```bash
python main.py
```

## Notes

- System-wide searches can take considerable time, especially on systems with large storage capacity
- The script implements error handling to continue searching despite permission issues or other non-critical errors
- For optimal performance, specify search paths rather than performing system-wide searches


### Contributing

Contributions to improve the File and Folder Searcher are welcome! To contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a new Pull Request

### Reporting Issues

If you encounter any bugs or have feature requests, please open an issue on the GitHub repository with:

- A clear description of the problem or suggestion
- Steps to reproduce the issue (if applicable)
- Your operating system and Python version
- Any relevant error messages or screenshots

### License

This project is licensed under the MIT License - see the LICENSE file for details.
