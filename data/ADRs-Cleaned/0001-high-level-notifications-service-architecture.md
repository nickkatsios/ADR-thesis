high level notification service architecture proposed many system requirement send notification user general enough requirement addressed standalone service service able support creation retrieval notification user categorisation notification multiple delivery channel email push notification etc delivery read tracking supported specific delivery channel configuration delivery per user notification category channel query notification query api notification store create notification management api update notification delivery channel sendgrid twilio etc service core service implemented via two apis management api create notification update deliveryread management operation might required future query api application presenting notification user sense query api special case delivery channel storage expect azure table storage store raw notification user partition key notification sequence number row key delivery channel make solution extensible possible core api handle notification delivery envisaged handled delivery channel integrated via webhooks expected implementation approach many delivery channel would power automatelogicapps connector available many extenal messaging service already sendgrid twilio envisage integration management delivery apis follows available delivery channel registered management api registration would likely include display name uri new notification posted defined data structure order specific category notification sent delivery channel additional configuration required channel specific example template convert notification data email well necessary configure per user notification category delivery channel order make easier envisage hierarchical categorisation system allowing configuration defined level category hierarchy mentioned query api special case delivery channel require special configuration notification available via api supported allow delivery channel update notification delivery read via callback url notification categorisation categorisation notification two related purpose allow peruser configuration different delivery channel category notification control display formatting category notification support hierarchy category expressed via dotnotation example set notification category could follows marainworkflowsinstancecreated marainworkflowsinstancestatechange marainworkflowsinstancecompleted marainworkflowsinstancefaulted maraintenancytenantcreated marainoperationsoperationstarted marainoperationsoperationfailed expect able provide configuration different level hierarchy example user could configure email notification category marainworkflows ensuring receive email notifcations four subcategories could also configure specific notification marainworkflowsinstancefaulted category