# Secret-Sharing #

This is an implementation of an algorithm I'm writing as part of my cryptography paper for [MATH3302](http://www.uq.edu.au/study/course.html?course_code=MATH3302).

The goals of the algorithm are:

1. Create a secure password that is not susceptible to a dictionary attack,
2. Generate the password using secret-sharing based on easy-to-remember dictionary words,
3. Set up the secret-sharing so that the password is hard to generate even if you have all but one of the dictionary words used to generate the password.

These goals must be of equal-ish priority in the implementation of the algorithm.

The motivation behind this algorithm is the idea that it's easier to remember three or four regular words than it is to remember a secure password.


## Algorithm, Mark I #

- User inputs a length `n` they want their password to be and (optionally) how many words they want their password to be based on `l` (default is 3).
- Program chooses `l` random words from the dictionary, ensuring that at least one of them is of length `n`.
- Program "adds" the words together (mod 40). This gives us a secure password and the `l` words that generate it.

## Notes #
- Assumptions for a Brute-Force Attack: The attacker knows the length of the password you're generating. He knows `l-1` of the shares. He has the dictionary you're using.

- Smart Brute-Force Attack: Assuming the attacker knows `l-1` words and he has the dictionary you're using, he only has to test each word in the dictionary to crack the password (41238 combinations).
- Dumb Brute-Force Attack: Assuming the attacker knows `l-1` words and he doesn't know to use a dictionary, he has to test 40^n combinations. For a password of length 10, this is 1.048576 x 10^16 combinations

## Things to consider at each phase #

- Does putting the non-alphanumeric characters not at the end make the password more secure?
- If an attacker knows all but one of the shares, how long does it take to brute-force the password? (Repeated brute-force tests)
- What kind of effect does changing the length of the password and the number of shares have on the security of the secret-sharing?
- Where's the sweet spot in terms of brute-force attack versus easy-to-remember (i.e. short, not many) shares?
