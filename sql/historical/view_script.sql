CREATE OR REPLACE VIEW `airy-parsec-400006.exoplanet_dataset.test_view` AS
(
  SELECT pl_name, hostname
  FROM `airy-parsec-400006.exoplanet_dataset.planetary_systems`
)
;
