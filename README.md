# Archiver
A `tar` wrapper with Discord notification for basic archiving tasks.

```
# Install dependencies
pipenv install --ignore-pipfile

# Run
python main.py --src </path/to/source> --dst </path/to/destination> --archive --name <NAME>
```

*Note: Requires Discord webhook URL to be exported as an environment variable: `WEBHOK`*.
