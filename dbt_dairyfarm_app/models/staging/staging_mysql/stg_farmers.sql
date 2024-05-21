{{ config(materialized='view') }}

with source as (
    select * from {{ source('mysql', 'farmers') }}
)

select
    farmer_id,
    username,
    email,
    phone,
    address
from source
