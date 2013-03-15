ALTER TABLE `parliament_tag_tagged_proposals` DROP `id`;
ALTER TABLE  `parliament_tag_tagged_proposals` ADD PRIMARY KEY (  `tag_id` ,  `proposal_id` ) ;

ALTER TABLE `parliament_proposalvote` DROP `id`;
ALTER TABLE  `parliament_proposalvote` ADD PRIMARY KEY (  `who_id` ,  `what_id` ) ;