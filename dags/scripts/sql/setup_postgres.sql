DROP TABLE IF EXISTS data_top_level_domains;

CREATE TABLE IF NOT EXISTS data_top_level_domains
(
    date date NOT NULL,
    domain varchar(30) NOT NULL,
    CONSTRAINT top_level_domains_pkey PRIMARY KEY (date, domain)
);

DROP TABLE IF EXISTS data_s_and_p_500;

CREATE TABLE IF NOT EXISTS data_s_and_p_500
(
    date date NOT NULL,
    sector varchar(30) NOT NULL,
    count integer NOT NULL,
    CONSTRAINT s_and_p_500_pkey PRIMARY KEY (date, sector)
);
