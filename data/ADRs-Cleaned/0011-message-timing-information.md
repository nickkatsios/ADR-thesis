message timing information decide whether message timing information exposed via api timing information refers important point time throughout lifecycle message initial rationale exposing timestamps business logic depends time way explicitly include timing information within message call logic timebased approach including explicit timing information modeling time section focus message role respective timestamps interest made case command message believe existing requirement application model time still appropriate command message time command message created enqueued irrelevant time information relevant domain logic included message decided expose command creation time event message time event recorded fundamental property event put another way every event occurs time regardless whether domain timebased furthermore time event occurs may relevant ancillary domain logic triggered event even aggregate produced event timebased logic inclusion occurred time fundamental property event supported implementing domain driven design chapter modeling event section decided include recordedat method processeventscope projectioneventscope actuality time method already added projectioneventscope without supporting adr method renamed timeout message time timeout message scheduled handled fundamental property timeout concept definition timeout message indicates timebased logic seems like unnecessary imposition require application developer include scheduled time message decided include scheduledfor method processtimeoutscope consequence result adr easier application developer implement timebased logic engine implementation must record time event occur necessarily true likely engine would done anyway