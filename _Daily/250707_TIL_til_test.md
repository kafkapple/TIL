---
created: 2025-07-07T09:55:00
date: 2025-07-07
weekday: Monday
note_id: "N_dof2c63o"
category: "TIL"
tags: [TIL, daily]
context_type: "none"
active: true
template_version: "2.0"
modified: 2025-07-07T18:55:16
---
# 250707 TIL - til test (Monday)
## Overview
-
## What I Learned
- dataview
TABLE date as "Date", context_name as "Context", file.name as "File"
FROM ""
WHERE category = "TIL" AND file.name != "250707_TIL_til_test"
SORT date DESC
LIMIT 5
```
## Recent Notes
```dataview
TABLE date as "Date", category as "Category", file.name as "File"
FROM ""
WHERE file.name != "250707_TIL_til_test"
SORT file.cday DESC
LIMIT 5
```