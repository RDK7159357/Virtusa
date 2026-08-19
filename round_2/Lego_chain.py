from collections import Counter


def lego_chain(wall, N, B):
	if not wall or not B:
		return [-1]

	word_len = len(B[0])
	if any(len(word) != word_len for word in B):
		return [-1]

	total_len = word_len * N
	if len(wall) < total_len:
		return [-1]

	need = Counter(B)
	result = []

	for offset in range(word_len):
		left = offset
		window = Counter()
		used = 0

		for right in range(offset, len(wall) - word_len + 1, word_len):
			word = wall[right:right + word_len]
			if word not in need:
				window.clear()
				used = 0
				left = right + word_len
				continue

			window[word] += 1
			used += 1

			while window[word] > need[word]:
				left_word = wall[left:left + word_len]
				window[left_word] -= 1
				used -= 1
				left += word_len

			if used == N:
				result.append(left)
				left_word = wall[left:left + word_len]
				window[left_word] -= 1
				used -= 1
				left += word_len

	return sorted(result) if result else [-1]
