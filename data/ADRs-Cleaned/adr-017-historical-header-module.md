adr historical header module changelog november start first version december final draft first version september reduce historicalinfo type order cosmos sdk implement ibc specification module within cosmos sdk must ability introspect recent consensus state validator set commitment root proof value chain must checked handshake application must store recent header persistent store first store may current merklised store nonmerklised store may later proof necessary application must store information storing new header immediately handling abcirequestbeginblock func beginblockctx sdkcontext keeper historicalheaderkeeper error info historicalinfo apphash ctxheaderinfoapphash time ctxheaderinfotime nextvalidatorshash ctxcometinfonextvalidatorshash keepersethistoricalinfoctx ctxblockheight info keepergetparamrecentheaderstostore keeperprunehistoricalinfoctx ctxblockheight continue handling request alternatively application may store hash validator set application must make past committed header available querying cosmos sdk module keeper gethistoricalinfo function may implemented new module may also integrated existing one likely xstaking xibc may configured parameter store parameter case could changed parameterchangeproposals although take block stored information catch increased proposed consequence implementation adr require change cosmos sdk require change tendermint positive easy retrieval header state root recent past height module anywhere cosmos sdk rpc call tendermint required abci alteration required negative duplicate header data tendermint application additional disk usage long term approach might preferable neutral none known reference consensus state introspection