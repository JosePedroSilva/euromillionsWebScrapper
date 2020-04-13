# Euromillions matcher
Webscrapping to check euromillions key results

## Requirements
Python 3.6+, python-pip, virtualenv

```
$ git clone https://github.com/JosePedroSilva/euromillionsWebScrapper.git

$ cd euromillionsWebScrapper
```

Create virtual environment
```
$ python3 -m venv env

$ source env/bin/activate

(env) $ _
```

Install all necessary dependencies
```
$ pip install -r requirements.txt
```

To check to your key played change the variables: 
- nums_played
- stars_played

```python
nums_played = [1, 2 ,20, 45, 46]
stars_played = [2, 4]
```

To run just execute euroApp.py
```
(env) $ python euroApp.py
```