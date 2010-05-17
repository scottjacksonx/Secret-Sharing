# Secret-Sharing #

This is an implementation of an algorithm I'm writing as part of my cryptography paper for [MATH3302](http://www.uq.edu.au/study/course.html?course_code=MATH3302).


## Algorithm, Mark I #

- User inputs a length `n` they want their password to be and (optionally) how many words they want their password to be based on `l` (default is 3).
- Program chooses `l` random words from the dictionary, ensuring that at least one of them is of length `n`.
- Program "adds" the words together (mod 40). This gives us a secure password and the `l` words that generate it.

## Notes #

- Brute-Force Attack: Assuming the attacker knows `l - 1` words, they only have to test each word in the dictionary to crack the password (41238).

## Things to consider at each phase #

- Does putting the non-alphanumeric characters not at the end make the password more secure?
- If an attacker knows all but one of the shares, how long does it take to brute-force the password? (Repeated brute-force tests)
- What kind of effect does changing the length of the password and the number of shares have on the security of the secret-sharing?
- Where's the sweet spot in terms of brute-force attack versus easy-to-remember (i.e. short, not many) shares?
