partial row complete cell batching gettimestampsbycell version implementation dbkvsgettimestampsbycell creating multimap pair cell timestamp range determined row batch size case wide row simply row batch size large could cause run memory see issue decided block triple row name column name timestamp batch size defaulting avoid loading many block memory algorithm fetch block row column increasing timestamp batch size met case least one row fully processed return rowresults timestamps row continue processing beginning current row rowresults necessary row fully processed continue processing block end current cell row column fetching timestamps cell return partial rowresult contains timestamps row including final cell processed create next rowresult continue processing row last cell processed effectively splitting wide row several rowresults example assuming batch size following table rowresults follows considered partial row batching fetch block block batch size hit stop immediately cell split across multiple batch full row batching fetch block block batch size hit middle row continue fetching row exhausted batching throw error block batch hint reached considered replaced modified version sweep must ensure block except recent immutable timestamp deleted achieved repeating last block one batch next batch keeping last result sweep memory know remove block cell encountered neither compelling first hard reason second reduces scope parallelisation risk introducing correctness bug chosen guard well wide row many cell many overwrites considered ultimately discarded relies property code call getcelltimestamps particular retry logic detects error thrown reduces batch size accordingly consequence row wider value batch size dbkvsgettimestampsbycell may split several rowresults