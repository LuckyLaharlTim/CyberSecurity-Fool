#Change input file to stegged file and output extension to what file you believe you'll get (no extension if you are unsure)
output=out.jpg
input=stegged-byte.bmp

#You may have to modify the intervals {start..end..increment}
for i in {256..1024..128}
do
	for j in {1..8..1}
	do
		#Make sure bit or byte mod is properly selected.
		python3 Steg.py -o$i -i$j -B -r -w"$input" > O"$i"I"$j""$output"
		size=`wc -c < O"$i"I"$j""$output"`
		if [ $size == 0 ]
		then
			rm O"$i"I"$j""$output"
		fi
	done
done


