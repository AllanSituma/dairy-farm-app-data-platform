{{ config(materialized='table') }}

select
    activity_id,
    farmer_id,
    animal_id,
    activity_type,
    activity_date,
    description
from {{ ref('stg_activity_tracking') }}
