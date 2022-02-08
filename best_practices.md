 # Python development - Best practices
 This page highlights a list of best practices while programming in python.
 
 - The metrics illustrated in the examples should be taken with a pinch of salt as it doesn't
 exclude thread sleep time.
 - This is fragment of my experience and not a comprehensive guide.
 
 <!-- TABLE OF CONTENTS -->
<details open="open">
  Table of Contents
  <ol>
     <li> <a href="#general">General</a> </li>
     <li> <a href="#loops">Loops</a> </li>
     <li> <a href="#collections">Collections</a> </li>
     <li> <a href="#strings">Strings</a> </li>
     <li> <a href="#conditions">Conditions</a> </li>
  </ol>
</details>

## General
 - <a href="wiki/general/fail_fast.py">Fail fast.</a>

 - <a href="wiki/general/lru_cache.py">Cache functions via decorator.</a>

 - Prefer built-in methods and keywords unless performance gain is worth the effort. Eg: <code>sort()</code>,
 <code>reduce()</code>,
 <code>map()</code>
 etc.

 - After code changes:
    - <details>Run unit tests.</details>
    - Test code coverage.
    - Profile application performance before and after the change.
      <p>

       ```bash
       $ python3.9 -m cProfile wiki/general/import_modules.py | awk 'NR<8 || /import_modules/'
       Check for a standard function call: 235.19015312194824 ms
       Check for a standard function call: 0.0026226043701171875 ms
              155065 function calls (149795 primitive calls) in 0.235 seconds
        Ordered by: standard name
        ncalls  tottime  percall  cumtime  percall filename:lineno(function)
             1    0.000    0.000    0.236    0.236 import_modules.py:1(<module>)
             2    0.000    0.000    0.235    0.118 import_modules.py:9(import_check)
       ```
      </p>
    - Run static code analysis.
 
 - [Zen 🧘](wiki/general/zen.py).

## Loops
 - In python 2.7, <code>range()</code> VS <code>xrange()</code>. <br>
<code>range()</code> computes all the values before iteration. <br>
<code>xrange()</code> does lazy evaluation i.e. computes values during iteration.
 - <a href="wiki/loops/loops_vs_list_comprehension_vs_map.py">for loops VS list comprehension VS <code>map()</code>
</a>
 - Avoiding dots in loops i.e member resolution.

 - Use local variables for loops instead of referring to global variables.


## Collections
 - While creating a collection of objects, <b> consider using [generators](wiki/loops/generator.py) as opposed to collections </b>, especially when the objects aren't 
   expensive to generate.<br>
    <pre>
    As when using a collection like a list or set, all the elements need to be generated and stored in memory.
    Whereas, a generator lazily generates elements only when the iteration needs it.
    </pre>

 - Initializing dict values, use <code>get()</code> with default value.

 - Use sets when intersections and unions are needed.


## Conditions
 - [Use <code>in</code>](wiki/conditions/in_keyword.py).
 - [Short circuiting VS Regular logical operators](wiki/conditions/logical_operators.py#36).

## Testing
 - Keep assertions as specific as possible.

## References
[1] https://stackify.com/20-simple-python-performance-tuning-tips/ <br>
[2] https://wiki.python.org/moin/PythonSpeed/PerformanceTips
[3] https://www.python.org/dev/peps/pep-0020/
