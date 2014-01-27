set -e
set -x

cp _driver_dockerfile Dockerfile
cp _driver_supervisord.conf driver_supervisord.conf

INIE=$(echo $INI | sed -e 's/[\/&]/\\&/g')
sed -i "s/DYNAMICALLYINSERTCOMMITIDHERE_SMAP/$SMAPID/g" Dockerfile
sed -i "s/DYNAMICALLYINSERTINIHERE/$INIE/g" driver_supervisord.conf

docker build . 2>&1 | tee log
tail log | grep "Successfully" | awk '{print $3}' > lastbuild.id
cat lastbuild.id

#example use of this: SMAPID=ee669956a59849794 INI="conf/caiso.ini" ./bake_driver_docklet.sh
