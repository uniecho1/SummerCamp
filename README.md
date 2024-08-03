A little project for ECNU summer camp.

Hope you'll find it interesting.

Normal Task:

1. Give message in plaintext, elliptic curve group, user's public / private key, and a mapping from ascii visible character to point on the curve, output the ciphertext.
2. Give the ciphertext and other parameters, output the plaintext.

This part can be run on a online judge system, just like algorithm problems.

Bonus Task:

Though Public-key cryptography is low efficiency and not used to encrypt long message but exchange symmetric key in practice, we can still have fun with optimizing its preference()

We'll give you the plaintext from real scene(eg. books, news, daily talks, etc), and a elliptic curve group, you can design the mapping from word to point yourself in order to achieve the least memory cost by mapping & ciphertext.And then you can still reduce the memory cost by adapting some algorithm to the ciphertext. 

This part will be manually judged. So don't try to compress the message in plaintext without any encryption. And note that we won't give you the plaintext in advance, so there's no way for you to map the whole plaintext to one node()

Here are some documents you may like to read:

https://oi-wiki.org/math/bignum/

https://en.wikipedia.org/wiki/Elliptic_curve

https://en.wikipedia.org/wiki/Elliptic-curve_cryptography

https://en.wikipedia.org/wiki/ElGamal_encryption

https://en.wikipedia.org/wiki/Data_compression

https://blog.51cto.com/u_13054458/4742037