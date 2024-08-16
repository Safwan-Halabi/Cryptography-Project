from finalRSA import encoder, decoder
from cast128 import encrypt_message_CAST, decrypt_message_CAST
from finalElGamal import encrypt_ElGamal, decrypt_ElGamal, generate_decryption_parameters

# public key = 7
# private key = 28543
# n = 40363

alice, bob = '', ''
alice_symmetric_key = 'FFFF0123ABCDEF12FFFF0123ABCDEF12'
encrypted_symmetric_key = encoder(alice_symmetric_key)

# We send encrypted_symmetric_key to Bob

bob_symmetric_key = decoder(encrypted_symmetric_key)

# Now both Alice and Bob have the same symmetric key

alice_message = "Hello bob, I wanted to say that I've loved you all along and I really miss you here in Oklahoma"

alice_encrypted_message = encrypt_message_CAST(alice_message, alice_symmetric_key)

# Now bob got alice's message, we will now 

q, g, key, h = generate_decryption_parameters()
alice_hased_message = str(hash(alice_encrypted_message))
en_msg, p = encrypt_ElGamal(alice_hased_message, q, h, g)

signature = ''
for i in en_msg:
    signature += str(i) + ','
signature = signature[:-1]
#dr_msg = decrypt_ElGamal(en_msg, p, key, q)

flag = '¿¿¿¿¿¿¿¿!!!!!!!!'

message_sent_to_bob = alice_encrypted_message + flag + signature

# Bob got the string, now he'll decrypt

bob_data, bob_signature = message_sent_to_bob.split(flag)

bob_signature = bob_signature.split(',')
bob_signature = [int(i) for i in bob_signature]

signature_decrypted = decrypt_ElGamal(bob_signature, p, key, q)

signature_decrypted = ''.join(signature_decrypted)

print("Is the message verified? Answer: " + str(signature_decrypted == str(hash(bob_data))))

bob_decrypted_message = decrypt_message_CAST(bob_data, bob_symmetric_key)

print("Message Bob received: " + bob_decrypted_message)




