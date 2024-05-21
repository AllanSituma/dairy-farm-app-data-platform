{{ config(materialized='view') }}

with source as (
    select * from {{ source('mysql', 'inventory') }}
)

select
    item_id,
    farmer_id,
    item_name,
    quantity,
    price
from source
