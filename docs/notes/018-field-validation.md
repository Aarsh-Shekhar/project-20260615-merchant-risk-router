# Field Validation

Domain: fintech

This note records an implementation detail for Merchant Risk Router. The current operating
threshold is `0.41` and review should happen within `8` hours
for records above that level.

## Checks

- confirm input fields are present
- verify score ordering is stable
- compare high exposure records against the review queue
