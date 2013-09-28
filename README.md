Markov n-gram demo program  
 by Paul Ebreo

Inspired by Brit Cruise's Markov videos:  
https://www.khanacademy.org/math/applied-math/informationtheory/moderninfotheory/v/a-mathematical-theory-of-communication

Usage
----  
```
>>> from ngram import NGRAM
>>> NGRAM.generate(3, 'sample-hamlet.txt', 100)

mind to suffer the slings and arrows of outrageous fortune or to take arms again
st a sea of troubles and by opposing end them To die to sleep no more and by a s
leep to say we end the heart ache and the thousand natural shocks that flesh is
heir to tis a consummation devoutly to be wishd To die to sleep no more and by a
 sleep to say we end the heart ache and the thousand natural shocks that flesh i
s heir to tis a consummation devoutly to be wishd To die to sleep no more and by
 a sleep to


```

Bugs
----
I need to diagnose and fix the following error:
```
>>> NGRAM.generate(2, 'sample-hamlet.txt', 200)                                                                                                                                                                                                
Traceback (most recent call last):                                                                                                                                                                                                             
  File "<stdin>", line 1, in <module>                                                                                                                                                                                                          
  File "ngram.py", line 83, in generate                                                                                                                                                                                                        
    next_word = NGRAM.topword(1, cups[this_token])                                                                                                                                                                                             
KeyError: ('something', 'after')                                                                                                                                                                                                               
```
