 # Best practices
 This page highlights a list of best practices while programming in python.
 
 <!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#loops">Loops</a>
    </li>
    <li>
        <a href="#lists">Lists</a>
    </li>
    <li>
        <a href="#strings">Strings</a>
    </li>
  </ol>
</details>

## Loops

## Lists

## Strings
 
 ### While generating data, consider using generators as opposed to collections.
 As when using a collection like a list or set, all the elements need to be generated and stored in memory.
 Whereas, a generator lazily generates elements only when the iteration needs it.
 
 ### Replace `range()` with `xrange()`.
 `range()` loads all the numbers in memory, whereas `xrange()` returns a generator that lazily loads the next number when needed.
   ```
   lol = 1243
   pop = 1323
   ```
   
 ### Use `in`.  
   
 ### Use `join()` for string concatenation instead of `+`.  

 ### Import modules only when needed.  
 
 ### Fail fast.
 
 ### Cache functionlls via decorator.
 
 ### Use map() instead of loops
 To use c compiled code instead of interpreted code.
 
 ### Avoiding dots in loops i.e member resolution. 
 
 ### Use local variables for loops instead of referring to Global variables.
 
 ### Initializing dict values, use get() with default value.
 
 ### Use in-built methods as much as possible
 sort()
 reduce()
 map()
 etc
 
 ### Prefer checking a long list as opposed to constructing a set.
 ```
 if animal in set(animals):
 
 if animal in animals:
 ```

 ### Reduce function calls.
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

 vs.

 import time
 x = 0
 def doit2(list):
     global x
     for i in list:
         x = x + i

 list = range(100000)
 t = time.time()
 doit2(list)
 
 ### Profile application. Especially after changing code.
 
 ### Use list comprehension instead of loops.
 
 ### Use sets when intersections and unions are needed.

   
   
## References
[1] https://stackify.com/20-simple-python-performance-tuning-tips/ <br>
[2] https://wiki.python.org/moin/PythonSpeed/PerformanceTips
