#include <stdint.h>


typedef uint32_t CRC; // Cette déclaration de type peut être ajustée pour supporter des CRC 64 bits


CRC bit_reflect(CRC data, unsigned char nbits) {
    CRC output = 0;
    for (unsigned char i = 0; i < nbits; ++i) {
        if (data & 1) 
            output |= 1 << ((nbits - 1) - i);
        data >>= 1;
    }
    return output;
}


CRC crc_generic(char* data, unsigned int data_len, 
                unsigned char nbits, CRC polynôme, CRC initial_value,
                char reflect_input, char reflect_output, CRC final_xor_value) {

    CRC bitmask = (1ULL << nbits) - 1;
    CRC msb_mask = 1 << (nbits - 1);
    CRC crc = initial_value;

    if (data_len == 0)
        return 0;

    for (unsigned int i = 0; i < data_len; ++i) {
        CRC dbyte = data[i];

        if (reflect_input)
            dbyte = bit_reflect(dbyte, 8);
        
        crc ^= dbyte << (nbits - 8);
        
        for (unsigned char j = 0; j < 8; ++j) {
            CRC mix = crc & msb_mask;
            crc = ((crc << 1) & bitmask);
            if (mix)
                crc = crc ^ polynôme;
        }
    }
    
    if (reflect_output)
        crc = bit_reflect(crc, nbits);

    return (crc ^ final_xor_value) & bitmask;
}


// ----- Exemple pour PC


#include <stdio.h>

int main(void) {
    
    printf("CRC-16: %lX\n", crc_generic("123456789", 9, 16, 0x8005, 0, 1, 1, 0)); // 0xBB3D
    printf("CRC-16 CCITT (0xFFFF): %lX\n", crc_generic("123456789", 9, 16, 0x1021, 0xffff, 0, 0, 0)); // 0x29B1
    printf("CRC-16 CCITT (0x1D0F): %lX\n", crc_generic("123456789", 9, 16, 0x1021, 0x1D0F, 0, 0, 0)); // 0xE5CC
    printf("CRC-32: %lX\n", crc_generic("123456789", 9, 32, 0x04C11DB7, 0xFFFFFFFF, 1, 1, 0xFFFFFFFF)); // 0xCBF43926
    
    return 0;
}