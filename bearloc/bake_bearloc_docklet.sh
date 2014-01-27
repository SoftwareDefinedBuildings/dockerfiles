set -e
set -x

bdir=BEARLOC_BUILD.$(date +%s).$RANDOM
mkdir $bdir

cp supervisor.conf $bdir/
cp _bearloc_dockerfile $bdir/Dockerfile

sed -i "s/DYNAMICALLYINSERTCOMMITIDHERE/$COMMITID/g" $bdir/Dockerfile

docker build $bdir 2>&1 | tee $bdir/build.log
tail $bdir/build.log | grep "Successfully" | awk '{print $3}'

#example use of this: COMMITID=<> ./bake_bearlock_docket.sh
