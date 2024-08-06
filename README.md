在这个小 project 中，你们需要基于 C++ 实现一个 ElGamal 的密码学算法，并支持以下功能：

- `encrypt(msg, group, char2elem, pk, r) -> ct`: 根据映射 `char2elem` 将消息 `msg` 中的每个字符映射 `Group` 中，并使用给定的 `pk` 和 `r` 进行加密，并将结果拼接在一起，得到最终的密文 `ct`。

- `decrypt(ct, group, elem2char, sk) -> msg`: 将 `ct` 用 `sk` 逐一解密后得到 `group` 中元素后，再由 `elem2char` 映射回字符，进而还原消息。

对于 $20\%$ 的数据，保证 `group` 为 $Z_p$

---

A little project for ECNU summer camp.

Hope you'll find it interesting.

Normal Task:

1. Give message in plaintext, elliptic curve group, user's public / private key, and a mapping from ascii visible character to point on the curve, output the ciphertext.
2. Give the ciphertext and other parameters, output the plaintext.

This part can be run on a online judge system, just like algorithm problems.

Bonus Task:

Though Public-key cryptography is low efficiency and not used to encrypt long message but exchange symmetric key in practice, we can still have fun with optimizing its preference()

We'll give you the plaintext from real scene(eg. books, news, daily talks, etc), and a elliptic curve group, you can design the mapping from word to point yourself in order to achieve the least memory cost by mapping & ciphertext.And then you can still reduce the memory cost by adapting some algorithm to the ciphertext. 

This part will be manually judged. So don't try to compress the message in plaintext without any encryption. And note that we won't give you the plaintext in advance, so there's no way for you to map the whole plaintext to one point()

Here are some documents you may like to read:

https://oi-wiki.org/math/bignum/

https://en.wikipedia.org/wiki/Elliptic_curve

https://en.wikipedia.org/wiki/Elliptic-curve_cryptography

https://en.wikipedia.org/wiki/ElGamal_encryption

https://en.wikipedia.org/wiki/Data_compression

https://blog.51cto.com/u_13054458/4742037
