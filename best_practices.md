 # Python development - Best practices
 This page highlights a list of best practices while programming in python.
 
 <!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#general">General</a>
    </li>
    <li>
      <a href="#loops">Loops</a>
    </li>
    <li>
        <a href="#collections">Collections</a>
    </li>
    <li>
        <a href="#strings">Strings</a>
    </li>
    <li>
        <a href="#conditions">Conditions</a>
    </li>
  </ol>
</details>

## General

<details>
 <summary>Import modules only when needed.</summary>
 <p>
 </p>
</details>

<details>
 <summary>Fail fast.</summary>
 <p>
 </p>
</details>

<details>
 <summary>Cache functions via decorator.</summary>
 <p>
 </p>
</details>

<details>
 <summary>Use built-in methods as much as possible.</summary>
 <p>
 sort()
 reduce()
 map()
 etc
 </p>
</details>

<details>
 <summary>Reduce function calls.</summary>
 <p>
  
 ```python
 import time
 x = 0
 def doit1(i):
     global x
     x = x + i

 list = range(100000)
 t = time.time()
 for i in list:
     doit1(i)

 print "%.3f" % (time.time()-t)
 ```
 vs.
 ```python
 import time
 x = 0
 def doit2(list):
     global x
     for i in list:
         x = x + i

 list = range(100000)
 t = time.time()
 doit2(list)
 ```
 </p>
 </details>

<details>
 <summary>Profile application. Especially after changing code.</summary>
 <p>
 </p>
</details>

## Loops

<details>
 <summary>Replace <code>range()</code> with <code>xrange()</code>.</summary>
 <p>
 `range()` loads all the numbers in memory, whereas `xrange()` returns a generator that lazily loads the next number when needed.
   ```python
   lol = 1243
   pop = 1323
   ```
 </p>
</details>

<details>
 <summary>Use <code>map()</code> instead of loops.</summary>
 <p>
  To use c compiled code instead of interpreted code.
 </p>
</details>

<details>
 <summary>Avoiding dots in loops i.e member resolution.</summary>
 <p>
 </p>
</details>

<details>
 <summary>Use local variables for loops instead of referring to global variables.</summary>
 <p>
 </p>
</details>

<details>
 <summary>Use list comprehension instead of loops.</summary>
 <p>
  
  
  ```python
   @time_it
   def square_numbers_using_for_loop(numbers: list) -> list:
       squared_numbers = list()
       for number in numbers:
           squared_numbers.append(number * number)
           return squared_numbers


   @time_it
   def square_numbers_using_list_comprehension(numbers: list) -> list:
       return [number * number for number in numbers]
   ```
 </p>
</details>

## Collections

<details>
 <summary>While generating data, consider using generators as opposed to collections.</summary>
 <p>
  As when using a collection like a list or set, all the elements need to be generated and stored in memory.
  Whereas, a generator lazily generates elements only when the iteration needs it
 </p>
</details>

<details>
 <summary>Initializing dict values, use <code>get()</code> with default value.</summary>
 <p>
 </p>
</details>

<details>
 <summary>Use sets when intersections and unions are needed.</summary>
 <p>
 </p>
</details>

## Strings

<details>
 <summary>Use <code>join()</code> for string concatenation instead of <code>+</code>.</summary>
 <p>
 </p>
</details>

## Conditions

<details>
 <summary>Use <code>in</code>.</summary>
 <p>
 </p>
</details>

<details>
 <summary>Prefer checking a long list as opposed to constructing a set.</summary>
 <p>
  
   ```python
   if animal in set(animals):

   if animal in animals:
   ```
 </p>
</details>


## References
[1] https://stackify.com/20-simple-python-performance-tuning-tips/ <br>
[2] https://wiki.python.org/moin/PythonSpeed/PerformanceTips
