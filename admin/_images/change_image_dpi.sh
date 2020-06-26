# mogrify is a part of imagemagic package
desired_dpi=150
for f in *.png
do
   dpi=$(printf "%.0f\n" `identify -units PixelsPerInch -format "%x" $f`)
   if [[ "$dpi" != "$desired_dpi" ]]; then
      echo "Changing resolution of $f from $dpi to $desired_dpi"
      mogrify -units PixelsPerInch -density $desired_dpi $f
   fi 
done
