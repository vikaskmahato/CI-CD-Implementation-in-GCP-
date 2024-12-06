CREATE OR REPLACE VIEW `airy-parsec-400006.exoplanet_dataset.testview` AS
(
  SELECT pl_name, hostname, pl_orbper FROM `airy-parsec-400006.exoplanet_dataset.planetary_systems`
)
;
