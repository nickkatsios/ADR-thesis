title atomic theme compilation area storefront tag theme storefront performance theme compilation could result broken storefront error theme compilation wrongly configured value theme configuration customer reason theme always compiled physical folderlocation start compilation folder deleted recreated compilation crash due error needed file present theme folder storefront broken another issue edge case hit shop theme compilation progress storefront also may look broken required compiled file present theme folder yet instead compiling theme always folder compile theme always new folder generated seed theme compilation completed successful old theme storefront theme compilation finished new theme folder storefront also open possibility new feature customer may manually rollback previous theme compiled version delete old theme folder one hour see caching theme compiled successfully new location theme new location storefront discarded alternative alternative solution would always folder location live version theme theme compile process directly write folder temporary folder theme compilation finished copy whole temp folder live folder approach work well assumption moving whole folder fast atomic operation local filesystems theme asset also stored external storage google cloud storage especially dedicated setup common store asset file external filesystemcdn cant assume copying whole folder atomic operation fact google cloud storage moving folder mean manually empty target folder move file individually storage dont really support concept folder even though alternative fixed issue theme compilation errored fix edge case hit store current theme asset folder contain needed folder yet file copied one one would probably exaggerate problem additionally cost perspective solution downside especially external storage pay storage also file operation temporary folder moving folder result lot file operation compared directly compiling new folder aforementioned issue decided discard approach consequence expand abstract class abstractthemepathbuilder allow seeding mechanism allows change active theme folder path based randomly generated seed add two following method implemented custom implementation abstractthemepathbuilder php public function generatenewpathstring saleschannelid string themeid string seed string public function saveseedstring saleschannelid string themeid string seed void theme compilation theme compiler generate new random seed call generatenewpath method seed get location theme folder compiled file compilation stored theme compilation finished successfully compiler call saveseed method seed compilation subsequent call existing assemblepath method take account new seed thus new theme folder storefront backwards compatibility method added concrete method abstract class default implementation break backwards compatibility new method marked deprecated abstract major version custom implementation implement method default implementation keep backwards compatibility ignore seed saveseed method noop generatenewpath call existing assemblepath method thus behaviour existing implementation change mean old implementation also dont seeding mechanism problem theme compilation still present implementation unless custom implementation also implement seeding mechanism implementing two new method performance current seed saved somewhere fast retrieve seed value needed every storefront request therefore store seed systemconfig table system config already heavily cached performance issue additionally already allows saving value per sale channel case also considered storing seed additional column themesaleschannel mapping table reading requesttransformer adding request attribute usage idea discarded dal allow additional column mapping definition fact reset value additional column every write replace query update mapping caching url asset change mean cache storefront request invalidated already case previously new theme compilation would add cachebuster query param url prevent serving stale theme file cached browser side theme compilation cant delete old theme folder immediately new theme compilation finished successfully cache invalidation take time especially external cdns like fastly mean expect short time client still request old theme folder served stale content cdn ensure site render normally client wont delete old theme folder immediately instead dispatch queue message configurable delay default min max sqs delay old theme folder deleted old theme file still accessible one hour new theme compiled expand deletion strategy implement feature like manual rollback previous theme version theme asset previously theme asset stored folder compiled theme file meant every saleschannel theme theme asset duplicated even though asset always regardless theme configuration scale create new folder compiled theme file fly every theme compile asset file stored separate folder dependent sale channel theme configuration themeid folder name asset still unique per theme duplicated every sale channel paas platformsh platformsh currently offer store theme asset internal storage therefore asset stored locally additionally platformsh immutable deploys meaning version deployed file system readonly change made local file theme compile executed paas build step connection cant new default implementation abstractthemepathbuilder store new seed theme compile immutable deploys possible recompile theme runtime new deployment needed recompile theme paas affected issue theme compilation instead rollbacking backup theme folder would rollback last deployment instead mean paas seeding mechanism add implementation abstractthemepathbuilder ignores seed always return path given theme sale channel combination like old default implementation platformsh allows store theme asset externally move theme compile build deploy step default seeding implementation access deploy step also recompile theme runtime paas also benefit new theme compile mechanism