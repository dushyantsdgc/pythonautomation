s="YYYXXXXAAABBBBCZZZCCCCCDDDEEEEE"
output=''
for ch in s:
    if ch not in output:
        output=output+ch
output_final=''.join(sorted(output))
print(output_final)