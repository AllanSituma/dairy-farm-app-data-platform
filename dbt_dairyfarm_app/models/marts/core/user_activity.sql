{{ config(materialized='table') }}

select
    activity_id,
    farmer_id,
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
from {{ ref('stg_user_activity') }}
