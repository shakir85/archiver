# Archiver
A `tar` wrapper with Discord notification for basic archiving tasks.


Requirements:
- Discord webhook environment variable: `WEBHOK=<URL>`.
- Python 3.10 (or run `pipenv --python /path/to/bin/python3`)


```
# Install dependencies
pipenv install --ignore-pipfile

# Run
python main.py --src </path/to/source> --dst </path/to/destination> --archive --name <NAME>
```

