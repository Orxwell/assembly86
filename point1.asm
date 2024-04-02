# PUNTO 1 DEL LABORATORIO

# .data assembler directive
.data # Section for declaring variables

	num1: .word 0 # The label 'num1' represents an integer with value 0
	num2: .word 0 # The label 'num2' represents an integer with value 0
	num3: .word 0 # The label 'num3' represents an integer with value 0

	result: .word 0 # The label 'result' represents an integer with value 0

	msg1: .asciiz "Ingresa un numero: "     # The label 'msg1' represents an ASCII message
	msg2: .asciiz "El mas grande es: "      # The label 'msg2' represents an ASCII message
	msg3: .asciiz "Ningun numero es mayor." # The label 'msg3' represents an ASCII message

# .text assembler directive
.text # Section for the program code

	.globl main # Declare 'main' as a global function
	
	main: # The lable 'main' represents the starting point
		jal inputMsg # CALL for all the Output/Input:Interface
		jal loadTemp # CALL for load all the Inputs to Temps
		jal evaluate # CALL for evaluate all the Inputs

	inputMsg: # I/O:Interface
		# INPUT 'NUM1'
		li      $v0, 4    # Service code 4 to print_string
		la      $a0, msg1 # Pointer to string (load the address of 'msg')
		syscall
		li      $v0, 5    # Service code 5 to input_integer
		syscall
		sw      $v0, num1 # Save the integer into the memory ($num1)

		# INPUT 'NUM2'
		li      $v0, 4    # Service code 4 to print_string
		la      $a0, msg1 # Pointer to string (load the address of 'msg')
		syscall
		li      $v0, 5    # Service code 5 to input_integer
		syscall
		sw      $v0, num2 # Save the integer into the memory ($num1)

		# INPUT 'NUM3'
		li      $v0, 4    # Service code 4 to print_string
		la      $a0, msg1 # Pointer to string (load the address of 'msg')
		syscall
		li      $v0, 5    # Service code 5 to input_integer
		syscall
		sw      $v0, num3 # Save the integer into the memory ($num1)

		jr $ra # End up the function

	loadTemp: # Load the temporary data
		lw $t0, num1 # Load 'num1' to the temp(0)
		lw $t1, num2 # Load 'num2' to the temp(1)
		lw $t2, num3 # Load 'num3' to the temp(2)

		jr $ra # End up the function

	evaluate: # Evaluate all 'num_n'
		jal ev0_equal # Evaluate if all the numbers are equal
		
		jal ev1_layer1 # Evaluation(1) of layer(1)
		jal ev2_layer1 # Evaluation(2) of layer(1)
		jal ev3_layer2 # Evaluation(3) of layer(2) [LAST layer]
		
		li      $v0, 4    # Service code 4 to print_string
		la      $a0, msg2 # Pointer to string (load the address of 'msg2')
		syscall

		li      $v0, 1      # Service code 1 to print_integer
		lw      $a0, result # Pointer to integer (load the address of 'result')
		syscall
		
		# Run the exit:syscall which has code 10
		li      $v0, 10 # Service code 10 to end up the program
		syscall         # End up the program
	
	ev0_equal:
		beq $t0, $t1, isEqual # 'num1' == 'num2', CALL maybeEqual
		
		jr $ra # End up the function
	
	isEqual:
		beq $t1, $t2, isTotallyEqual # 'num2' == 'num3', CALL isTotallyEqual
		
		jr $ra # End up the function
	
	isTotallyEqual:
		li      $v0, 4    # Service code 4 to print_string
		la      $a0, msg3 # Pointer to string (load the address of 'msg3')
		syscall
		
		# Run the exit:syscall which has code 10
		li      $v0, 10   # Service code 10 to end up the program
		syscall           # End up the program
	
	ev1_layer1:
		bge $t0, $t1, ev1_moveA # $t0 >= $t1, CALL ev1_moveA
		blt $t0, $t1, ev1_moveB # $t0 <  $t1, CALL ev1_moveB

		jr $ra # End up the function

	ev1_moveA:
		move $t3, $t0 # SET $t3 WITH 'num1'

		jr $ra # End up the function

	ev1_moveB:
		move $t3, $t1 # SET $t3 WITH 'num2'

		jr $ra # End up the function

	ev2_layer1:
		bge $t1, $t2, ev2_moveB # $t1 >= $t2, CALL ev2_moveB
		blt $t1, $t2, ev2_moveC # $t1 <  $t2, CALL ev2_moveC

		jr $ra # End up the function

	ev2_moveB:
		move $t4, $t1 # SET $t4 WITH 'num2'

		jr $ra # End up the function

	ev2_moveC:
		move $t4, $t2 # SET $t4 WITH 'num3'

		jr $ra # End up the function

	ev3_layer2:
		bge $t3, $t4, result1 # $t3 >= $t4, CALL result1
		blt $t3, $t4, result2 # $t3 <  $t4, CALL result2

		jr $ra # End up the function

	result1: # '$t3' is the greatest
		sw $t3, result # Storage '$t3' at 'result'

		jr $ra # End up the function

	result2: # '$t4' is the greatest
		sw $t4, result # Storage '$t4' at 'result'

		jr $ra # End up the function
