{{ config(materialized='view') }}

with source as (
    select * from {{ source('mongo', 'user_activity') }}
)

select
    _id as activity_id,
    user_id as farmer_id,
    activity_type,
    activity_details,
    timestamp,
    ip_address,
    device_type,
    browser,
    os,
    referrer,
    country,
    city,
    latitude,
    longitude,
    duration,
    event_value,
    event_label,
    user_agent,
    language,
    session_id,
    campaign_source,
    campaign_medium,
    campaign_name
from source
