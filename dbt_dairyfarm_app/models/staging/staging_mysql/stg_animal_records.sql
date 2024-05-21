{{ config(materialized='view') }}

with source as (
    select * from {{ source('mysql', 'animal_records') }}
)

select
    animal_id,
    farmer_id,
    species,
    breed,
    birthdate,
    sex
from source
