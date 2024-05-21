{{ config(materialized='view') }}

with source as (
    select * from {{ source('mysql', 'activity_tracking') }}
)

select
    activity_id,
    farmer_id,
    animal_id,
    activity_type,
    activity_date,
    description
from source
