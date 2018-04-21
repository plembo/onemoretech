#!/usr/bin/perl
# Get rss feed url from conf file and add latest to web page.
use strict;
use XML::FeedPP;

my $HOME = $ENV{'HOME'};
my $outfile = "/data/podcasts/podcasts.html";

our(@sources);

require "$HOME/etc/podcasts.conf";

my @indices = (0,1,2,3);

open FH, ">$outfile" or die $!;

print FH <<'EOT';
<!DOCTYPE html>
<html>
<head>
<title>Latest Podcasts</title>
<meta http-equiv="content-type" content="text/html; charset=utf-8">
<link rel="stylesheet" href="/css/main.css" type="text/css">
</head>
<body>
<h1>Latest Podcasts</h1>
EOT

foreach my $source(@sources) {

  my $feed = XML::FeedPP->new($source);
  my $title = $feed->title();
  print FH "\<h3\>", $title, "\</h3\>\n";

  # foreach my $item ( $feed->get_item() ) {
  foreach my $index(@indices) {
     my $item = $feed->get_item($index);
     if($item) {
	    my $itemtitle = $item->title();
	    print FH "\<p\>", $itemtitle, "\</p\>\n";
        my $medialink = $item->get('enclosure@url');
        print FH "\<p\>\<a href=\"$medialink\"\>$medialink\</a\>\</p\>\n";
     }
     print FH "\<p\>\n";
  }
}

print FH "\</body\>\n";
print FH "\</html\>\n";

close FH;

__END__;

