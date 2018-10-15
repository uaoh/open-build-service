#!/bin/bash

sourcearchive=$1
shift
prefix=$1
shift
limit=$1
shift

tdir=`mktemp -d`

# extract files
tar xJf $sourcearchive -C $tdir >&/dev/null

(echo tdir $tdir
 ls -laF $tdir
 echo tdir/
 ls -laF $tdir/*) 1>&2

pushd $tdir/*/src/api >& /dev/null  || echo "___ERROR_SRCDIR_NOT_FOUND___ $tdir/*"
ruby.ruby2.5 -rbundler -e 'exit' || echo "___ERROR_BUNDLER_NOT_INSTALLED___"

mode="resolve"
if [ "$limit" == "production" ]; then
  mode="specs_for([:default, :production, :assets])"
fi

ruby.ruby2.5 -rbundler -e 'Bundler.definition.'"$mode"'.any? { |s| puts "rubygem('$prefix':#{s.name}) = #{s.version}" }' | while read i; do echo -n $i", "; done
popd >& /dev/null

#cleanup
rm -rf $tdir

