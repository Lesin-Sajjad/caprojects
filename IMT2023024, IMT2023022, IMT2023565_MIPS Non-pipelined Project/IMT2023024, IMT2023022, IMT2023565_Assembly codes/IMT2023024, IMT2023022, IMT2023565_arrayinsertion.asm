.data
source: .word 1, 2, 3, 4, 5  # array of elements {1,2,3,4,5}
target: .space 20       # Allocate space for target array 5x4
size:   .word 5

.text
main:

    la $t2, source        # Load base address of source array
    la $t3, target        # Load base address of target array
    lw $t0, size          # Load array size
    addi $t1, $zero, 0    # Initialize loop counter
 

loop:
    beq $t1, $t0, end     # Exit loop if counter = size
    lw $t4, 0($t2)        # Load element from source
    sw $t4, 0($t3)        # Store element to target
    addi $t1, $t1, 1      # Increment loop counter
    addi $t2, $t2, 4      # Move to next element in source array
    addi $t3, $t3, 4      # Move to next element in target array
    j loop                # restart loop

end:
