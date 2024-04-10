class RailFenceCipher:
    def __init__(self):
        pass
    
    def rail_fence_encrypt(self, plain_text, num_rails):
        rails = [[] for _ in range(num_rails)]
        rail_index = 0
        direction = 1  # Direction: 1 for down, -1 for up

        for char in plain_text:
            rails[rail_index].append(char)
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction
        
        cipher_text = ''.join(''.join(rail) for rail in rails)
        return cipher_text

    def rail_fence_decrypt(self, cipher_text, num_rails):
        # Determine the lengths of each rail
        rail_lengths = [0] * num_rails
        rail_index = 0
        direction = 1

        for _ in range(len(cipher_text)):
            rail_lengths[rail_index] += 1
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction
        
        # Reconstruct the rails from the cipher text
        rails = []
        start = 0
        for length in rail_lengths:
            rails.append(cipher_text[start:start + length])
            start += length
        
        # Decipher the text based on the rail structure
        plain_text = [''] * len(cipher_text)  # Initialize an empty list to store the plain text
        rail_index = 0
        direction = 1
        current_index = 0  # Index to track position in the plain text

        for _ in range(len(cipher_text)):
            plain_text[current_index] = rails[rail_index][0]
            rails[rail_index] = rails[rail_index][1:]
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction
            current_index += 1
        
        return ''.join(plain_text)  # Join the list of characters into a single string