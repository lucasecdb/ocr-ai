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

rm -rf BadImag/

pushd GoodImg &> /dev/null

rm -rf Msk/

pushd Bmp &> /dev/null

for d in */; do
    mv $d/* .
    rmdir $d
done

popd &> /dev/null

mv Bmp/* ../

rmdir Bmp/

popd &> /dev/null

rmdir GoodImg/

popd &> /dev/null

echo "Pronto!"
