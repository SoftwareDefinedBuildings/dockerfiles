
cp _dockerfile Dockerfile

sed -i "s/DYNAMICALLYINSERTCOMMITIDHERE_READINGDB/$RDBID/g" Dockerfile
sed -i "s/DYNAMICALLYINSERTCOMMITIDHERE_SMAP/$SMAPID/g" Dockerfile
sed -i "s/DYNAMICALLYINSERTCOMMITIDHERE_PDB2/$PDBID/g" Dockerfile

docker build . | tee log
cat log | grep "Successfully" | awk '{print $3}'

#example use of this: PDBID=bb2ed62ff SMAPID=ee669956a59849794 RDBID=4fb25f96e73d44960 ./bake_docklet.sh
