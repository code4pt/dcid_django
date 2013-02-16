INSERT INTO `parliament_person`(`id_num`, `name`, `email`) VALUES (1111,"alice wonderland","alice@wonderland.com");
INSERT INTO `parliament_person` VALUES (2222,"bob builder","bob@builder.com");
INSERT INTO `parliament_person` VALUES (3333,"clair de lune boudair","clair@boudair.com");
INSERT INTO `parliament_person` VALUES (4444,"dionisus draconius","dionisus@draconius.com");

INSERT INTO `parliament_tag`(`name`, `desc`) VALUES ("cm-cascais", "sem descrição");
INSERT INTO `parliament_tag` VALUES ("cm-lisboa", "sem descrição");
INSERT INTO `parliament_tag` VALUES ("cm-faro", "sem descrição");
INSERT INTO `parliament_tag` VALUES ("cm-porto", "sem descrição");
INSERT INTO `parliament_tag` VALUES ("parque", "sem descrição");
INSERT INTO `parliament_tag` VALUES ("reparação", "sem descrição");
INSERT INTO `parliament_tag` VALUES ("nova-construção", "sem descrição");
INSERT INTO `parliament_tag` VALUES ("iniciativa", "sem descrição");
INSERT INTO `parliament_tag` VALUES ("jf-carcavelos", "sem descrição");

INSERT INTO `parliament_proposal`(`id`, `author_id`, `title`, `desc`, `reasons`, `upvotes`, `downvotes`, `views`, `timestamp`) VALUES (1,1111,"Elevar Cascais a distrito","desc1","reasons1",1,0,0,"2012-09-04 14:13:12");
INSERT INTO `parliament_proposal` VALUES (2,2222,"Terminar o parque Quinta de Rana","desc2","reasons2",2,1,0,"2012-09-04 14:14:12");
INSERT INTO `parliament_proposal` VALUES (3,3333,"Expandir o parque Eduardo Sétimo até à rotunda do Marquês de Pombal","desc3","reasons3",5,0,0,"2012-09-04 14:15:12");
INSERT INTO `parliament_proposal` VALUES (4,4444,"A ponte Dona Maria devia ser um jardim","desc4","reasons4",1,4,0,"2012-09-04 14:16:12");
INSERT INTO `parliament_proposal` VALUES (5,4444,"Era vir charters todos os dias para Faro","desc5","reasons5",123456,987,0,"2012-09-04 15:14:13");

INSERT INTO `parliament_tag_tagged_proposals`(`id`, `tag_id`, `proposal_id`) VALUES (1, "cm-cascais", 1);
INSERT INTO `parliament_tag_tagged_proposals` VALUES (2, "cm-cascais", 2);
INSERT INTO `parliament_tag_tagged_proposals` VALUES (3, "parque", 2);
INSERT INTO `parliament_tag_tagged_proposals` VALUES (4, "cm-lisboa", 3);
INSERT INTO `parliament_tag_tagged_proposals` VALUES (5, "parque", 3);
INSERT INTO `parliament_tag_tagged_proposals` VALUES (6, "nova-construção", 3);
INSERT INTO `parliament_tag_tagged_proposals` VALUES (7, "cm-porto", 4);
INSERT INTO `parliament_tag_tagged_proposals` VALUES (8, "reparação", 4);
INSERT INTO `parliament_tag_tagged_proposals` VALUES (9, "parque", 4);
INSERT INTO `parliament_tag_tagged_proposals` VALUES (10, "cm-faro", 5);
INSERT INTO `parliament_tag_tagged_proposals` VALUES (11, "iniciativa", 5);
