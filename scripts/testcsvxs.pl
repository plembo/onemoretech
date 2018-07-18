#!/usr/bin/perl
# Test Text::CSV_XS module operation.
use strict;
use Text::CSV_XS;

my $HOME = $ENV{'HOME'};

my $infile = "$HOME/Documents/testfile.csv";
 
my $csv = Text::CSV_XS->new({
    binary => 1,
    allow_loose_quotes => 1,
    escape_char => undef,
    auto_diag => 1,
});
 
my $sum = 0;
open(my $data, '<:encoding(utf8)', $infile) or die "Could not open '$infile' $!\n";
while (my $row = $csv->getline($data)) {

    my $fname = $row->[0];
    my $lname = $row->[1];
    my $street = $row->[2];
    my $city = $row->[3];
    my $state = $row->[4];
    my $country = $row->[5];
    my $postalcode = $row->[6];
   
    print "\"$fname\",\"$lname\",\"$country\"\n";
}

close $data;
