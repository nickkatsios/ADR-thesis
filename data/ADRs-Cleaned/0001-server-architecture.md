server architecture timely dataflow system made number worker peer running exact dataflows timely worker expect run full speed without blocking initial design therefore extend worker loop nonblocking networking accepting pure tcp websocket connection worker may accept client command worker utilize timelys sequencer primitive ensure every worker process command order busy loop worker accept new client connection accept command connection push sequencer step registered dataflows forward result client keeping everything within single loop easily experiment tradeoff limiting number command consumed order ensure timely progress registered query vice versa want client access power whole cluster talking single peer achieved notion owner worker manages client connection originally given request worker forward result back owner apart connection state worker thus also maintain mapping query name list client interested worker maintain mapping client connected thus mapping vary worker worker design also make easy move part loop thread become neccessary running top external sourceoftruth separate dedicated event loop might run consume connection full speed consequence existing websocket library seem run encapsulated event loop thus neccessary fork wsrshttpsgithubcomcomnikwsrs care must taken always step worker even query registered otherwise sequencer dataflow make progress