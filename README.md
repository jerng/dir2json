# dir2json
Crawls a directory, infers metadata about every file, saves it as a JSON object.

# Implementation
Currently this is code, for a Python interpreter, of a [Zeppelin](https://zeppelin.apache.org/) notebook, which also uses [tika-python](https://github.com/chrismattmann/tika-python) for [Tika](https://tika.apache.org/).
- `docker run -i -t -p 8080:8080 -v ~/folder_on_host:/hostdata apache/zeppelin:0.8.1`

# Motivation
Palantir doesn't offer a B2C service. I want to first extract superficial metadata from a body of files, and then more complex inferences from the same. All this can be stored in a database for further processing.
