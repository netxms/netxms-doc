# mogrify is a part of imagemagic package
desired_dpi=150
find . -name '*.png' -type f -not -path './icons/*' | while read -r f
do
   dpi=$(LC_NUMERIC=C printf "%.0f\n" "$(identify -units PixelsPerInch -format "%x" "$f")")
   if [[ "$dpi" != "$desired_dpi" ]]; then
      echo "Changing dpi of $f from $dpi to $desired_dpi"
      mogrify -units PixelsPerInch -density "$desired_dpi" "$f"
   fi
done
