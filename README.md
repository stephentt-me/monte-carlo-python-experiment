# Monte Carlo and a story about locking

This repo is and experiment about Python global locking.

## Method

By trying to calculate Pi number by using Monte Carlo method. Implement with:
* Multiprocessing
* Threading
* 'Normal'

And compare the result (time executed).

## Usage

Clone this repo.

```
python monte_carlo.py <mode>
```
With mode: `normal`, `multiprocess`, `thread`

## Sample Result

_in my machine_

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