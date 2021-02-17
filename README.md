[![GitHub license](https://img.shields.io/github/license/aaqibb13/Primality-Testing)](https://github.com/aaqibb13/Primality-Testing/blob/master/LICENSE) ![GitHub language count](https://img.shields.io/github/languages/count/aaqibb13/Primality-Testing?color=brightgreen)

# Primality-Testing:
This is the readme file for the various probabilistic primality testing algorithms implemented in Python, starting right from the fermat's test which is the basic and most oldest of the primality testing algorithms.

Primality testing algorithm's behave differently depending upon the integer ***n*** being fed to the primality testing algorithm:
* ` The answer is either:  n is a composite (not a prime) or`
* ` The answer is: n is a probable prime`

However, the first condition is always true, or the second condition is true with a high probability. Though, in rare cases, an integer might prompt a “prime” statement but lie, i.e., an incorrect answer is yielded. There, however is a way to deal with this sort of behavior.

Probabilistic algorithms are usually used in practical scenarios. These algorithms have another parameter **a** as input which is chosen at random. 
If a composite number **n** together with a parameter **a** yields the incorrect statement “Probable prime”, the test is repeated a second time with a different value for **a**. 
The general strategy is to test a prime candidate **n** so often with several different random values of **a** that the likelihood of the pair **(n,a)** lying every single time is sufficiently small, say, less than **2^(−80)**.

Remember that as soon as the statement **n is composite** occurs, we know with certainty that **n is not a prime** and we can discard it right there.

#### Caveat:

> **Probabilistic Primality Testing Algorithms are No-biased Monte Carlo algorithms which means that, when the algorithms output No, the answer is correct. Whereas the output Yes comes with some chances of error. In order for these algorithms to be useful, the error probabilities should be low** 

# Progress: 
- [x] Trial and Error 
- [x] Fermat Primality Test
- [ ] Miller–Rabin Test
- [ ] Solovay–Strassen Test
- [ ] Fibonacci Test
- [ ] Lucas Test

# References:
A brief description of the following tests can be found as follows: 

| Test                  | Wikipedia Description                                                                            |
| --------------------- | ------------------------------------------------------------------------------------------------ |
| Test #1               | [Fermat Primality Test](https://en.wikipedia.org/wiki/Fermat_primality_test)                     |
| Test #2               | [Miller-Rabin primality test](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test) |
| Test #3               | [Solovay-Strassen Test](https://en.wikipedia.org/wiki/Solovay%E2%80%93Strassen_primality_test)   |
| Test #4               | [Lucas Test](https://en.wikipedia.org/wiki/Lucas_primality_test)                                 |


## Purpose:
The purpose of this repository is to include all the primality testing algorithms so that one can suitably understand why Miller-Rabin is an ideal choice in most cryptographic applications where Primality testing plays a crucial role.

## To-do:
- [ ] Prepare a table with corresponding running times of these algorithms along with the class they belong to.
