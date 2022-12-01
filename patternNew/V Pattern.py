		# Python3 program to print alphabet pattern V

		# *                                   *
		#   *                               *
		#     *                           *
	#       *                       *
		#         *                   *
		#           *               *
		#             *           *
			#               *       *
			#                 *   *
			#                   *
'''
def print_pattern(n):
			# row looping
	for row in range(n):

	# column looping
		for column in range(n):
			if (
							# right slanting line
				(row + column == n - 1 and row < n / 2) or
					# left slanting line
				(row == column and row < n / 2)
				):
				print("*", end= " ")
			else:
				print(" ", end=" ")
		print()


size = int(input("Enter any size: \t"))
if size < 8:
	print("Enter a size minimum of 8")
else:
	print_pattern((size * 2) +1)



'''

def design_A_Pattern(n):
	for row in range(n):
		for column in range(n):
			if(
				(row+column==n-1 and row < n/2) or
				(row==column and row < n/2)
			):
				print("*",end="")
			else:
				print(" ",end="")
		print()


n=int(input("Enter a size"))
if n<8:
	print("Enter minimium size 8")
else:
	design_A_Pattern((n*2)+1)