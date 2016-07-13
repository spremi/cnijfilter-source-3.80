#!/usr/bin/perl

if ( @ARGV != 1 ) {
	printf( "usage : %s ../rules\n", $0 );
}



$fn = $ARGV[0];

open( IN, $fn );
while( <IN> ){
	$line = $_;
	chomp( $line );

	if ( $line =~ /^PRINTER_DEPEND_PKG.+?=(.+$)/ ){
		$info = $1;
		if (  $info =~ /(.+)\-(.+)\-(.+)/ ){
			$model = $2;
			$num = $3;
			printf( "model: %s\n", $2 );
			printf( "num: %s\n", $3 );
			# doc file
			`perl -pe 's/MODEL/${model}/' docs.skel >  cnijfilter-${model}series.docs`;

			# postinst file
			`perl -pe 's/XXXX/${info}/' postinst.skel >  cnijfilter-${model}series.postinst`;

			# postinst file
			`perl -pe 's/XXXX/${info}/' postrm.skel > cnijfilter-${model}series.postrm`;
		}
	}
}
close( IN );
