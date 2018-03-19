#!/bin/bash

URL=http://www.ee.surrey.ac.uk/CVSSP/demos/chars74k/EnglishImg.tgz

echo
echo "Baixando os dados..."
echo

curl $URL > data.tgz

echo
echo "Decomprimindo os arquivos..."
echo

tar -xf data.tgz

rm data.tgz

pushd English/ &> /dev/null

mv Img/ data/

popd &> /dev/null

mv English/data .

rmdir English

pushd data &> /dev/null

pushd BadImag &> /dev/null

rm -rf Msk/

pushd Bmp &> /dev/null

for d in */; do
    mv $d/* .
    rmdir $d
done

for f in *; do
    mv $f "BadImag-$f"
done

popd &> /dev/null

find Bmp -name '*.*' -exec mv {} ../ \;

rmdir Bmp/

popd &> /dev/null

rmdir BadImag/

pushd GoodImg &> /dev/null

rm -rf Msk/

pushd Bmp &> /dev/null

for d in */; do
    mv $d/* .
    rmdir $d
done

for f in *; do
    mv $f "GoodImg-$f"
done

popd &> /dev/null

find Bmp -name '*.*' -exec mv {} ../ \;

rmdir Bmp/

popd &> /dev/null

rmdir GoodImg/

popd &> /dev/null

echo "Pronto!"
