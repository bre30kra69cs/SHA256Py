import Input
import Raund


# Test vector
test_str = "abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq"
input_mas = Input.create_input_message(test_str)
state = Raund.static_dict


def sha256(params, result):
	for i in params:
		result = Raund.one_block_permutation(result, i)
	return result