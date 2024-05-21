{{ config(materialized='table') }}

select
    animal_id,
    farmer_id,
    species,
    breed,
    birthdate,
    sex
from {{ ref('stg_animal_records') }}
