configuration title configuration server configuration run startup command introduction franklin start default default endpoint query extension stac api specification available however two additional flag enable additional functionality case additional endpoint included server openapi specification hostopenapispecyaml configuring database connection two configuring database first whats shown example startup command case specify user host port password separate argument alternatively specify complete connection string connection string look something like jdbcpostgresqlhostdatabasenameuseruserpasswordpassword general safer configure database connection one component time allows ensure value individually correct leave assembling strange looking string franklin however there one circumstance jdbc url instead cloud provider internal system resulted database requires ssl connection jdbc url configuration start server case like applicationrun serve dbconnectionstring jdbcpostgresqllocalhostfranklinuserfranklinpasswordfranklinssltrue constraint originally discovered google cloud platform environment appears relevant azure setting well withtiles enabling withtiles flag add different sort tile rendering item raster tile item cog asset get additional link relationship tile tile information include available tile matrix set webmercatorquad service url template franklin serve png tile url item collection item footprint tile collection get additional link relationship tile link include information item raster tile instead raster tile franklin serve mapbox vector tile mvt footprint item collection mvts include withfield query parameter property item label style client pas multiple withfield parameter include multiple field vector tile output field missing underlying item rendered resulting mvt label item data footprint label item imported static catalog get asset role datacollection asset collection also footprint start server withtiles flag mvts include withfield query parameter property item label style client pas multiple withfield parameter include multiple field vector tile output field missing underlying item rendered resulting mvt withtransactions enabling withtransactions flag add endpoint creating editing deleting item creating collection endpoint useful deployment scenario dont data youll want serve front transaction extension documented stac api specification franklin added endpoint creating collection well