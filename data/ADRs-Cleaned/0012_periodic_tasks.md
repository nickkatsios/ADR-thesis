title periodic task weight problem statement currently scheduler consumes task queue database allows multiple job executor running parallel racing next job execute executing task immediately long enough resource missing component maintains periodic task reason house keeping task run regularily clean stale unused data later user able create periodic task example read email inbox notified due item problem must work multiple job executor instance running time pattern scheduler must ensured one task time multiple job exectuors must schedule perdiodic task periodic task take longer time run must wait next interval considered adding timer nextrun field current job table creating separate table periodic task outcome internal housekeeping task may suffice reuse existing job queue adding field job may considered periodic conflates scheduler executing task soon possible bound resource limit completely different subject new periodicscheduler work new table database representing periodic task table share field job table able create rjob record new component taking care periodically submitting job job queue scheduler eventually pick run task cannot run example due resource limitation periodic scheduler cant nothing wait try next time sql create table periodictask varchar null primary key enabled boolean null task varchar null group varchar null args text null subject varchar null submitter varchar null priority int null worker varchar marked timestamp timer varchar null nextrun timestamp null created timestamp null preparing feature point periodic task created user possible disableenable next property needed insert job job table worker field marked mark periodic job worked job executor timer schedule systemdlike calendar event string parsed library nextrun field store timestamp next time task would executed needed query table newest task periodicscheduler work roughly like startup remove stale worker value process killed may marked task must cleared mainloop cancel current scheduled notify see get next earliest enabled periodic job none stop triggered nextrun mark periodic task fail goto submit new job jobqueue update nextrun field check nonfinal job name required run periodic task multiple time concurrently exist goto exist submit job unmark periodic task future schedule notify notify self run next time task schedule trigger