-- Bot database
CREATE DATABASE IF NOT EXISTS `aiess_bot_test`;
USE `aiess_bot_test`;

DROP TABLE IF EXISTS `prefixes`;
CREATE TABLE `prefixes` (
  `guild_id` bigint(20) unsigned NOT NULL,
  `prefix` mediumtext,
  PRIMARY KEY (`guild_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `subscriptions`;
CREATE TABLE `subscriptions` (
  `guild_id` bigint(20) unsigned NOT NULL,
  `channel_id` bigint(20) unsigned NOT NULL,
  `filter` mediumtext NOT NULL,
  PRIMARY KEY (`guild_id`,`channel_id`),
  UNIQUE KEY `UNIQUE` (`channel_id`,`guild_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `permissions`;
CREATE TABLE `permissions` (
  `guild_id` bigint(20) unsigned NOT NULL,
  `command_name` varchar(60) NOT NULL,
  `permission_filter` mediumtext,
  PRIMARY KEY (`guild_id`,`command_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Scraper database
CREATE DATABASE IF NOT EXISTS `aiess_test`;
USE `aiess_test`;

DROP TABLE IF EXISTS `beatmapset_modes`;
CREATE TABLE `beatmapset_modes` (
  `beatmapset_id` bigint(20) unsigned NOT NULL,
  `mode` varchar(20) NOT NULL,
  PRIMARY KEY (`beatmapset_id`,`mode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` bigint(20) unsigned NOT NULL,
  `name` mediumtext,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `group_users`;
CREATE TABLE `group_users` (
  `group_id` bigint(20) unsigned NOT NULL,
  `user_id` bigint(20) unsigned NOT NULL,
  PRIMARY KEY (`group_id`,`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `beatmapsets`;
CREATE TABLE `beatmapsets` (
  `id` bigint(20) unsigned NOT NULL,
  `title` mediumtext,
  `artist` mediumtext,
  `creator_id` bigint(20) unsigned NOT NULL,
  `genre` mediumtext,
  `language` mediumtext,
  `tags` mediumtext,
  PRIMARY KEY (`id`),
  KEY `beatmapsetsfk_creator_id_idx` (`creator_id`),
  CONSTRAINT `beatmapsetsfk_creator_id` FOREIGN KEY (`creator_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `discussions`;
CREATE TABLE `discussions` (
  `id` bigint(20) unsigned NOT NULL,
  `beatmapset_id` bigint(20) unsigned NOT NULL,
  `user_id` bigint(20) unsigned NOT NULL,
  `content` mediumtext,
  `tab` mediumtext,
  `difficulty` mediumtext,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `discussionsfk_beatmapset_id_idx` (`beatmapset_id`),
  KEY `discussionsfk_user_id_idx` (`user_id`),
  CONSTRAINT `discussionsfk_beatmapset_id` FOREIGN KEY (`beatmapset_id`) REFERENCES `beatmapsets` (`id`),
  CONSTRAINT `discussionsfk_user_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `events`;
CREATE TABLE `events` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `insert_time` datetime NOT NULL,
  `time` datetime NOT NULL,
  `type` varchar(64) NOT NULL,
  `beatmapset_id` bigint(20) unsigned DEFAULT NULL,
  `discussion_id` bigint(20) unsigned DEFAULT NULL,
  `user_id` bigint(20) unsigned DEFAULT NULL,
  `group_id` bigint(20) unsigned DEFAULT NULL,
  `group_mode` varchar(20) DEFAULT NULL,
  `news_id` bigint(20) unsigned DEFAULT NULL,
  `content` mediumtext,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `newsposts`;
CREATE TABLE `newsposts` (
  `id` bigint(20) unsigned NOT NULL,
  `title` mediumtext NOT NULL,
  `preview` mediumtext NOT NULL,
  `author_id` bigint(20) unsigned DEFAULT NULL,
  `author_name` mediumtext NOT NULL,
  `slug` mediumtext NOT NULL,
  `image_url` mediumtext NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `newsposts_author_id_fk_idx` (`author_id`),
  CONSTRAINT `newsposts_author_id_fk` FOREIGN KEY (`author_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `discussion_obv_sev`;
CREATE TABLE `discussion_obv_sev` (
  `id` bigint(20) unsigned NOT NULL,
  `obv` INT unsigned NOT NULL,
  `sev` INT unsigned NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  CONSTRAINT `discussion_obv_sev_id` FOREIGN KEY (`id`) REFERENCES `discussions` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;