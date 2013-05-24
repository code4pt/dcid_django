-- fix Django's ORM limitations
ALTER TABLE `parliament_tag_tagged_proposals` DROP `id`;
ALTER TABLE  `parliament_tag_tagged_proposals` ADD PRIMARY KEY (  `tag_id` ,  `proposal_id` ) ;