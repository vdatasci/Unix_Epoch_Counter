# Unix_Epoch_Counter

![](http://i.imgur.com/H4PDROU.jpg)


The purpose of the Unix Epoch Counter is to celebrate 1.5 Billion Unix Epoch and future timestamps. The counter will be displayed on an [LED sign](https://scontent.fdet1-1.fna.fbcdn.net/v/t1.0-9/19366127_1563430300374880_9164840505946069472_n.jpg?oh=a2e3adc5bf063309edc0df470d8cf6bf&oe=59CBB2DF).


According to Wikipedia, [Unix time](https://en.wikipedia.org/wiki/Unix_time) (also known as POSIX time or epoch time) is a system for describing instants in time, defined as the number of seconds that have elapsed since 00:00:00 Coordinated Universal Time (UTC), Thursday, 1 January 1970, minus the number of leap seconds that have taken place since then.

The file called [unix_periods.py](https://github.com/vdatasci/Unix_Epoch_Counter/blob/master/unix_period.py) has a function called unix_countup() which counts up to a specified unix timestamp.

![](https://media.giphy.com/media/NuLThwEkFqhXO/giphy.gif)

## Setup:
* Download the files [here](https://github.com/vdatasci/Unix_Epoch_Counter/archive/master.zip).
* Open [Command Prompt](file:///C:\Windows\System32\cmd.exe)
* Change the directory ([cd](https://en.wikipedia.org/wiki/Cd_(command))) to folder location of [unix_periods.py](https://github.com/vdatasci/Unix_Epoch_Counter/blob/master/unix_period.py) and [unix_counter.py](https://github.com/vdatasci/Unix_Epoch_Counter/blob/master/unix_counter.py).
* Type in ```python unix_counter.py --help```



## Command-Line Examples:
In the following examples, [unix_periods.py](https://github.com/vdatasci/Unix_Epoch_Counter/blob/master/unix_period.py) and [unix_counter.py](https://github.com/vdatasci/Unix_Epoch_Counter/blob/master/unix_counter.py) are stored in an USB thumb drive (F:). 

To run the code, we need to switch drives and then change the directory within the (F:) drive.

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

#### Recorded Example:
![](http://i.imgur.com/rPiAmrx.gif)


#### Desired Results:
![](https://media.giphy.com/media/3KC2jD2QcBOSc/giphy.gif)

## About The Author:
[https://www.JoshingAroundBlog.WordPress.com/](https://www.JoshingAroundBlog.WordPress.com/)

[http://www.LinkedIn.com/in/Josh-Voss/](http://www.linkedin.com/in/josh-voss/)

[https://www.Twitter.com/VossDataScience](https://www.Twitter.com/VossDataScience)


## REMEMBER!

![](http://i.imgur.com/vmo1IYJ.jpg)
