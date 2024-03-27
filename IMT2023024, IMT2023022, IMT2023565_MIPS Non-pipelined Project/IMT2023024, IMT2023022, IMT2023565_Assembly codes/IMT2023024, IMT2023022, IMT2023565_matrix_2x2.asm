.data
matrix_X:    .word 1, 2, 3, 4       # matrix_X (2x2)
matrix_Y:    .word 5, 6, 7, 8       # matrix_Y (2x2)
result:     .space 16              # Allocate memory for result 

.text
main:
    la $a0, matrix_X           # Load address of matrix_X
    la $a1, matrix_Y           # Load address of matrix_Y

    # Load matrix_X values into registers
    lw $t0, 0($a0)            # Load X[0][0]
    lw $t1, 4($a0)            # Load X[0][1]
    lw $t2, 8($a0)            # Load X[1][0]
    lw $t3, 12($a0)           # Load X[1][1]

    # Load matrix_Y values into registers
    lw $t4, 0($a1)            # Load Y[0][0]
    lw $t5, 4($a1)            # Load Y[0][1]
    lw $t6, 8($a1)            # Load Y[1][0]
    lw $t7, 12($a1)           # Load Y[1][1]

    # Perform matrix multiplication of matrix_X and matrix_Y
    mul $s0, $t0, $t4         # X[0][0] * Y[0][0]
    mul $s1, $t1, $t6         # X[0][1] * Y[1][0]
    add $s0, $s1, $s0         # Sum of products in result[0][0]

    mul $s2, $t0, $t5         # X[0][0] * Y[0][1]
    mul $s3, $t1, $t7         # X[0][1] * Y[1][1]
    add $s2, $s3, $s2         # Sum of products in result [0][1]

    mul $s4, $t2, $t4         # X[1][0] * Y[0][0]
    mul $s5, $t3, $t6         # X[1][1] * Y[1][0]
    add $s4, $s5, $s4         # Sum of products in result [1][0]

    mul $s6, $t2, $t5         # X[1][0] * Y[0][1]
    mul $s7, $t3, $t7         # X[1][1] * Y[1][1]
    add $s6, $s7, $s6         # Sum of products in result [1][1]

    # Store the result back to memory
    sw $s0, result            # Store result[0][0]
    sw $s2, result + 4        # Store result[0][1]
    sw $s4, result + 8        # Store result[1][0]
    sw $s6, result + 12       # Store result[1][1]

    # Exit
    li $v0, 10                # syscall 10 (exit)
    syscall
