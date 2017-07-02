# Unix_Epoch_Counter
The purpose of this Unix Epoch Counter is to celebrate 1.5 Billion Unix Epoch and future Timestamps.

![](https://media.giphy.com/media/T6H2loCrVb9mM/giphy.gif)

According to Wikipedia, [Unix time](https://en.wikipedia.org/wiki/Unix_time) (also known as POSIX time or epoch time) is a system for describing instants in time, defined as the number of seconds that have elapsed since 00:00:00 Coordinated Universal Time (UTC), Thursday, 1 January 1970, minus the number of leap seconds that have taken place since then.

This Python script contains a function called unix_countup() in [unix_periods.py](https://github.com/vdatasci/Unix_Epoch_Counter/blob/master/unix_period.py), which counts up to a unix time.

## Setup:
* Open Command Prompt
* Change the directory ([cd](https://en.wikipedia.org/wiki/Cd_(command))) to folder location of [unix_periods.py](https://github.com/vdatasci/Unix_Epoch_Counter/blob/master/unix_period.py) and [unix_counter.py](https://github.com/vdatasci/Unix_Epoch_Counter/blob/master/unix_counter.py).
* Type in ```python unix_counter.py --help'```



## Comand-Line Examples:
In the following examples, [unix_periods.py](https://github.com/vdatasci/Unix_Epoch_Counter/blob/master/unix_period.py) and [unix_counter.py](https://github.com/vdatasci/Unix_Epoch_Counter/blob/master/unix_counter.py) are stored in an USB thumb drive (F:). First we need to switch drives, then we can change the directory within the (F:) drive.

Example #1:
```cmd
F:
cd F:\\Python\\Projects\\Epoch
python unix_counter.py 1500000000 0.01 0
```

Example #2:
```cmd
F:
cd F:\\Python\\Projects\\Epoch
python unix_counter.py -p 1500000000 -m 0.01 -o 0
```

Example #3:
```cmd
F:
cd F:\\Python\\Projects\\Epoch
python unix_counter.py --party 1500000000 --moment 0.01 --offset 0
```
