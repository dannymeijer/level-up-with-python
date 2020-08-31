"""
You are given a list of files.
You need to sort this list by the file extension.
The files with the same extension should be sorted by name.

Some possible cases:
 - Filename cannot be an empty string;
 - Files without the extension should go before the files with one;
 - Filename ".config" has an empty extension and a name ".config";
 - Filename "config." has an empty extension and a name "config.";
 - Filename "table.imp.xls" has an extension "xls" and a name "table.imp";
 - Filename ".imp.xls" has an extension "xls" and a name ".imp".

Input: A list of filenames.
Output: A list of filenames.

"""


from typing import List
from pathlib import Path
from collections import namedtuple
import itertools

flatten = itertools.chain.from_iterable


def get_extension(file_name: str):
    """ Taken from / inspired by pathlib.Path.suffix """
    i = file_name.rfind(".")
    return file_name[i:] if 0 < i < len(file_name) - 1 else ""


def sort_by_ext(files: List[str]) -> List[str]:

    # # Using plain python with pathlib.Path
    # #  with a namedtuple thrown in for legibility
    # File = namedtuple("File", ["name", "ext"])
    # files_with_ext = [File(name=file, ext=Path(file).suffix) for file in files]
    #
    # # extensions = sorted(set([file.ext for file in files_with_ext]))
    # result = []
    # for ext in extensions:
    #     result.extend(sorted([
    #         file.name for file in files_with_ext if file.ext == ext
    #     ]))

    # # Using nested comprehension with 'flatten' taken from itertools
    # #  with a namedtuple thrown in for legibility
    # #  using pathlib.Path.suffix
    # File = namedtuple("File", ["name", "ext"])
    # files_with_ext = [File(name=file, ext=Path(file).suffix) for file in files]
    # result = list(
    #     itertools.chain.from_iterable(  # flatten function
    #         [
    #             sorted([file.name for file in files_with_ext if file.ext == ext])
    #             for ext in sorted(set([file.ext for file in files_with_ext]))
    #         ]
    #     )
    # )

    # Using nested comprehension with 'flatten' taken from itertools
    #  avoiding pathlib library
    result = list(
        itertools.chain.from_iterable(
            [
                # sorting files with the same extension
                sorted([file for file in files if get_extension(file) == ext])
                for ext in sorted(set([get_extension(file) for file in files]))
            ]
        )
    )
    return result


if __name__ == "__main__":
    print("Example:")
    print(sort_by_ext(["1.cad", "1.bat", "1.aa"]))
    print(sort_by_ext(["1.cad", "1.bat", "1.aa"]))
    print(sort_by_ext([".config", "config.", "a.config", "b.config", "table.imp.xls"]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sort_by_ext(["1.cad", "1.bat", "1.aa"]) == ["1.aa", "1.bat", "1.cad"]
    assert sort_by_ext(["1.cad", "1.bat", "1.aa", "2.bat"]) == [
        "1.aa",
        "1.bat",
        "2.bat",
        "1.cad",
    ]
    assert sort_by_ext(["1.cad", "1.bat", "1.aa", ".bat"]) == [
        ".bat",
        "1.aa",
        "1.bat",
        "1.cad",
    ]
    assert sort_by_ext(["1.cad", "1.bat", ".aa", ".bat"]) == [
        ".aa",
        ".bat",
        "1.bat",
        "1.cad",
    ]
    assert sort_by_ext(["1.cad", "1.", "1.aa"]) == ["1.", "1.aa", "1.cad"]
    assert sort_by_ext(["1.cad", "1.bat", "1.aa", "1.aa.doc"]) == [
        "1.aa",
        "1.bat",
        "1.cad",
        "1.aa.doc",
    ]
    assert sort_by_ext(["1.cad", "1.bat", "1.aa", ".aa.doc"]) == [
        "1.aa",
        "1.bat",
        "1.cad",
        ".aa.doc",
    ]
