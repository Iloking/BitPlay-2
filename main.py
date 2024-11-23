def reverse_bits(num):

    reversed_num = 0
    
   
    num_bits = num.bit_length()

    for i in range(num_bits):
        
        last_bit = num & 1
        
        reversed_num = (reversed_num << 1) | last_bit
        
        num = num >> 1

    return reversed_num

original_number = int(input("Enter your original number: "))
reversed_number = reverse_bits(original_number)
print(f"Reversed Number: {reversed_number} ({bin(reversed_number)[2:]})")
