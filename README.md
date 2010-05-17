# Secret-Sharing #

This is an implementation of an algorithm I'm writing as part of my cryptography paper for [MATH3302](http://www.uq.edu.au/study/course.html?course_code=MATH3302).

The goals of the algorithm are:

1. Create a secure password that is not susceptible to a dictionary attack,
2. Generate the password using secret-sharing based on easy-to-remember dictionary words,
3. Set up the secret-sharing so that the password is hard to generate even if you have all but one of the dictionary words used to generate the password.

These goals are of equal-ish priority in the implementation of the algorithm.

The motivation behind this algorithm is the idea that it's easier to remember three or four regular words than it is to remember a secure password.


## Algorithm, Mark I ##

An alphabet of `{a-z} U {0-9 \ 1} U {-, &, _, ., *, #, '}` is used to create the password. The number `1` is eliminated for the sake of readability ('1' and 'l' can look very similar). The alphabet therefore has a length of 42.

- The user inputs a length `n` they want their password to be and (optionally) how many words they want their password to be based on `l` (default is 3).
- The algorithm chooses `l` random words (shares) from the dictionary, ensuring that at least one of them is of length `n`.
- The algorithm "adds" the words together (letterwise mod 42). This gives us a secure password and the `l` words that generate it. If an attacker has < `l` words, he knows as much about the password as if he had 0 words.

## Brute-Force Attack #

Assumptions for a Brute-Force Attack: The attacker knows the length of the password you're generating. He knows `l-1` of the shares.

- **Brute-Force Attack**: Assuming the attacker knows `l-1` shares, he knows there is one share he doesn't have and that that share is of length at most `n`. Therefore, he has to test 42^n combinations (the same amount as if he knew 0 shares). For a password of length 10, this is 1.708019812 x 10^16 combinations.
- **Super Brute-Force Attack Turbo**: Assuming the attacker knows `l-1` shares *and he knows the exact dictionary you're using*, he only has to test each word in the dictionary to crack the password (41238 combinations in the implementation provided here). However, if the attacker has access to the dictionary you're using, he obviously already has access to something of yours that's password-protected (assuming you kept the dictionary somewhere password-protected), and thus probably doesn't need to figure out your password.



## Notes ##

The size of the dictionary is the most obvious bottleneck in the security of this secret-sharing system. Since one of the goals of the algorithm is to use regular (i.e. easy-to-remember) words to form a secure password, it's no surprise that this convenience is its major problem. The following are steps one could take to improve the security of the secret-sharing system:

- Include more obscure words in your dictionary. The downside of this is that obscure words are hard to remember. The purpose of the algorithm is to only remember things that are *easy* to remember. If you're going to go to the trouble of remembering an archaic word like "[absquatulate](http://www.kokogiak.com/logolepsy/ow_a.html)," you may as well remember a secure password.
- Make up your own words and include them in your dictionary. "Flabble-dabble-robocop" is a great example. Making up your own words decreases the chance that the attacker will be able to find the exact dictionary you're using to generate your passwords.
- Be fluent in other languages, and therefore be able to include the commonly-used words of other languages in your dictionary. This is the best option, but only really a nicety for those who already know another language. It's not worth learning another language just to improve the security of the algorithm you use to generate passwords.

