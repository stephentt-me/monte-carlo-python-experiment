# Monte Carlo and Python benchmark

This repo is an experiment about GIL, multiprocess vs thread, CPython vs PyPy.

## Method

By trying to calculate Pi number by using Monte Carlo method. Implemented with:
* Multiprocessing
* Threading
* "Normal"

And compare the result (time executed).

## Usage

Clone this repo.

```
<python implementation> monte_carlo.py <mode>
```

* With `<mode>` is: `normal`, `multiprocess`, `thread`
* With `<python implementation>` can be: CPython 3 (`python3`) or PyPy 3 `pypy3`.

## Sample Result

_A non-scientific experiment I ran on my computer. And yes, I know 2 version of CPython and PyPy is not the same. I will do it agan when have time._

CPython

```
➜ python monte_carlo.py normal 
3.14154884
Executed time: 30.305227756500244

➜ python monte_carlo.py multiprocess
3.14140592
Executed time: 16.27352023124695

➜ python monte_carlo.py thread 
3.14141776
Executed time: 46.7792592048645
```

```
➜ python3  --version 
Python 3.7.3
```

PyPy

```
➜ pypy3 monte_carlo.py normal  
3.14184992
Executed time: 4.59272837638855s

➜ pypy3 monte_carlo.py multiprocess                      
3.14170188
Executed time: 2.0504963397979736s

➜ pypy3 monte_carlo.py thread                             
3.14140112
Executed time: 8.281656265258789s
```

```
➜ pypy3 --version              
Python 3.6.1 (de061d87e39c7df4e436974096d7982c676a859d, Apr 01 2019, 15:02:06)
[PyPy 7.1.0-beta0 with GCC 8.2.1 20181127]
```