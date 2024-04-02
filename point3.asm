# PUNTO 3 DEL LABORATORIO

# .data assembler directive
.data # Section for declaring variables

	ndx: .word 0 # The label 'num1' represents an integer with value 0

	sum: .word 0

	msg:    .asciiz "Ingresa un entero: " # The label 'msg' represents an ASCII message
	msg_s:  .asciiz ", "                  # The label 'masg_s' representas an ASCII message (space)
	result: .asciiz "Resultado: "         # The label 'result' represents an ASCII message

# .text assembler directive
.text # Section for the program code

	.globl main # Declare 'main' as a global function

	main: # The lable 'main' represents the starting point
		jal inputMsg # CALL for all the Output/Input:Interface
		jal loadTemp # CALL for load all the Inputs to Temps
		
		li      $v0, 4    # Service code 4 to print_string
		la      $a0, result # Pointer to string (load the address of 'msg2')
		syscall
		
		jal for_loop

	inputMsg: # I/O:Interface
		# INPUT 'NUM1'
		li      $v0, 4    # Service code 4 to print_string
		la      $a0, msg # Pointer to string (load the address of 'msg')
		syscall
		li      $v0, 5    # Service code 5 to input_integer
		beq     $v0, 0, end_loop
		syscall
		sw $v0, ndx # Save the integer into the memory ($num1)

		jr $ra # End up the function

	loadTemp: # Load the temporary data
		lw $t1, ndx # Load 'num1' to the temp(0)

		jr $ra # End up the function
	
	for_loop:
		beq $t0, $t1, end_loop

		# start code
		beq $t0, 0, load_0
		beq $t0, 1, load_1
		bgt $t0, 1, load_n
		# end code
	
	load_0:
		# Run the print_integer:syscall which has code 1
		li      $v0, 1     # Service code 1 to print_integer
		la      $a0, ($t2) # Pointer to integer (load word of '$t2')
		syscall
		
		# Run the print_string:syscall which has code 4
		li      $v0, 4     # Service code 4 to print_string
		la      $a0, msg_s # Pointer to string (load the address of 'msg_s')
		syscall

		addi $t0, $t0, 1

		j for_loop # End up the function

	load_1:
		add $t4, $zero, $t0
		add $t2, $zero, $t0
		
		# Run the print_integer:syscall which has code 1
		li      $v0, 1     # Service code 1 to print_integer
		la      $a0, ($t2) # Pointer to integer (load word of '$t2')
		syscall
		
		# Run the print_string:syscall which has code 4
		li      $v0, 4     # Service code 4 to print_string
		la      $a0, msg_s # Pointer to string (load the address of 'msg_s')
		syscall
		
		move $t2, $zero
		addi $t0, $t0, 1

		j for_loop # End up the function

	load_n:
		add $t2, $t3, $t4
		sub $t9, $t1, $t0
		
		# Run the print_integer:syscall which has code 1
		li      $v0, 1     # Service code 1 to print_integer
		la      $a0, ($t2) # Pointer to integer (load word of '$t2')
		syscall
		
		beq $t9, 1, end_loop
		
		# Run the print_string:syscall which has code 4
		li      $v0, 4     # Service code 4 to print_string
		la      $a0, msg_s # Pointer to string (load the address of 'msg_s')
		syscall
		
		move $t3, $t4
		move $t4, $t2
		move $t2, $zero
		
		addi $t0, $t0, 1

		j for_loop # End up the function

	end_loop:
		# Run the exit:syscall which has code 10
		li      $v0, 10   # Service code 10 to end up the program
		syscall           # End up the program
