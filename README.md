# SHA-256 Python

Python implementation of sha-256 hash algorithm.

## How to use?

```python
import Input
import Raund
import MAIN

# 1) Parse str what you with with Input.create_input_message
test_str = "abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq"
input_mas = Input.create_input_message(test_str)

# 2) Initiate params for algorithm
state = Raund.static_dict

# 3) Use sha256 func to get hash
# ATTENTION! THIS FUNC WITH SIDE EFFECT (IN FP TERMS)
MAIN.sha256(params, result)

# 4) Now 'state' include result
```

## Where did i get SHA-512 description?

Paper name: "Descriptions of SHA-256, SHA-384, and SHA-512"

Source: http://www.iwar.org.uk/comsec/resources/cipher/sha256-384-512.pdf

