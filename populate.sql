INSERT INTO `parliament_person`(`id_num`, `name`, `email`) VALUES (1111,"alice wonderland","alice@wonderland.com");
INSERT INTO `parliament_person` VALUES (2222,"bob builder","bob@builder.com");
INSERT INTO `parliament_person` VALUES (3333,"clair de lune boudair","clair@boudair.com");
INSERT INTO `parliament_person` VALUES (4444,"dionisus draconius","dionisus@draconius.com");
INSERT INTO `parliament_person` VALUES (5555,"someone anonymous","someone@anonymous.com");

INSERT INTO `parliament_tag`(`name`, `desc`) VALUES ("cm-cascais", "sem descrição");
INSERT INTO `parliament_tag` VALUES ("cm-lisboa", "sem descrição");
INSERT INTO `parliament_tag` VALUES ("cm-faro", "sem descrição");
INSERT INTO `parliament_tag` VALUES ("cm-porto", "sem descrição");
INSERT INTO `parliament_tag` VALUES ("parque", "sem descrição");
INSERT INTO `parliament_tag` VALUES ("reparação", "sem descrição");
INSERT INTO `parliament_tag` VALUES ("nova-construção", "sem descrição");
INSERT INTO `parliament_tag` VALUES ("iniciativa", "sem descrição");
INSERT INTO `parliament_tag` VALUES ("jf-carcavelos", "sem descrição");

INSERT INTO `parliament_proposal`(`id_num`, `author_id`, `title`, `desc`, `reasons`, `upvotes`, `downvotes`, `views`, `timestamp`) VALUES (1,1111,"Elevar Cascais a distrito","desc1","reasons1",1,0,0,"2012-09-04 14:13:12");
INSERT INTO `parliament_proposal` VALUES (2,2222,"Terminar o parque Quinta de Rana","desc2","reasons2",2,1,10,"2012-09-04 14:14:12");
INSERT INTO `parliament_proposal` VALUES (3,3333,"Expandir o parque Eduardo Sétimo até à rotunda do Marquês de Pombal","desc3","reasons3",5,0,100,"2012-09-04 14:15:12");
INSERT INTO `parliament_proposal` VALUES (4,4444,"A ponte Dona Maria devia ser um jardim","desc4","reasons4",1,4,500,"2012-09-04 14:16:12");
INSERT INTO `parliament_proposal` VALUES (5,4444,"Era vir charters todos os dias para Faro","desc5","reasons5",123456,987,300,"2012-09-04 15:14:13");
INSERT INTO `parliament_proposal` VALUES (6,5555,"Adoptar o 'dcid' em todas as Câmaras Municipais","Várias câmaras municipais já começaram a implementar Orçamentos Participativos. Infelizmente, cada câmara gasta tempo  e dinheiro público a desenvolver o seu próprio site de votação online (reinventando a roda). Proponho que todas as Câmaras Municipais com OPs usem o 'dcid' como plataforma de suporte.","Poupa-se dinheiro público; Criam-se sinergias pois todas as CMs trabalham para mnelhorar a mesma plataforma; Os cidadãos habituam-se a utilizar uma só plataforma; Incentiva-se a participação democrática dos munícipes e cidadãos em geral.",131,7,1000,"2013-03-10 14:13:12");

INSERT INTO `parliament_tag_tagged_proposals`(`tag_id`, `proposal_id`) VALUES ("cm-cascais", 1);
INSERT INTO `parliament_tag_tagged_proposals` VALUES ("cm-cascais", 2);
INSERT INTO `parliament_tag_tagged_proposals` VALUES ("parque", 2);
INSERT INTO `parliament_tag_tagged_proposals` VALUES ("cm-lisboa", 3);
INSERT INTO `parliament_tag_tagged_proposals` VALUES ("parque", 3);
INSERT INTO `parliament_tag_tagged_proposals` VALUES ("nova-construção", 3);
INSERT INTO `parliament_tag_tagged_proposals` VALUES ("cm-porto", 4);
INSERT INTO `parliament_tag_tagged_proposals` VALUES ("reparação", 4);
INSERT INTO `parliament_tag_tagged_proposals` VALUES ("parque", 4);
INSERT INTO `parliament_tag_tagged_proposals` VALUES ("cm-faro", 5);
INSERT INTO `parliament_tag_tagged_proposals` VALUES ("iniciativa", 5);
