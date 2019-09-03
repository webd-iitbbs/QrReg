#change the directory to the folder where you have your qrcodes

cd qrcodes/

#Code for removing the file extension/name problems
#start

for i in *
do
j=`echo $i | sed -e 's/....$//'`
mv $i $j
done

#end

count=0

for i in *
do
	echo $i

	#Code for putting single qr code in a single template
	#start

	convert -resize 710x710 $i $i
	magick composite -gravity center -geometry +0+440 $i ../card.jpg $i

	#end

done

cd ..