.text
    .globl main

main:
    li $t0, 8          # number = 8
    li $t1, 0          # x = 0 (fib 0)
    li $t2, 1          # y = 1 (fib 1)
    li $t3, 0          # counter = 0
    
#We are using linear time algorithm to calculate the fibonacci numbers.
fibonacci_loop: add $t4, $t1, $t2        # t4 = x + y
                add $t1, $zero, $t2      # x = y
                add $t2, $zero, $t4      # y = t4
    
                addi $t3, $t3, 1   # counter++

                # Check if counter < n
                bne $t3, $t0, fibonacci_loop
    
       
# Exit program
li $v0, 10         
syscall
