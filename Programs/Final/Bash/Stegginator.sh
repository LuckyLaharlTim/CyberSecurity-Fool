output=out.jpg
input=stegged-byte.bmp
for i in {256..1024..128}
do
	for j in {1..8..1}
	do
		python3 Steg.py -o$i -i$j -B -r -w"$input" > O"$i"I"$j""$output"
		size=`wc -c < O"$i"I"$j""$output"`
		if [ $size == 0 ]
		then
			rm O"$i"I"$j""$output"
		fi
	done
done


