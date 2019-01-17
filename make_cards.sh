cd qr_procodes/

# for i in *
# do
# j=`echo $i | sed -e 's/....$//'`
# mv $i $j
# done

for i in *
do
	echo $i
	convert -resize 710x710 $i $i
	magick composite -gravity center -geometry +0+440 $i ../card.jpg $i
done 

cd ..