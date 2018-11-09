use strict;
use warnings;

use File::Path;
use FindBin;
use Data::Dumper;

use Test::More tests => 2;

require_ok('BSSched::Checker');

my @basefile = split('/', __FILE__);
my $basename = pop(@basefile);
my $dirname  = join('/', @basefile);

$BSConfig::bsdir = $dirname . "/tmp/4242";
unlink($BSConfig::bsdir);
$BSSched::arch = 'x86_64';
$BSSched::reporoot = $dirname . "/tmp/4242/build";

my $prp           = 'openSUSE:Test/standard';
my $packid        = 'findutils';
my $fdir          = join('/', $BSSched::reporoot, $prp, $BSSched::arch);
my $pkg_finished  = join('/', $fdir, ':packstatus.finished');
my $gctx	  = {
	reporoot => $dirname . "/tmp/4242/build",
	arch	 => 'x86_64'
};

my $ctx = BSSched::Checker->new($gctx, $prp);
$ctx->{'packs'} = [ 'diffutils' ];
$ctx->{'prpchecktime'} = time();
$ctx->{'gdst'} = $dirname . '/tmp/4242/';
File::Path::make_path($ctx->{'gdst'});

my ($state, $details) = $ctx->checkpkgs();
is($state, 'finished', 'checker checkpkgs call');

exit 0;
