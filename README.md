# road-compare

Simple script to compare Beeminder roads

## Installation

```bash
chmod +x main.py
python3 -m pip install --user -r requirements.txt
```

## Usage

Script accepts two data sources as arguments, which can be URLs and/or local file paths.

```bash
./main.py https://www.beeminder.com/user/before.json https://www.beeminder.com/user/after.json
./main.py before.json after.json
```

### Docker

```bash
docker-compose run app ./main.py before.json after.json
```

## Results

```bash
$ ./main.py https://www.beeminder.com/user/before.json https://www.beeminder.com/user/after.json
2019-01-01 – 2019-11-10: True
2019-11-11 – 2019-11-23: False
2019-11-24 – 2019-12-31: True

FAILED
```

## Upgrade requirements

```bash
python3 -m pip install --upgrade -r requirements.txt
```