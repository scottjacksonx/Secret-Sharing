# Secret-Sharing #

This is an implementation of an algorithm I'm writing as part of my cryptography paper for [MATH3302](http://www.uq.edu.au/study/course.html?course_code=MATH3302).

The goals of the algorithm are:

1. Create a secure password that is not susceptible to a dictionary attack,
2. Generate the password using secret-sharing based on easy-to-remember dictionary words,
3. Set up the secret-sharing so that the password is hard to generate even if you have all but one of the dictionary words used to generate the password.

These goals must be of equal-ish priority in the implementation of the algorithm.

The motivation behind this algorithm is the idea that it's easier to remember three or four regular words than it is to remember a secure password.


## Algorithm, Mark I ##

An alphabet of {a-z} U {0-9 \ 1} U {-, &, _, .< *, #} is used to create the password. The number `1` is eliminated for readability's sake ('1' and 'l' can look very similar). The alphabet therefore has a length of 40.

- The user inputs a length `n` they want their password to be and (optionally) how many words they want their password to be based on `l` (default is 3).
- The algorithm chooses `l` random words from the dictionary, ensuring that at least one of them is of length `n`.
- The algorithm "adds" the words together (letterwise mod 40). This gives us a secure password and the `l` words that generate it.

## Notes #

Assumptions for a Brute-Force Attack: The attacker knows the length of the password you're generating. He knows `l-1` of the shares. He has the exact same dictionary that you're using.

- Smart Brute-Force Attack: Assuming the attacker knows `l-1` words and he has the dictionary you're using, he only has to test each word in the dictionary to crack the password (41238 combinations).
- Dumb Brute-Force Attack: Assuming the attacker knows `l-1` words and he doesn't have your dictionary, he has to test 40^n combinations. For a password of length 10, this is 1.048576 x 10^16 combinations.
