# Program to Improve string matching using KMP string matching algorithm.
# Python program for KMP Algorithm
# ------------------------------------------------------------------------------------------------------
# Preprocessing part for KMP :
# Here, we are interested in identifying the part where mismatch occurs and using the information till what progress we have made
# and use it to match for next iteration at that index which is taken from precomputed table.
# Precomputed table, is made by having two pointers and shift them both if it matches and if not matches, then we need to simply add 1 to the first pointer var
# and put it to the precomputed table value.
# Also, if we reach the end, and pointers do not match, then we need to move first pointer to the index of the value stored at just previous index : lps[j - 1]
# for j as first var, i as second var.
# and now after pushing j to the one of the older indices as described above, again we check, if match, then same add 1 and put it that index at i.
# Given pattern : a b c d a b c a
#                 -----   -----
# precomputed :  [0 0 0 0 1 2 3 1]
# Explained : for ex. in above table, longest suffix matching with prefix is 3 is "abc" <> "abc" which is evident at index "6" in the table.
# Overall, these indices mean that at any index, the value tells the longest value of suffix before that which also matches some same prefix in the pattern.
# Like, value at index "4" says the value is 1 and pattern till that : a b c d a => so longest suffix matching prefix is "a" and sim. for other values.
# Now, how will this help ? we will see now...
# -----------------------------------------------------------------------------------------------------------
# Comparison part
# Now, after building the above part, we can move onto comparison of text and pattern, and then same two pointers j, i
# if match occurs, then simply shift both pointers, and if match doesn't occurs, then now we need not compare the pattern from starting
# here, actually our precomputed table will help, in the next iteration, we can start our comparison directly from that particular index
# whatever is the value at just previous index (lps[j - 1] ) in precomputed table and go to that index (move j there) and start checking again (without changing i pointer).
# Hence, we are actually using our saved progress made at that point, like
# text : a b c d a x .....
#                -
# pat :  a b c d a b .....
#        -       -
# so, keeping our j, i in mind, match occurs till index "4" (a) and as soon as we hit "x", then we bascially use our table which tells
# that value at index 5-1 => index 4 in precomputed table value is "1", so in next iteration we start our matching from index "1" in pattern string
# and not from all the back from "0".
# We can also see the progress saved in the text string also, as just before x, we have matched till first char that is "a", and that is also
# the same information that precomputed table tell us that start the search from index "1", that is after "a", start from "b".
# -------------------------------------------------------------------------------------------------------------
# Keeping up with this, we can search the string in 0(M + N) where M is length of text.
# Space : 0(N), N is length of pattern string.
# ---------------------------------------------------------------------------------------------------------------

def KMPSearch(pat, txt):
	M = len(pat)
	N = len(txt)

	# create lps[] that will hold the longest prefix suffix
	# values for pattern
	lps = [0]*M
	j = 0 # index for pat[]

	# Preprocess the pattern (calculate lps[] array)
	computeLPSArray(pat, M, lps)

	i = 0 # index for txt[]
	while i < N:
		if pat[j] == txt[i]:
			i += 1
			j += 1

		if j == M:
			print("Found pattern at index " + str(i-j))
			j = lps[j-1]

		# mismatch after j matches
		elif i < N and pat[j] != txt[i]:
			# Do not match lps[0..lps[j-1]] characters,
			# they will match anyway
			if j != 0:
				j = lps[j-1]
			else:
				i += 1

def computeLPSArray(pat, M, lps):
	len = 0 # length of the previous longest prefix suffix

	lps[0] # lps[0] is always 0
	i = 1

	# the loop calculates lps[i] for i = 1 to M-1
	while i < M:
		if pat[i]== pat[len]:
			len += 1
			lps[i] = len
			i += 1
		else:
			# This is tricky. Consider the example.
			# AAACAAAA and i = 7. The idea is similar
			# to search step.
			if len != 0:
				len = lps[len-1]

				# Also, note that we do not increment i here
			else:
				lps[i] = 0
				i += 1

txt = "ABABDABACDABABCABAB"
pat = "ABABCABAB"
KMPSearch(pat, txt)

# This code is contributed by Bhavya Jain
