#!/usr/bin/perl
# Test Bing translation service
use strict;
use Bing::Translate;
use Locale::Codes::Language;
use utf8;

my $HOME = $ENV{'HOME'};
our($cliID, $cliSecret);
require "$HOME/etc/msservices.conf";

my $srcText = "Hello world!";
my $outfile = "$HOME/data/export/test-bing.txt";

my @langcodes = all_language_codes();

my $translator = Bing::Translate->new($cliID,$cliSecret);

open FH, ">$outfile";
binmode(FH, ":utf8");

foreach my $langcode(@langcodes) {
    my $langname = code2language($langcode);
    my $result = $translator->translate("$srcText", "en", $langcode);
    if($result !~ /translate fail/g) {
        print $srcText, " in ", $langname, " is ", $result, "\n";
        print FH $srcText, " in ", $langname, " is ", $result, "\n";
    }
}

close FH;

__END__;


