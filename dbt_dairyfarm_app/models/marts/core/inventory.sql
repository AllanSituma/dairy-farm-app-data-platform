{{ config(materialized='table') }}

select
    item_id,
    farmer_id,
    item_name,
    quantity,
    price
from {{ ref('stg_inventory') }}
