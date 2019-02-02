#change the directory to the folder where you have your qrcodes

cd qrcodes/

#Code for removing the file extension/name problems
#start

# for i in *
# do
# j=`echo $i | sed -e 's/....$//'`
# mv $i $j
# done

#end

count=0

for i in *
do
	echo $i

	#Code for putting single qr code in a single template
	#start

	# convert -resize 710x710 $i $i
	# magick composite -gravity center -geometry +0+440 $i ../card.jpg $i

	#end

	#Code for combining 4 registration cards to print on an A4 sheet
	#start 

	if (( $count % 4 == 0 ))
	then
		echo "First One"
		mv $i test.jpg
	elif (( $count % 4 == 1 ))
	then
		echo "Second One"
		convert test.jpg $i +append test.jpg
		rm $i
	elif (( $count % 4 == 2 ))
	then 
		echo "Third One"
		mv $i test1.jpg
	elif (( $count % 4 == 3 ))
	then
		echo "Last One"
		convert test1.jpg $i +append test1.jpg
		convert test.jpg test1.jpg -append $i
		rm test.jpg && rm test1.jpg
	fi

	count=$((count+1))

	#end

done

cd ..