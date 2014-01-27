set -e
set -x

cp _stack_dockerfile Dockerfile
cp _stack_supervisord.conf stack_supervisord.conf
INIE=$(echo $INI | sed -e 's/[\/&]/\\&/g')
sed -i "s/DYNAMICALLYINSERTCOMMITIDHERE_READINGDB/$RDBID/g" Dockerfile
sed -i "s/DYNAMICALLYINSERTCOMMITIDHERE_SMAP/$SMAPID/g" Dockerfile
sed -i "s/DYNAMICALLYINSERTCOMMITIDHERE_PDB2/$PDBID/g" Dockerfile
sed -i "s/DYNAMICALLYINSERTINIHERE/$INIE/g" stack_supervisord.conf

docker build . 2>&1 | tee log
tail log | grep "Successfully" | awk '{print $3}' > lastbuild.id
cat lastbuild.id

#example use of this: PDBID=bb2ed62ff SMAPID=ee669956a59849794 RDBID=4fb25f96e73d44960 ./bake_docklet.sh
