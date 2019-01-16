# Auto-reply for WeChat

This repo is mainly for me to record some problems I had while building this autoreply bot.

#### Problems:

* How to run a function at a certain time. For example, when it's 13:05-14:25, Tuesday, my bot should reply a specific course name.

  * ~~Possible solution:~~

    ~~Use Python `schedule`. Define several functions. Start a certain function at a certain time, and stop it at another time.~~
  * Current solution(kind of brute force, waiting for improvement):
    
    Just manually use `if` to compare the receive time and the course time.
  

* How to compare the `msg.receive_time` ?

  * Possible solution:

    Store `start_time` and `end_time` as time objects. Dates are not needed here, so I can create another time object

     `receive_time = time(msg.receive_time.hour,`

    `msg.receive_time.minute)`

#### What I learned:

* Add multiple values to a list, use `extend((x, y, z))`

* `datetime.time` objects can't be compared with `datetime.datetime` objects

* `defaultdict` is a great tool for creating `key:[val1, val2, val3..]`  pairs in a dictionary

  ```python
  >>>from collections import defaultdict
  >>>food_list = 'spam spam spam spam spam spam eggs spam'.split()
  >>> food_count = defaultdict(int) # default value of int is 0
  >>> for food in food_list:
  ...     food_count[food] += 1 # increment element's value by 1
  ...
  defaultdict(<type 'int'>, {'eggs': 1, 'spam': 7})
  ```
