-- ************************************** `races`

CREATE TABLE `races`
(
    `id`                varchar(45) NOT NULL ,
    `race_name`         varchar(45) NOT NULL ,
    `race_place`        varchar(45) NULL ,
    `number_of_entries` int NULL ,
    `race_state`        varchar(45) NULL,
    `date`              varchar(45) NULL ,

    PRIMARY KEY (`id`)
);

-- ************************************** `race_results`

CREATE TABLE `race_results`
(
    `horse_id`       varchar(45) NOT NULL ,
    `id`             varchar(45) NOT NULL ,
    `rank`           varchar(45) NULL ,
    `box`            varchar(45) NULL ,
    `horse_order`    varchar(45) NULL ,
    `horse_name`     varchar(45) NULL ,
    `sex_and_age`    varchar(45) NULL ,
    `burden_weight`  varchar(45) NULL ,
    `jockey`         varchar(45) NULL ,
    `time`           varchar(45) NULL ,
    `difference`     varchar(45) NULL ,
    `transit`        varchar(45) NULL ,
    `climb`          varchar(45) NULL ,
    `odds`           varchar(45) NULL ,
    `popularity`     varchar(45) NULL ,
    `horse_weight`   varchar(45) NULL ,
    `horse_trainer`  varchar(45) NULL ,
    `horse_owner`    varchar(90) NULL ,
    `prize`          varchar(45) NULL ,

    PRIMARY KEY (`horse_id`),
    KEY `FK_1` (`id`),
    CONSTRAINT `FK_2` FOREIGN KEY `FK_1` (`id`) REFERENCES `races` (`id`)
);