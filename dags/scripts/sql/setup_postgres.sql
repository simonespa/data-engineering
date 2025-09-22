CREATE TABLE IF NOT EXISTS top_level_domains
(
    date date NOT NULL,
    domain varchar(30) NOT NULL,
    CONSTRAINT top_level_domains_pkey PRIMARY KEY (date, domain)
);
