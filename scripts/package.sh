mkdir package

cp -R venv/lib/python*/site-packages/* package/
cp -R src/* package/

cd package/
zip -9 -FSr ../package.zip *
cd ..
rm -rf package