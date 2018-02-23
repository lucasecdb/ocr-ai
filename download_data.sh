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

echo "Pronto!"
