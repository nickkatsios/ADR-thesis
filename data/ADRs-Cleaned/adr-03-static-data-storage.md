static data storage order support fast blocklevel district editing user necessary push large amount static data clientside may initially appear able get data vector tile given blocklevel vector tile zoomlevel restricted due abundance feature lower zoom level operation require additional information example say user load set district district split blockgroups common situation user want select split blockgroup move one district another wont possible calculate change demographic data clientside changed district without appropriate blocklevel vector tile available solution problem load static blocklevel data demographic clientside another piece static data thats needed mapping block belong geounits higher geolevels example know block belong blockgroup well able collect underlying demographic data perform calculation detailed conversation data frontend user make selection map see conversation particularly answer third question testing weve determined order efficiently store large amount static data clientside memory make typed array reduced memory footprint efficient storage mechanic make typed array ideal storing large amount fixed integer array testing lack sluggishness immediately apparent even large amount data loaded order make typed array stick theme adr make internally consistent geolevel ordering across static data file demographic static data array contains element base geounit block whose value set demographic value demographic type question mean one file demographic type similarly geolevel static data array contains element base geounit whose value set index geounit geolevel type question one file nonbase geolevel take county block example county delaware idea create flat array specify block belong county create file long number block element either depending county belongs file length since mapping geounits contained base geolevel since data static able know advance information contained within file able programatically make kind typed array upon creation file uintarray store value situation well able uintarray store value half size unlikely situation ever demand even larger number uintarray expands weve tested ability store data file format well read back serverside clientside problem clientside fetch function support specifying input data arraybuffer proper typed array constructed without overhead consequence appears safest bet pushing large amount data frontend efficient memory characteristic working array practice may pose small amount developer friction since additionally processing occasionally actually work example user selects county know block belong county filter geolevel typed array order find element storing json structure grouping place would easier work however wed miss performance benefit typed array tradeoff seems worthwhile necessary