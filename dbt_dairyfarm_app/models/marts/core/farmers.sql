{{ config(materialized='table') }}

select
    farmer_id,
    username,
    email,
    phone,
    address
from {{ ref('stg_farmers') }}
